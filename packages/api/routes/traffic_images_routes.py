from fastapi import APIRouter, Request
from controller.traffic_images_controller import traffic_images_controller

traffic_images_router = APIRouter()


@traffic_images_router.get("/traffic-images")
def get_traffic_images(request: Request):
    response = traffic_images_controller(request)
    return response
