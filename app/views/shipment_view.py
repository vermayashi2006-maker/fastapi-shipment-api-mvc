
"""Response formatting for shipment endpoints."""


def shipment_response(shipment):
    return {
        "id": shipment.id,
        "content": shipment.content,
        "weight": shipment.weight,
        "expected_delivery": shipment.expected_delivery,
        "destination": shipment.destination,
        "status": shipment.status,
    }


def shipments_response(shipments):
    return [shipment_response(shipment) for shipment in shipments]
