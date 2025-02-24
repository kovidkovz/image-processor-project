from routes import STATUS, router


@router.get(STATUS)
async def get_status(request_id: str):
    status = await get_request_status(request_id)
    if not status:
        raise HTTPException(status_code=404, detail="Request ID not found.")
    return {"request_id": request_id, "status": status}