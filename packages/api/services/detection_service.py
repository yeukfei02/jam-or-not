import os
import glob
import json
import requests
import cv2
import supervision as sv
from inference import get_model
import numpy as np


def supervision_detection(body):
    woodland_johor_bridge_image_url = body.get(
        "woodland_johor_bridge_image_url")
    tuas_second_link_image_url = body.get(
        "tuas_second_link_image_url")
    woodland_checkpoint_image_url = body.get(
        "woodland_checkpoint_image_url")
    towards_woodland_checkpoint_image_url = body.get(
        "towards_woodland_checkpoint_image_url"
    )
    tuas_checkpoint_image_url = body.get("tuas_checkpoint_image_url")
    malaysia_ciq_1_image_url = body.get("malaysia_ciq_1_image_url")
    malaysia_ciq_2_image_url = body.get("malaysia_ciq_2_image_url")
    malaysia_second_link_01_image_url = body.get(
        "malaysia_second_link_01_image_url")
    malaysia_second_link_02_image_url = body.get(
        "malaysia_second_link_02_image_url")
    malaysia_second_link_03_image_url = body.get(
        "malaysia_second_link_03_image_url")
    malaysia_second_link_04_image_url = body.get(
        "malaysia_second_link_04_image_url")
    malaysia_second_link_05_image_url = body.get(
        "malaysia_second_link_05_image_url")
    malaysia_second_link_06_image_url = body.get(
        "malaysia_second_link_06_image_url")
    malaysia_second_link_07_image_url = body.get(
        "malaysia_second_link_07_image_url")
    malaysia_second_link_09_image_url = body.get(
        "malaysia_second_link_09_image_url")
    malaysia_second_link_10_image_url = body.get(
        "malaysia_second_link_10_image_url")

    save_image_in_local(
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

    target_image = None

    selected_image = body.get("selected_image")
    if selected_image:
        match selected_image:
            case "woodland_johor_bridge_image":
                woodland_johor_bridge_image = f"{os.getcwd()}/images/woodland_johor_bridge_image.jpg"
                target_image = woodland_johor_bridge_image
            case "tuas_second_link_image":
                tuas_second_link_image = f"{os.getcwd()}/images/tuas_second_link_image.jpg"
                target_image = tuas_second_link_image
            case "woodland_checkpoint_image":
                woodland_checkpoint_image = f"{os.getcwd()}/images/woodland_checkpoint_image.jpg"
                target_image = woodland_checkpoint_image
            case "towards_woodland_checkpoint_image":
                towards_woodland_checkpoint_image = f"{os.getcwd()}/images/towards_woodland_checkpoint_image.jpg"
                target_image = towards_woodland_checkpoint_image
            case "tuas_checkpoint_image":
                tuas_checkpoint_image = f"{os.getcwd()}/images/tuas_checkpoint_image.jpg"
                target_image = tuas_checkpoint_image
            case "malaysia_ciq_1_image":
                malaysia_ciq_1_image = f"{os.getcwd()}/images/malaysia_ciq_1_image.jpg"
                target_image = malaysia_ciq_1_image
            case "malaysia_ciq_2_image":
                malaysia_ciq_2_image = f"{os.getcwd()}/images/malaysia_ciq_2_image.jpg"
                target_image = malaysia_ciq_2_image
            case "malaysia_second_link_01_image":
                malaysia_second_link_01_image = f"{os.getcwd()}/images/malaysia_second_link_01_image.jpg"
                target_image = malaysia_second_link_01_image
            case "malaysia_second_link_02_image":
                malaysia_second_link_02_image = f"{os.getcwd()}/images/malaysia_second_link_02_image.jpg"
                target_image = malaysia_second_link_02_image
            case "malaysia_second_link_03_image":
                malaysia_second_link_03_image = f"{os.getcwd()}/images/malaysia_second_link_03_image.jpg"
                target_image = malaysia_second_link_03_image
            case "malaysia_second_link_04_image":
                malaysia_second_link_04_image = f"{os.getcwd()}/images/malaysia_second_link_04_image.jpg"
                target_image = malaysia_second_link_04_image
            case "malaysia_second_link_05_image":
                malaysia_second_link_05_image = f"{os.getcwd()}/images/malaysia_second_link_05_image.jpg"
                target_image = malaysia_second_link_05_image
            case "malaysia_second_link_06_image":
                malaysia_second_link_06_image = f"{os.getcwd()}/images/malaysia_second_link_06_image.jpg"
                target_image = malaysia_second_link_06_image
            case "malaysia_second_link_07_image":
                malaysia_second_link_07_image = f"{os.getcwd()}/images/malaysia_second_link_07_image.jpg"
                target_image = malaysia_second_link_07_image
            case "malaysia_second_link_09_image":
                malaysia_second_link_09_image = f"{os.getcwd()}/images/malaysia_second_link_09_image.jpg"
                target_image = malaysia_second_link_09_image
            case "malaysia_second_link_10_image":
                malaysia_second_link_10_image = f"{os.getcwd()}/images/malaysia_second_link_10_image.jpg"
                target_image = malaysia_second_link_10_image

    print(f"target_image = {target_image}")

    to_johor_data_list, to_singapore_data_list = get_detections(
        target_image, selected_image)

    return selected_image, to_johor_data_list, to_singapore_data_list


def save_image_in_local(
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
    images_folder_path = f"{os.getcwd()}/images"

    # remove all image files in images folder
    files = glob.glob(f"{images_folder_path}/*")
    for f in files:
        os.remove(f)

    # create images folder
    if not os.path.exists(images_folder_path):
        os.makedirs(images_folder_path)

    # create woodland_johor_bridge image
    if woodland_johor_bridge_image_url:
        woodland_johor_bridge_page = requests.get(
            woodland_johor_bridge_image_url)

        woodland_johor_bridge_image_path = f"{images_folder_path}/woodland_johor_bridge_image.jpg"
        with open(woodland_johor_bridge_image_path, 'wb') as f:
            f.write(woodland_johor_bridge_page.content)

    # create tuas_second_link image
    if tuas_second_link_image_url:
        tuas_second_link_page = requests.get(
            tuas_second_link_image_url)

        tuas_second_link_image_path = f"{images_folder_path}/tuas_second_link_image.jpg"
        with open(tuas_second_link_image_path, 'wb') as f:
            f.write(tuas_second_link_page.content)

    # create woodland_checkpoint image
    if woodland_checkpoint_image_url:
        woodland_checkpoint_image_page = requests.get(
            woodland_checkpoint_image_url)

        woodland_checkpoint_image_path = f"{images_folder_path}/woodland_checkpoint_image.jpg"
        with open(woodland_checkpoint_image_path, 'wb') as f:
            f.write(woodland_checkpoint_image_page.content)

    # create towards woodland_checkpoint image
    if towards_woodland_checkpoint_image_url:
        towards_woodland_checkpoint_image_page = requests.get(
            towards_woodland_checkpoint_image_url)

        towards_woodland_checkpoint_image_path = f"{images_folder_path}/towards_woodland_checkpoint_image.jpg"
        with open(towards_woodland_checkpoint_image_path, 'wb') as f:
            f.write(towards_woodland_checkpoint_image_page.content)

    # create tuas_checkpoint image
    if tuas_checkpoint_image_url:
        tuas_checkpoint_image_page = requests.get(tuas_checkpoint_image_url)

        tuas_checkpoint_image_path = f"{images_folder_path}/tuas_checkpoint_image.jpg"
        with open(tuas_checkpoint_image_path, 'wb') as f:
            f.write(tuas_checkpoint_image_page.content)

    # create malaysia_ciq_1 image
    if malaysia_ciq_1_image_url:
        malaysia_ciq_1_image_page = requests.get(malaysia_ciq_1_image_url)

        malaysia_ciq_1_image_path = f"{images_folder_path}/malaysia_ciq_1_image.jpg"
        with open(malaysia_ciq_1_image_path, 'wb') as f:
            f.write(malaysia_ciq_1_image_page.content)

    # create malaysia_ciq_2 image
    if malaysia_ciq_2_image_url:
        malaysia_ciq_2_image_page = requests.get(malaysia_ciq_2_image_url)

        malaysia_ciq_2_image_path = f"{images_folder_path}/malaysia_ciq_2_image.jpg"
        with open(malaysia_ciq_2_image_path, 'wb') as f:
            f.write(malaysia_ciq_2_image_page.content)

    # create malaysia_second_link_01 image
    if malaysia_second_link_01_image_url:
        malaysia_second_link_01_image_page = requests.get(
            malaysia_second_link_01_image_url)

        malaysia_second_link_01_image_path = f"{images_folder_path}/malaysia_second_link_01_image.jpg"
        with open(malaysia_second_link_01_image_path, 'wb') as f:
            f.write(malaysia_second_link_01_image_page.content)

    # create malaysia_second_link_02 image
    if malaysia_second_link_02_image_url:
        malaysia_second_link_02_image_page = requests.get(
            malaysia_second_link_02_image_url)

        malaysia_second_link_02_image_path = f"{images_folder_path}/malaysia_second_link_02_image.jpg"
        with open(malaysia_second_link_02_image_path, 'wb') as f:
            f.write(malaysia_second_link_02_image_page.content)

    # create malaysia_second_link_03 image
    if malaysia_second_link_03_image_url:
        malaysia_second_link_03_image_page = requests.get(
            malaysia_second_link_03_image_url)

        malaysia_second_link_03_image_path = f"{images_folder_path}/malaysia_second_link_03_image.jpg"
        with open(malaysia_second_link_03_image_path, 'wb') as f:
            f.write(malaysia_second_link_03_image_page.content)

    # create malaysia_second_link_04 image
    if malaysia_second_link_04_image_url:
        malaysia_second_link_04_image_page = requests.get(
            malaysia_second_link_04_image_url)

        malaysia_second_link_04_image_path = f"{images_folder_path}/malaysia_second_link_04_image.jpg"
        with open(malaysia_second_link_04_image_path, 'wb') as f:
            f.write(malaysia_second_link_04_image_page.content)

    # create malaysia_second_link_05 image
    if malaysia_second_link_05_image_url:
        malaysia_second_link_05_image_page = requests.get(
            malaysia_second_link_05_image_url)

        malaysia_second_link_05_image_path = f"{images_folder_path}/malaysia_second_link_05_image.jpg"
        with open(malaysia_second_link_05_image_path, 'wb') as f:
            f.write(malaysia_second_link_05_image_page.content)

    # create malaysia_second_link_06 image
    if malaysia_second_link_06_image_url:
        malaysia_second_link_06_image_page = requests.get(
            malaysia_second_link_06_image_url)

        malaysia_second_link_06_image_path = f"{images_folder_path}/malaysia_second_link_06_image.jpg"
        with open(malaysia_second_link_06_image_path, 'wb') as f:
            f.write(malaysia_second_link_06_image_page.content)

    # create malaysia_second_link_07 image
    if malaysia_second_link_07_image_url:
        malaysia_second_link_07_image_page = requests.get(
            malaysia_second_link_07_image_url)

        malaysia_second_link_07_image_path = f"{images_folder_path}/malaysia_second_link_07_image.jpg"
        with open(malaysia_second_link_07_image_path, 'wb') as f:
            f.write(malaysia_second_link_07_image_page.content)

    # create malaysia_second_link_09 image
    if malaysia_second_link_09_image_url:
        malaysia_second_link_09_image_page = requests.get(
            malaysia_second_link_09_image_url)

        malaysia_second_link_09_image_path = f"{images_folder_path}/malaysia_second_link_09_image.jpg"
        with open(malaysia_second_link_09_image_path, 'wb') as f:
            f.write(malaysia_second_link_09_image_page.content)

    # create malaysia_second_link_10 image
    if malaysia_second_link_10_image_url:
        malaysia_second_link_10_image_page = requests.get(
            malaysia_second_link_10_image_url)

        malaysia_second_link_10_image_path = f"{images_folder_path}/malaysia_second_link_10_image.jpg"
        with open(malaysia_second_link_10_image_path, 'wb') as f:
            f.write(malaysia_second_link_10_image_page.content)


def get_detections(target_image, selected_image):
    image = cv2.imread(target_image)
    print(f"image = {image}")

    slicer = sv.InferenceSlicer(callback=callback)

    detections = slicer(image)

    print(f"detections = {detections}")

    to_johor_polygon = np.array([])

    to_singapore_polygon = np.array([])

    match selected_image:
        case "woodland_johor_bridge_image":
            to_johor_polygon = np.array([
                [563, 836],
                [661, 872],
                [1830, 258],
                [1885, 271]
            ])

            to_singapore_polygon = np.array([
                [559, 934],
                [701, 982],
                [1840, 320],
                [1909, 351]
            ])
        case "tuas_second_link_image":
            to_johor_polygon = np.array([
                [132, 97],
                [286, 95],
                [639, 684],
                [1612, 659]
            ])

            to_singapore_polygon = np.array([
                [362, 77],
                [651, 47],
                [1724, 538],
                [1914, 373]
            ])
        case "woodland_checkpoint_image":
            to_johor_polygon = np.array([
                [1911, 1053],
                [537, 80],
                [1190, 1068],
                [1818, 986]
            ])

            to_singapore_polygon = np.array([
                [318, 1059],
                [1087, 1052],
                [782, 645],
                [416, 87]
            ])
        case "towards_woodland_checkpoint_image":
            to_johor_polygon = np.array([
                [1065, 185],
                [1210, 183],
                [1025, 1012],
                [1879, 1007]
            ])

            to_singapore_polygon = np.array([
                [1329, 229],
                [1456, 235],
                [1792, 623],
                [1906, 546]
            ])
        case "tuas_checkpoint_image":
            to_johor_polygon = np.array([
                [1425, 132],
                [1605, 138],
                [1629, 676],
                [1800, 613]
            ])

            to_singapore_polygon = np.array([
                [10, 697],
                [97, 821],
                [608, 387],
                [717, 477]
            ])

    is_malaysia_image = False

    malaysia_images = [
        "malaysia_ciq_1_image",
        "malaysia_ciq_2_image",
        "malaysia_second_link_01_image",
        "malaysia_second_link_02_image",
        "malaysia_second_link_03_image",
        "malaysia_second_link_04_image",
        "malaysia_second_link_05_image",
        "malaysia_second_link_06_image",
        "malaysia_second_link_07_image",
        "malaysia_second_link_09_image",
        "malaysia_second_link_10_image"
    ]
    for malaysia_image in malaysia_images:
        if selected_image == malaysia_image:
            is_malaysia_image = True

    to_johor_data_list = []
    to_singapore_data_list = []

    if not is_malaysia_image:
        to_johor_data_list = filter_by_polygon_zone_and_class_id(
            to_johor_polygon,
            detections,
            is_malaysia_image
        )

    to_singapore_data_list = filter_by_polygon_zone_and_class_id(
        to_singapore_polygon,
        detections,
        is_malaysia_image
    )

    return to_johor_data_list, to_singapore_data_list


def callback(image_slice: np.ndarray) -> sv.Detections:
    model = get_model(model_id="yolov8x-640")

    results = model.infer(image_slice)[0]

    return sv.Detections.from_inference(results)


def filter_by_polygon_zone_and_class_id(polygon, detections, is_malaysia_image):
    data_list = []

    if not is_malaysia_image:
        zone = sv.PolygonZone(polygon=polygon)

        mask = zone.trigger(detections=detections)

        # filter detections by polygon zone
        detections = detections[mask]

    # only select classes are car, motorcycle, bus, truck
    selected_classes = [2, 3, 5, 7]

    # filter detections by selected classes
    detections = detections[np.isin(detections.class_id, selected_classes)]

    for xyxy, mask, confidence, class_id, tracker_id, data in detections:
        class_name = data["class_name"]

        print(f"xyxy = {xyxy}")
        print(f"mask = {mask}")
        print(f"confidence = {confidence}")
        print(f"class_id = {class_id}")
        print(f"tracker_id = {tracker_id}")
        print(f"class_name = {class_name}")

        print(f"xyxy type = {type(xyxy)}")
        print(f"mask type = {type(mask)}")
        print(f"confidence type = {type(confidence)}")
        print(f"class_id type = {type(class_id)}")
        print(f"tracker_id type = {type(tracker_id)}")
        print(f"class_name type = {type(class_name)}")

        data = {
            "xyxy": json.dumps(xyxy, default=str),
            "mask": mask.item() if mask else "",
            "confidence": np.float64(confidence).item(),
            "class_id": np.int64(class_id).item(),
            "tracker_id": tracker_id.item() if tracker_id else "",
            "class_name": class_name
        }
        data_list.append(data)

    # uncomment this when in local development
    # annotate_image(image, detections)

    return data_list


def annotate_image(image, detections):
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = box_annotator.annotate(
        scene=image.copy(), detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)

    sv.plot_image(annotated_image)
