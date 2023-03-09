import numpy as np
from PIL import Image, ImageTk
import chladni_image
import chladni_anim
import PySimpleGUI as sg

import chladni_loop

chladni_left_bound = -0.5
chladni_right_bound = 0.5
chladni_down_bound = -0.5
chladni_up_bound = 0.5
image_width = 300
image_height = 300
image_data = np.empty((image_width, image_height, 3))
x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

error_margin = 0.1

a = 3.2
b = -1
n = 7.6
m = -1.4

chladni_loop.start()

# p = chladni_image.get_image(image_width, image_height, 0.5, 2, 1, 1, 1, 0.1)

# chladni_anim.get_gif_varying_a(image_width, image_height, 0.5, a0=1, an=10, b=1, n=1, m=1, error_margin=error_margin)
# chladni_anim.get_gif_varying_n(image_width, image_height, 0.5, a=1, b=-1, n0=-10, n=10, m=2, error_margin=error_margin)
# chladni_anim.get_gif_varying_m(image_width, image_height, 0.5, a=4, b=-1.5, n=7, m0=-4, mn=4, error_margin=error_margin)
# chladni_anim.get_gif_varying_b(image_width, image_height, 0.5, a=1, b0=-2, bn=2, n=7, m=2, error_margin=error_margin)
# chladni_anim.get_gif_varying_a_n(image_width, image_height, 0.5, 1, 10, b, 7, 2, m, error_margin)
# chladni_anim.get_gif_varying_a_b(image_width, image_height, 0.5, a0=-5.7, an=5.7, b0=-2, bn=2, n=7.6, m=-1.4, error_margin=error_margin)

# num_z = 0
#
# chladni_values = np.empty((image_width, image_height, 3))
#
# def chladni_equation(a, b, n, m, x, y):
#     pi = np.pi
#     a_term = np.sin(pi * n * x) * np.sin(pi * m * y)
#     b_term = np.sin(pi * m * x) * np.sin(pi * n * y)
#     eq_value = (a * a_term) + (b + b_term)
#     return eq_value
#
#
# for idx_x in range(image_width):
#     for idx_y in range(image_height):
#         x = chladni_left_bound + (idx_x * x_ratio)
#         y = chladni_up_bound - (idx_y * y_ratio)
#         chladni_value = chladni_equation(a, b, n, m, x, y)
#         chladni_values[idx_x][idx_y][0] = abs(chladni_value)
#         chladni_values[idx_x][idx_y][1] = abs(chladni_value)
#         chladni_values[idx_x][idx_y][2] = abs(chladni_value)
#         if (chladni_value >= 0-error_margin) and (chladni_value <= 0+error_margin):
#             image_data[idx_x][idx_y] = [255, 255, 255]
#             num_z += 1
#         else:
#             image_data[idx_x][idx_y] = [0, 0, 0]
#
#
# max_value = chladni_values.max()
# r = 255 / max_value
# chladni_values *= r
#
# chladni_values_image = Image.fromarray(chladni_values.astype(np.uint8))
# chladni_values_image.show()
# print(num_z)
#
# chladni_patterns = Image.fromarray(image_data.astype(np.uint8))
# chladni_patterns.show()
