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

    save_image_in_local(
        woodland_johor_bridge_image_url,
        tuas_second_link_image_url,
        woodland_checkpoint_image_url,
        towards_woodland_checkpoint_image_url,
        tuas_checkpoint_image_url
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

    print(f"target_image = {target_image}")

    to_johor_data_list, to_singapore_data_list = get_detections(
        target_image, selected_image)

    return selected_image, to_johor_data_list, to_singapore_data_list


def save_image_in_local(
    woodland_johor_bridge_image_url,
    tuas_second_link_image_url,
    woodland_checkpoint_image_url,
    towards_woodland_checkpoint_image_url,
    tuas_checkpoint_image_url
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
                [20, 972],
                [55, 1006],
                [1775, 275],
                [1800, 295]
            ])

            to_singapore_polygon = np.array([
                [570, 955],
                [792, 994],
                [1802, 351],
                [1887, 367]
            ])
        case "tuas_second_link_image":
            to_johor_polygon = np.array([
                [820, 445],
                [1073, 424],
                [133, 98],
                [313, 73]
            ])

            to_singapore_polygon = np.array([
                [339, 66],
                [502, 52],
                [1364, 420],
                [1629, 399]
            ])
        case "woodland_checkpoint_image":
            to_johor_polygon = np.array([
                [825, 645],
                [967, 665],
                [1206, 1053],
                [1427, 1048]
            ])

            to_singapore_polygon = np.array([
                [333, 1056],
                [522, 1051],
                [330, 307],
                [411, 317]
            ])
        case "towards_woodland_checkpoint_image":
            to_johor_polygon = np.array([
                [1075, 216],
                [1232, 223],
                [1059, 1034],
                [1859, 1017]
            ])

            to_singapore_polygon = np.array([
                [1343, 249],
                [1552, 289],
                [1797, 622],
                [1906, 572]
            ])
        case "tuas_checkpoint_image":
            to_johor_polygon = np.array([
                [1150, 429],
                [1370, 435],
                [1338, 630],
                [1705, 591]
            ])

            to_singapore_polygon = np.array([
                [30, 683],
                [455, 698],
                [602, 418],
                [732, 446]
            ])

    to_johor_data_list = filter_by_polygon_zone_and_class_id(
        to_johor_polygon,
        detections,
        image
    )

    to_singapore_data_list = filter_by_polygon_zone_and_class_id(
        to_singapore_polygon,
        detections,
        image
    )

    return to_johor_data_list, to_singapore_data_list


def filter_by_polygon_zone_and_class_id(polygon, detections, image):
    data_list = []

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


def callback(image_slice: np.ndarray) -> sv.Detections:
    model = get_model(model_id="yolov8x-640")

    results = model.infer(image_slice)[0]
    return sv.Detections.from_inference(results)


def annotate_image(image, detections):
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = box_annotator.annotate(
        scene=image.copy(), detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)

    sv.plot_image(annotated_image)
