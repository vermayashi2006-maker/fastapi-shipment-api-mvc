
from fastapi import HTTPException
from sqlmodel import Session, select
from app.views.shipment_view import shipment_response, shipments_response
from app.models.shipment import Shipment
from schemas import Ship, ShipmentPatch



def create_shipment(session: Session, shipment_data: Ship) -> Shipment:
    shipment = Shipment(**shipment_data.model_dump())
    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment_response(shipment)



def get_all_shipments(session: Session):
    shipments = list(session.exec(select(Shipment)).all())
    return shipments_response(shipments)


def get_shipment_by_id(session: Session, shipment_id: int):
    shipment = session.get(Shipment, shipment_id)

    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")

    return shipment_response(shipment)



def update_shipment(session: Session, shipment_id: int, shipment_data: Ship):
    shipment = session.get(Shipment, shipment_id)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")

    for field, value in shipment_data.model_dump().items():
        setattr(shipment, field, value)

    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment_response(shipment)




def patch_shipment(session: Session, shipment_id: int, shipment_data: ShipmentPatch):
    shipment = session.get(Shipment, shipment_id)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")

    for field, value in shipment_data.model_dump(exclude_unset=True).items():
        setattr(shipment, field, value)

    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment_response(shipment)



def delete_shipment(session: Session, shipment_id: int) -> dict:
    shipment = get_shipment_by_id(session, shipment_id)

    session.delete(shipment)
    session.commit()

    return {"message": "Shipment deleted successfully"}
