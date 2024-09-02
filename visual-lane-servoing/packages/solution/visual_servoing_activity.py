from typing import Tuple

import numpy as np
import cv2


def get_steer_matrix_left_lane_markings(shape: Tuple[int, int]) -> np.ndarray:

    # TODO: write your function instead of this one
    steer_matrix_left = np.zeros(shape)
    steer_matrix_left[230:, 100:250] = -1

    return steer_matrix_left


def get_steer_matrix_right_lane_markings(shape: Tuple[int, int]) -> np.ndarray:

 # TODO: write your function instead of this one
    steer_matrix_right = np.zeros(shape)
    steer_matrix_right[220:, 400:680] = 1

    return steer_matrix_right


def detect_lane_markings(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    imgbgr = image
    img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2HSV)
    imgg = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)

    mask_ground = np.ones(imgg.shape, dtype=np.uint8)
    mask_ground[0:180, ::] = 0

    white_lower_hsv = np.array([0, 0, 150])
    white_upper_hsv = np.array([180, 50, 255])
    yellow_lower_hsv = np.array([20, 45, 150])
    yellow_upper_hsv = np.array([40, 255, 255])


    mask_white = cv2.inRange(img, white_lower_hsv, white_upper_hsv)
    mask_yellow = cv2.inRange(img, yellow_lower_hsv, yellow_upper_hsv)

    mask_left_edge = mask_ground * mask_yellow
    mask_right_edge = mask_ground * mask_white


    return mask_left_edge, mask_right_edge
