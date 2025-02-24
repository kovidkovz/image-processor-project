from fastapi import HTTPException
from services.db_handler import mark_request_completed

async def webhook_logic(request_id: str):
    if not await mark_request_completed(request_id):
        raise HTTPException(status_code=404, detail="Request ID not found.")
    return {"status": "Processing completed."}
