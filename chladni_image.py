import numpy as np
from PIL import Image


def chladni_equation(a, b, n, m, x, y):
    pi = np.pi
    a_term = np.sin(pi * n * x) * np.sin(pi * m * y)
    b_term = np.sin(pi * m * x) * np.sin(pi * n * y)
    eq_value = (a * a_term) + (b + b_term)
    return eq_value


def get_image(image_width, image_height, bound_value, a, b, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    image_data = np.empty((image_width, image_height, 3))

    for idx_x in range(image_width):
        for idx_y in range(image_height):
            x = chladni_left_bound + (idx_x * x_ratio)
            y = chladni_up_bound - (idx_y * y_ratio)
            chladni_value = chladni_equation(a, b, n, m, x, y)
            if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                image_data[idx_x][idx_y] = [255, 255, 255]
            else:
                image_data[idx_x][idx_y] = [0, 0, 0]

    chladni_patterns = Image.fromarray(image_data.astype(np.uint8))
    chladni_patterns.show()

    return Image.fromarray(image_data.astype(np.uint8))
