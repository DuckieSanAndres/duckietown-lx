import numpy as np
from typing import Tuple

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    """
    Define a weight matrix for the left motor.
    High positive values in the right part of the image will make the left motor respond more to those areas.
    """
    res = np.zeros(shape=shape, dtype="float32")
    res[:, :shape[1]//2] = 1
    res[:, shape[1]//2:] = -1

    return res

def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    """
    Define a weight matrix for the right motor.
    High negative values in the left part of the image will make the right motor respond to those areas.
    """
    res = np.zeros(shape=shape, dtype="float32")

    res[:, shape[1]//2:] = 1  # Right half of the image
    res[:, :shape[1]//2] = -1

    return res

