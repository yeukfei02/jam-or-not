from fastapi import Request, status
from fastapi.responses import JSONResponse
from services.traffic_images_service import get_images_api


def traffic_images_controller(request: Request):
    data = {
        "message": "traffic-images",
        "result": {}
    }

    image_result = get_images_api()
    if image_result:
        data = {
            "message": "traffic-images",
            "result": image_result
        }

    response = JSONResponse(status_code=status.HTTP_200_OK, content=data)
    return response
