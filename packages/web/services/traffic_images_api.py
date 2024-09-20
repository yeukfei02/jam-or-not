import requests


def traffic_images_api():
    result = None

    try:
        root_url = "http://localhost:8000"

        response = requests.get(f"{root_url}/traffic-images")
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json
    except Exception as e:
        print(f"traffic_images_api error = {e}")

    return result
