import time
import streamlit as st
from services.traffic_images_api import traffic_images_api
from services.detections_api import detections_api


def get_selected_image_text(selected_image):
    selected_image_text = ""

    match selected_image:
        case "Woodland johor bridge":
            selected_image_text = "woodland_johor_bridge_image"
        case "Tuas second link":
            selected_image_text = "tuas_second_link_image"
        case "Woodland checkpoint":
            selected_image_text = "woodland_checkpoint_image"
        case "Towards woodland checkpoint":
            selected_image_text = "towards_woodland_checkpoint_image"
        case "Tuas checkpoint":
            selected_image_text = "tuas_checkpoint_image"

    return selected_image_text


st.title("Jam or not")

st.write("")

selected_image = st.selectbox(
    label="Select image",
    placeholder="Select image",
    options=[
        "Woodland johor bridge",
        "Tuas second link",
        "Woodland checkpoint",
        "Towards woodland checkpoint",
        "Tuas checkpoint"
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

                match selected_image:
                    case "Woodland johor bridge":
                        woodland_johor_bridge = result.get(
                            "woodland_johor_bridge")

                        camera_id = woodland_johor_bridge.get("camera_id")
                        latitude = woodland_johor_bridge.get("latitude")
                        longitude = woodland_johor_bridge.get("longitude")
                        image_link = woodland_johor_bridge.get("image_link")

                        woodland_johor_bridge_image_url = image_link
                    case "Tuas second link":
                        tuas_second_link = result.get(
                            "tuas_second_link")

                        camera_id = tuas_second_link.get("camera_id")
                        latitude = tuas_second_link.get("latitude")
                        longitude = tuas_second_link.get("longitude")
                        image_link = tuas_second_link.get("image_link")

                        tuas_second_link_image_url = image_link
                    case "Woodland checkpoint":
                        woodland_checkpoint = result.get(
                            "woodland_checkpoint")

                        camera_id = woodland_checkpoint.get("camera_id")
                        latitude = woodland_checkpoint.get("latitude")
                        longitude = woodland_checkpoint.get("longitude")
                        image_link = woodland_checkpoint.get("image_link")

                        woodland_checkpoint_image_url = image_link
                    case "Towards woodland checkpoint":
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
                    case "Tuas checkpoint":
                        tuas_checkpoint = result.get(
                            "tuas_checkpoint")

                        camera_id = tuas_checkpoint.get("camera_id")
                        latitude = tuas_checkpoint.get("latitude")
                        longitude = tuas_checkpoint.get("longitude")
                        image_link = tuas_checkpoint.get("image_link")

                        tuas_checkpoint_image_url = image_link

                st.write(
                    f"Camera Id: **{camera_id}**, Latitude: **{latitude}**, Longitude: **{longitude}**"
                )
                st.image(image_link, caption=selected_image)

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
                        tuas_checkpoint_image_url
                    )
                    if detections_response:
                        result = detections_response["result"]

                        to_johor_data_list = result["to_johor_data_list"]
                        to_singapore_data_list = result["to_singapore_data_list"]
                        to_johor_number_of_vehicles = result["to_johor_number_of_vehicles"]
                        to_singapore_number_of_vehicles = result["to_singapore_number_of_vehicles"]

                        st.write(
                            f"To johor number of vehicles: {to_johor_number_of_vehicles}"
                        )
                        st.write(
                            f"To singapore number of vehicles: {to_singapore_number_of_vehicles}"
                        )

                        st.write("To Johor")
                        st.json(to_johor_data_list, expanded=2)

                        st.write("To Singapore")
                        st.json(to_singapore_data_list, expanded=2)
