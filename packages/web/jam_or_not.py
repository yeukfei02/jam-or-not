import time
import streamlit as st
import requests
from io import BytesIO
from services.traffic_images_api import traffic_images_api
from services.detections_api import detections_api


def get_selected_image_text(selected_image):
    selected_image_text = ""

    match selected_image:
        case "Woodland Johor Bridge":
            selected_image_text = "woodland_johor_bridge_image"
        case "Tuas Second Link":
            selected_image_text = "tuas_second_link_image"
        case "Woodland Checkpoint":
            selected_image_text = "woodland_checkpoint_image"
        case "Towards Woodland Checkpoint":
            selected_image_text = "towards_woodland_checkpoint_image"
        case "Tuas Checkpoint":
            selected_image_text = "tuas_checkpoint_image"
        case "Malaysia CIQ 1":
            selected_image_text = "malaysia_ciq_1_image"
        case "Malaysia CIQ 2":
            selected_image_text = "malaysia_ciq_2_image"
        case "Malaysia Second link 1":
            selected_image_text = "malaysia_second_link_01_image"
        case "Malaysia Second link 2":
            selected_image_text = "malaysia_second_link_02_image"
        case "Malaysia Second link 3":
            selected_image_text = "malaysia_second_link_03_image"
        case "Malaysia Second link 4":
            selected_image_text = "malaysia_second_link_04_image"
        case "Malaysia Second link 5":
            selected_image_text = "malaysia_second_link_05_image"
        case "Malaysia Second link 6":
            selected_image_text = "malaysia_second_link_06_image"
        case "Malaysia Second link 7":
            selected_image_text = "malaysia_second_link_07_image"
        case "Malaysia Second link 9":
            selected_image_text = "malaysia_second_link_09_image"
        case "Malaysia Second link 10":
            selected_image_text = "malaysia_second_link_10_image"

    return selected_image_text


@st.cache_data
def get_image(image_link):
    response = requests.get(image_link)
    return BytesIO(response.content)


st.title("Jam or not")

st.write("")

