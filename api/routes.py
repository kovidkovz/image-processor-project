from fastapi import APIRouter

router = APIRouter()

UPLOAD              = "/upload"
STATUS              = "/status/{request_id}"
WEBHOOK             = "/webhook"