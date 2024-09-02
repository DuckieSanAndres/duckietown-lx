from typing import Tuple

import numpy as np
import yaml
import os

def PIDController(
    v_0: float, y_ref: float, y_hat: float, prev_e_y: float, prev_int_y: float, delta_t: float #, theta_hat: float , prev_e: float
) -> Tuple[float, float, float, float]:
    """
    PID performing lateral control.

    Args:
        v_0:        linear Duckiebot speed (constant).
        y_ref:      target y coordinate.
        y_hat:      the current estimated y.
        prev_e_y:   tracking error at previous iteration.
        prev_int_y: previous integral error term.
        delta_t:    time interval since last call.

    Returns:
        v_0:        linear velocity of the Duckiebot
        omega:      angular velocity of the Duckiebot
        e:          current tracking error (automatically becomes prev_e_y at next iteration).
        e_int:      current integral error (automatically becomes prev_int_y at next iteration).
    """

    # Read PID gains from file
    #script_dir = os.path.dirname(__file__)
    #file_path = script_dir + "/GAINS.yaml"

    #with open(file_path) as f:
        #gains = yaml.full_load(f)
        #f.close()

    Kp = 5
    Ki = 5
    Kd = 1

    e_dist = y_ref-y_hat

    e_int_dist = prev_e_y + e_dist * delta_t

    delta_et_dist = (e_dist - e_int_dist) / delta_t


    # PID controller for omega
    omega = Kp*e_dist + Ki*e_int_dist + Kd*delta_et_dist



    return v_0, omega, e_dist, e_int_dist
