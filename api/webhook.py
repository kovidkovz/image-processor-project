from fastapi import APIRouter, HTTPException
from app.services.db_handler import mark_request_completed

router = APIRouter()

@router.post("/webhook")
async def webhook(request_id: str):
    if not await mark_request_completed(request_id):
        raise HTTPException(status_code=404, detail="Request ID not found.")
    return {"status": "Processing completed."}
