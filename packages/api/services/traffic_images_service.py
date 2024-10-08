import os
import requests


def get_images_api():
    result = {}

    try:
        root_url = "https://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2"

        account_key = os.getenv("ACCOUNT_KEY")

        headers = {
            "AccountKey": account_key
        }

        response = requests.get(root_url, headers=headers)
        print(f"response = {response}")

        if response.status_code == 200:
            response_json = response.json()
            # print(f"response_json = {response_json}")

            if response_json:
                values = response_json.get("value")

                if values:
                    for item in values:
                        camera_id = item.get("CameraID")
                        latitude = item.get("Latitude")
                        longitude = item.get("Longitude")
                        image_link = item.get("ImageLink")

                        if camera_id == "2701":
                            data = {
                                "camera_id": camera_id,
                                "latitude": latitude,
                                "longitude": longitude,
                                "image_link": image_link
                            }
                            result["woodland_johor_bridge"] = data

                        if camera_id == "4703":
                            data = {
                                "camera_id": camera_id,
                                "latitude": latitude,
                                "longitude": longitude,
                                "image_link": image_link
                            }
                            result["tuas_second_link"] = data

                        if camera_id == "2702":
                            data = {
                                "camera_id": camera_id,
                                "latitude": latitude,
                                "longitude": longitude,
                                "image_link": image_link
                            }
                            result["woodland_checkpoint"] = data

                        if camera_id == "2704":
                            data = {
                                "camera_id": camera_id,
                                "latitude": latitude,
                                "longitude": longitude,
                                "image_link": image_link
                            }
                            result["towards_woodland_checkpoint"] = data

                        if camera_id == "4713":
                            data = {
                                "camera_id": camera_id,
                                "latitude": latitude,
                                "longitude": longitude,
                                "image_link": image_link
                            }
                            result["tuas_checkpoint"] = data

        result["malaysia_ciq_1"] = {
            "camera_id": "",
            "latitude": 0,
            "longitude": 0,
            "image_link": "https://c1.cgies.com/mbciq/CIQ1W.jpg"
        }

        result["malaysia_ciq_2"] = {
            "camera_id": "",
            "latitude": 0,
            "longitude": 0,
            "image_link": "https://c1.cgies.com/mbciq/CIQ2W.jpg"
        }

        for index in range(1, 11):
            if index >= 1 and index <= 9 and index != 8:
                result[f"malaysia_second_link_0{index}"] = {
                    "camera_id": "",
                    "latitude": 0,
                    "longitude": 0,
                    "image_link": f"https://c1.cgies.com/bucket-link2/LINK2-0{index}.jpg"
                }
            if index == 10:
                result[f"malaysia_second_link_{index}"] = {
                    "camera_id": "",
                    "latitude": 0,
                    "longitude": 0,
                    "image_link": f"https://c1.cgies.com/bucket-link2/LINK2-{index}.jpg"
                }
    except Exception as e:
        print(f"get_images_api error = {e}")

    return result
