import requests


def detections_api(
    selected_image,
    woodland_johor_bridge_image_url,
    tuas_second_link_image_url,
    woodland_checkpoint_image_url,
    towards_woodland_checkpoint_image_url,
    tuas_checkpoint_image_url,
    malaysia_ciq_1_image_url,
    malaysia_ciq_2_image_url,
    malaysia_second_link_01_image_url,
    malaysia_second_link_02_image_url,
    malaysia_second_link_03_image_url,
    malaysia_second_link_04_image_url,
    malaysia_second_link_05_image_url,
    malaysia_second_link_06_image_url,
    malaysia_second_link_07_image_url,
    malaysia_second_link_09_image_url,
    malaysia_second_link_10_image_url
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
            "tuas_checkpoint_image_url": tuas_checkpoint_image_url,
            "malaysia_ciq_1_image_url": malaysia_ciq_1_image_url,
            "malaysia_ciq_2_image_url": malaysia_ciq_2_image_url,
            "malaysia_second_link_01_image_url": malaysia_second_link_01_image_url,
            "malaysia_second_link_02_image_url": malaysia_second_link_02_image_url,
            "malaysia_second_link_03_image_url": malaysia_second_link_03_image_url,
            "malaysia_second_link_04_image_url": malaysia_second_link_04_image_url,
            "malaysia_second_link_05_image_url": malaysia_second_link_05_image_url,
            "malaysia_second_link_06_image_url": malaysia_second_link_06_image_url,
            "malaysia_second_link_07_image_url": malaysia_second_link_07_image_url,
            "malaysia_second_link_09_image_url": malaysia_second_link_09_image_url,
            "malaysia_second_link_10_image_url": malaysia_second_link_10_image_url
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
