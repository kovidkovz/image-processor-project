from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.upload import upload_file
from api.status import get_status
from api.webhook import webhook_logic
import uvicorn
import os
from api.routes import UPLOAD, STATUS, WEBHOOK

app = FastAPI()

# upload api
@app.post(UPLOAD)
async def upload(request: Request):
    payload, status_code = await upload_file(request)
    return JSONResponse(content= payload, status_code= status_code)

# status api
@app.get(STATUS)
async def status(request: Request):
    payload, status_code = await get_status(request)
    return JSONResponse(content= payload, status_code= status_code)

# webhook
@app.get(WEBHOOK)
async def webhook(request: Request):
    payload, status_code = await webhook_logic(request)
    return JSONResponse(content= payload, status_code= status_code)

# run the server
if __name__ == "__main__":
    is_debug = os.getenv("DEBUG", "0") == "1"
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=is_debug)
