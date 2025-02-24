from fastapi import FastAPI
from api import upload, status, webhook
import uvicorn
import os

app = FastAPI(title="Image Processor API")

# Include API routers
app.include_router(upload.router, prefix="/api/v1")
app.include_router(status.router, prefix="/api/v1")
app.include_router(webhook.router, prefix="/api/v1")
from fastapi import FastAPI
from api import upload, status, webhook

app = FastAPI(title="Image Processor API")

# Include API routers
app.include_router(upload.router, prefix="/api/v1")
app.include_router(status.router, prefix="/api/v1")
app.include_router(webhook.router, prefix="/api/v1")

# run the server
if __name__ == "__main__":
    is_debug = os.getenv("DEBUG", "0") == "1"
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=is_debug)
