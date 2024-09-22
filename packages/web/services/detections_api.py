import requests


def detections_api(
    selected_image,
    woodland_johor_bridge_image_url,
    tuas_second_link_image_url,
    woodland_checkpoint_image_url,
    towards_woodland_checkpoint_image_url,
    tuas_checkpoint_image_url
):
    result = None

    try:
        root_url = "http://localhost:8000"

        json_data = {
            "selected_image": selected_image,
            "woodland_johor_bridge_image_url": woodland_johor_bridge_image_url,
            "tuas_second_link_image_url": tuas_second_link_image_url,
            "woodland_checkpoint_image_url": woodland_checkpoint_image_url,
            "towards_woodland_checkpoint_image_url": towards_woodland_checkpoint_image_url,
            "tuas_checkpoint_image_url": tuas_checkpoint_image_url
        }

        response = requests.post(f"{root_url}/detections", json=json_data)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json
    except Exception as e:
        print(f"detections_api error = {e}")

    return result
