
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from sqlmodel import Session, select, or_

from app.routes.shipment_routes import router as shipment_router
from auth import (
    create_access_token,
    get_user,
    oauth_scheme,
    revoke_token,
    verify_token,
)
from database.models import User
from database.sessions import create_db_and_table, get_session
from hash import check_password, generate_password
from schemas import LoginResponse, LoginUser, UserCreate, UserResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables when the application starts.
    create_db_and_table()
    yield


app = FastAPI(
    title="Shipment Management API",
    lifespan=lifespan,
)

# Register shipment endpoints from the MVC routes layer.
app.include_router(shipment_router)


@app.post(
    "/create-user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_user(
    data: UserCreate,
    session: Session = Depends(get_session),
):
    existing_user = session.exec(
        select(User).where(
            or_(
                User.username == data.username,
                User.email == data.email,
            )
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email is already taken",
        )

    hashed = generate_password(data.password)

    new_user = User(
        username=data.username,
        email=data.email,
        password_hash=hashed,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@app.post("/login", response_model=LoginResponse)
def login_user(
    data: LoginUser,
    session: Session = Depends(get_session),
):
    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user or not check_password(
        data.password, user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(user.id)

    return LoginResponse(
        message="Login successful",
        userid=user.id,
        username=user.username,
        email=user.email,
        token=token,
    )


@app.get("/users/me", response_model=UserResponse)
def get_my_profile(
    current_user: User = Depends(get_user),
):
    return current_user


@app.post("/logout")
def logout_user(
    credentials: HTTPAuthorizationCredentials = Depends(oauth_scheme),
    session: Session = Depends(get_session),
):
    token = credentials.credentials

    # Validate the token before revoking it.
    verify_token(token)
    revoke_token(token, session)

    return {"message": "Logged out successfully"}
