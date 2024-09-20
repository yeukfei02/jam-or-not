from fastapi import APIRouter, Request
from controller.detections_controller import detections_controller

detections_router = APIRouter()


@detections_router.post("/detections")
async def get_detections(request: Request):
    response = await detections_controller(request)
    return response
