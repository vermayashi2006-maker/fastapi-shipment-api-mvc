
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.controllers import shipment_controller as controller
from database.sessions import get_session
from schemas import Ship, ShipmentPatch

router = APIRouter(tags=["Shipments"])


@router.post("/new-shipment", status_code=status.HTTP_201_CREATED)
def create_shipment(
    shipment_data: Ship,
    session: Session = Depends(get_session),
):
    return controller.create_shipment(session, shipment_data)


@router.get("/shipments")
def get_all_shipments(session: Session = Depends(get_session)):
    return controller.get_all_shipments(session)


@router.get("/shipments/{shipment_id}")
def get_shipment(
    shipment_id: int,
    session: Session = Depends(get_session),
):
    return controller.get_shipment_by_id(session, shipment_id)


@router.put("/shipments/{shipment_id}")
def update_shipment(
    shipment_id: int,
    shipment_data: Ship,
    session: Session = Depends(get_session),
):
    return controller.update_shipment(session, shipment_id, shipment_data)


@router.patch("/shipments/{shipment_id}")
def patch_shipment(
    shipment_id: int,
    shipment_data: ShipmentPatch,
    session: Session = Depends(get_session),
):
    return controller.patch_shipment(session, shipment_id, shipment_data)


@router.delete("/shipments/{shipment_id}")
def delete_shipment(
    shipment_id: int,
    session: Session = Depends(get_session),
):
    return controller.delete_shipment(session, shipment_id)
