from routes import STATUS, router
from services.db_handler import get_request_status
from fastapi import HTTPException


@router.get(STATUS)
async def get_status(request_id: str):
    status = await get_request_status(request_id)
    if not status:
        raise HTTPException(status_code=404, detail="Request ID not found.")
    return {"request_id": request_id, "status": status}