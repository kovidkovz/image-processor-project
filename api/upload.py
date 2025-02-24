from fastapi import UploadFile, HTTPException, BackgroundTasks
from routes import UPLOAD, router
from utils.helpers import build_response
from app.services.file_handler import process_csv
from app.services.db_handler import insert_request
from uuid import uuid4


@router.post(UPLOAD)
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
    
    request_id = str(uuid4())
    await insert_request(request_id)

    background_tasks.add_task(process_csv, file, request_id)
    
    return {"request_id": request_id, "status": "File received and processing started."}
