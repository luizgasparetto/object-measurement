import cv2
import numpy as np

from scripts.object_detector import *
from urllib.request import urlopen
from scripts.models.Object import *

def measure_object(image_url):
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

    detector = HomogeneousBgDetector()

    url = image_url
    url_response = urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    corners, _, __ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

    aruco_perimeter = cv2.arcLength(corners[0], True)

    pixel_cm_ratio = aruco_perimeter / 40

    contours = detector.detect_objects(img)

    objects_width = []
    objects_height = []

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        obj_width = w / pixel_cm_ratio
        obj_height = h / pixel_cm_ratio

        objects_width.append(round(obj_width, 1))
        objects_height.append(round(obj_height, 1))

    object_measured = Object(objects_width[1], objects_height[1])

    cv2.waitKey(0)
    return object_measured