selected_image = st.selectbox(
    label="Select image",
    placeholder="Select image",
    options=[
        "Woodland Johor Bridge",
        "Tuas Second Link",
        "Woodland Checkpoint",
        "Towards Woodland Checkpoint",
        "Tuas Checkpoint",
        "Malaysia CIQ 1",
        "Malaysia CIQ 2",
        "Malaysia Second link 1",
        "Malaysia Second link 2",
        "Malaysia Second link 3",
        "Malaysia Second link 4",
        "Malaysia Second link 5",
        "Malaysia Second link 6",
        "Malaysia Second link 7",
        "Malaysia Second link 9",
        "Malaysia Second link 10"
    ],
)

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if selected_image:
        traffic_images_response = traffic_images_api()

        if traffic_images_response:
            result = traffic_images_response["result"]

            with st.spinner('Loading...'):
                time.sleep(2)

                camera_id = ""
                latitude = 0
                longitude = 0
                image_link = ""

                woodland_johor_bridge_image_url = ""
                tuas_second_link_image_url = ""
                woodland_checkpoint_image_url = ""
                towards_woodland_checkpoint_image_url = ""
                tuas_checkpoint_image_url = ""
                malaysia_ciq_1_image_url = ""
                malaysia_ciq_2_image_url = ""
                malaysia_second_link_01_image_url = ""
                malaysia_second_link_02_image_url = ""
                malaysia_second_link_03_image_url = ""
                malaysia_second_link_04_image_url = ""
                malaysia_second_link_05_image_url = ""
                malaysia_second_link_06_image_url = ""
                malaysia_second_link_07_image_url = ""
                malaysia_second_link_09_image_url = ""
                malaysia_second_link_10_image_url = ""

                match selected_image:
                    case "Woodland Johor Bridge":
                        woodland_johor_bridge = result.get(
                            "woodland_johor_bridge")

                        camera_id = woodland_johor_bridge.get("camera_id")
                        latitude = woodland_johor_bridge.get("latitude")
                        longitude = woodland_johor_bridge.get("longitude")
                        image_link = woodland_johor_bridge.get("image_link")

                        woodland_johor_bridge_image_url = image_link
                    case "Tuas Second Link":
                        tuas_second_link = result.get(
                            "tuas_second_link")

                        camera_id = tuas_second_link.get("camera_id")
                        latitude = tuas_second_link.get("latitude")
                        longitude = tuas_second_link.get("longitude")
                        image_link = tuas_second_link.get("image_link")

                        tuas_second_link_image_url = image_link
                    case "Woodland Checkpoint":
                        woodland_checkpoint = result.get(
                            "woodland_checkpoint")

                        camera_id = woodland_checkpoint.get("camera_id")
                        latitude = woodland_checkpoint.get("latitude")
                        longitude = woodland_checkpoint.get("longitude")
                        image_link = woodland_checkpoint.get("image_link")

                        woodland_checkpoint_image_url = image_link
                    case "Towards Woodland Checkpoint":
                        towards_woodland_checkpoint = result.get(
                            "towards_woodland_checkpoint")

                        camera_id = towards_woodland_checkpoint.get(
                            "camera_id")
                        latitude = towards_woodland_checkpoint.get("latitude")
                        longitude = towards_woodland_checkpoint.get(
                            "longitude")
                        image_link = towards_woodland_checkpoint.get(
                            "image_link")

                        towards_woodland_checkpoint_image_url = image_link
                    case "Tuas Checkpoint":
                        tuas_checkpoint = result.get(
                            "tuas_checkpoint")

                        camera_id = tuas_checkpoint.get("camera_id")
                        latitude = tuas_checkpoint.get("latitude")
                        longitude = tuas_checkpoint.get("longitude")
                        image_link = tuas_checkpoint.get("image_link")

                        tuas_checkpoint_image_url = image_link
                    case "Malaysia CIQ 1":
                        malaysia_ciq_1 = result.get(
                            "malaysia_ciq_1")

                        camera_id = malaysia_ciq_1.get("camera_id")
                        latitude = malaysia_ciq_1.get("latitude")
                        longitude = malaysia_ciq_1.get("longitude")
                        image_link = malaysia_ciq_1.get("image_link")

                        malaysia_ciq_1_image_url = image_link
                    case "Malaysia CIQ 2":
                        malaysia_ciq_2 = result.get(
                            "malaysia_ciq_2")

                        camera_id = malaysia_ciq_2.get("camera_id")
                        latitude = malaysia_ciq_2.get("latitude")
                        longitude = malaysia_ciq_2.get("longitude")
                        image_link = malaysia_ciq_2.get("image_link")

                        malaysia_ciq_2_image_url = image_link
                    case "Malaysia Second link 1":
                        malaysia_second_link_01 = result.get(
                            "malaysia_second_link_01")

                        camera_id = malaysia_second_link_01.get("camera_id")
                        latitude = malaysia_second_link_01.get("latitude")
                        longitude = malaysia_second_link_01.get("longitude")
                        image_link = malaysia_second_link_01.get("image_link")

                        malaysia_second_link_01_image_url = image_link
                    case "Malaysia Second link 2":
                        malaysia_second_link_02 = result.get(
                            "malaysia_second_link_02")

                        camera_id = malaysia_second_link_02.get("camera_id")
                        latitude = malaysia_second_link_02.get("latitude")
                        longitude = malaysia_second_link_02.get("longitude")
                        image_link = malaysia_second_link_02.get("image_link")

                        malaysia_second_link_02_image_url = image_link
                    case "Malaysia Second link 3":
                        malaysia_second_link_03 = result.get(
                            "malaysia_second_link_03")

                        camera_id = malaysia_second_link_03.get("camera_id")
                        latitude = malaysia_second_link_03.get("latitude")
                        longitude = malaysia_second_link_03.get("longitude")
                        image_link = malaysia_second_link_03.get("image_link")

                        malaysia_second_link_03_image_url = image_link
                    case "Malaysia Second link 4":
                        malaysia_second_link_04 = result.get(
                            "malaysia_second_link_04")

                        camera_id = malaysia_second_link_04.get("camera_id")
                        latitude = malaysia_second_link_04.get("latitude")
                        longitude = malaysia_second_link_04.get("longitude")
                        image_link = malaysia_second_link_04.get("image_link")

                        malaysia_second_link_04_image_url = image_link
                    case "Malaysia Second link 5":
                        malaysia_second_link_05 = result.get(
                            "malaysia_second_link_05")

                        camera_id = malaysia_second_link_05.get("camera_id")
                        latitude = malaysia_second_link_05.get("latitude")
                        longitude = malaysia_second_link_05.get("longitude")
                        image_link = malaysia_second_link_05.get("image_link")

                        malaysia_second_link_05_image_url = image_link
                    case "Malaysia Second link 6":
                        malaysia_second_link_06 = result.get(
                            "malaysia_second_link_06")

                        camera_id = malaysia_second_link_06.get("camera_id")
                        latitude = malaysia_second_link_06.get("latitude")
                        longitude = malaysia_second_link_06.get("longitude")
                        image_link = malaysia_second_link_06.get("image_link")

                        malaysia_second_link_06_image_url = image_link
                    case "Malaysia Second link 7":
                        malaysia_second_link_07 = result.get(
                            "malaysia_second_link_07")

                        camera_id = malaysia_second_link_07.get("camera_id")
                        latitude = malaysia_second_link_07.get("latitude")
                        longitude = malaysia_second_link_07.get("longitude")
                        image_link = malaysia_second_link_07.get("image_link")

                        malaysia_second_link_07_image_url = image_link
                    case "Malaysia Second link 9":
                        malaysia_second_link_09 = result.get(
                            "malaysia_second_link_09")

                        camera_id = malaysia_second_link_09.get("camera_id")
                        latitude = malaysia_second_link_09.get("latitude")
                        longitude = malaysia_second_link_09.get("longitude")
                        image_link = malaysia_second_link_09.get("image_link")

                        malaysia_second_link_09_image_url = image_link
                    case "Malaysia Second link 10":
                        malaysia_second_link_10 = result.get(
                            "malaysia_second_link_10")

                        camera_id = malaysia_second_link_10.get("camera_id")
                        latitude = malaysia_second_link_10.get("latitude")
                        longitude = malaysia_second_link_10.get("longitude")
                        image_link = malaysia_second_link_10.get("image_link")

                        malaysia_second_link_10_image_url = image_link

                st.write(
                    f"**Camera Id**: {camera_id}, **Latitude**: {latitude}, **Longitude**: {longitude}"
                )
                st.link_button("Open image in new tab", image_link)
                image_str = get_image(image_link)
                st.image(image_str, caption=selected_image)

                with st.spinner('Loading detections...'):
                    time.sleep(2)

                    selected_image_text = get_selected_image_text(
                        selected_image)

                    detections_response = detections_api(
                        selected_image_text,
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
                    )
                    if detections_response:
                        result = detections_response["result"]

                        to_johor_data_list = result["to_johor_data_list"]
                        to_singapore_data_list = result["to_singapore_data_list"]
                        no_direction_total_data_list = result["no_direction_total_data_list"]
                        to_johor_number_of_vehicles = result["to_johor_number_of_vehicles"]
                        to_singapore_number_of_vehicles = result["to_singapore_number_of_vehicles"]
                        no_direction_total_number_of_vehicles = result[
                            "no_direction_total_number_of_vehicles"]

                        st.write(
                            f"**To Johor Number of Vehicles**: {to_johor_number_of_vehicles}"
                        )
                        st.write(
                            f"**To Singapore Number of Vehicles**: {to_singapore_number_of_vehicles}"
                        )
                        st.write(
                            f"**No Direction Total Number of Vehicles**: {no_direction_total_number_of_vehicles}"
                        )

                        st.write("**To Johor data list**")
                        st.json(to_johor_data_list, expanded=2)

                        st.write("**To Singapore data list**")
                        st.json(to_singapore_data_list, expanded=2)

                        st.write("**No Direction total data list**")
                        st.json(no_direction_total_data_list, expanded=2)
