from fastapi import Request, status
from fastapi.responses import JSONResponse
from services.detection_service import supervision_detection


async def detections_controller(request: Request):
    data = {
        "message": "detections",
        "result": {}
    }

    body = await request.json()
    # print(f"body = {body}")

    if body:
        selected_image, to_johor_data_list, to_singapore_data_list, no_direction_total_data_list = supervision_detection(
            body)

        data = {
            "message": "detections",
            "result": {
                "selected_image": selected_image,
                "to_johor_data_list": to_johor_data_list,
                "to_singapore_data_list": to_singapore_data_list,
                "to_johor_number_of_vehicles": len(to_johor_data_list),
                "to_singapore_number_of_vehicles": len(to_singapore_data_list),
                "no_direction_total_data_list": no_direction_total_data_list,
                "no_direction_total_number_of_vehicles": len(no_direction_total_data_list)
            }
        }

    response = JSONResponse(status_code=status.HTTP_200_OK, content=data)
    return response
