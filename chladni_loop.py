import numpy as np
from PIL import Image, ImageTk
import PySimpleGUI as sg
import random as rand
from numba import njit, prange, jit
import time


def start():
    boundary_value = 0.5
    image_height = 405  # 720 , 405
    image_width = 720  # 1280 , 720
    error_margin = 0.05

    # CODE TO FIND HEIGHT AND WIDTH
    # h1 = 1080
    # w1 = 1920
    # r = w1 / h1
    # h2 = 400
    # w2 = 0.1
    # while not w2.is_integer():
    #     h2 += 1
    #     w2 = r * h2
    # print(w2, h2)

    a = 1
    b = -1
    n = 7
    m = 2

    sg.theme('DarkGreen3')

    layout = [
        [sg.Image('', size=(1920, 1080), key='-IMAGE-')],  # (1920, 1080)
    ]
    window = sg.Window(title="chladni patterns", layout=layout, margins=(0, 0), finalize=True, no_titlebar=True)
    window.bind("<Escape>", "-ESCAPE-")

    vals = [a, b, n, m]

    window.TKroot['cursor'] = 'none'  # hide cursor
    window.bring_to_front()  # re-focus on window

    window.maximize()

    x, y = get_x_y_matrices(image_height, image_width, boundary_value)

    while True:
        event, values = window.read(timeout=10)
        if event in (sg.WIN_CLOSED, "-ESCAPE-"):
            window.close()
            break

        # slightly change values
        r = rand.randint(0, 2)
        vals[r] = round(vals[r] + (random_float(-1, 1, 0.2)), 1)

        # get new frame, update, find FPS
        start_time = time.time()

        chladni_img = get_frame(image_width, image_height, vals, error_margin, x, y)
        chladni_pattern = ImageTk.PhotoImage(image=chladni_img.resize(size=(1920, 1080), resample=Image.LANCZOS))
        window['-IMAGE-'].update(data=chladni_pattern)

        end_time = time.time()
        print("FPS:", 1 / (end_time - start_time))

    window.close()


@jit
def random_float(start, stop, step):
    values = np.arange(start, stop, step)
    return rand.choice(values)


@njit
def chladni_equation(a, b, n, m, x, y):
    # vals = [a, b, n, m]
    a_term = np.sin(np.pi * n * x) * np.sin(np.pi * m * y)
    b_term = np.sin(np.pi * m * x) * np.sin(np.pi * n * y)
    eq_value = (a * a_term) + (b + b_term)
    return eq_value


# returns x, y matrices with x and y values at correct index
@jit
def get_x_y_matrices(image_height, image_width, bound_value):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    x = np.zeros((image_height, image_width)) * 0.0
    y = np.zeros((image_height, image_width)) * 0.0
    # create x and y arrays
    for idx_x in prange(image_width):
        for idx_y in prange(image_height):
            x[idx_y][idx_x] = chladni_left_bound + (idx_x * x_ratio)
            y[idx_y][idx_x] = chladni_up_bound - (idx_y * y_ratio)
    return x, y


# def map_with_gradient(chladni_values, error_margin_arr):


@jit
def get_frame(image_width, image_height, vals, error_margin, x, y):

    # create chladni values
    pi_n = np.pi * vals[2]
    pi_m = np.pi * vals[3]
    a_term = np.multiply(np.sin(np.multiply(x, pi_n)), np.sin(np.multiply(y, pi_m)))
    b_term = np.multiply(np.sin(np.multiply(x, pi_m)), np.sin(np.multiply(y, pi_n)))
    chladni_values = np.multiply(vals[0], a_term) + np.multiply(vals[1], b_term)

    # check condition
    # TODO replace condition with a mapping function similar to a damping sinusoidal wave

    # TODO only calculate a quarter of the image, then duplicate and mirror on other quadrants

    # image_data = np.zeros((image_height, image_width, 3)) * 0.0
    # for idx_x in range(image_width):
    #     for idx_y in range(image_height):
    #         chladni_value = chladni_values[idx_y][idx_x]
    #         if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
    #             image_data[idx_y][idx_x] = [255, 255, 255]

    image_data = np.floor(np.multiply(255, np.exp(-1 * np.abs(np.multiply(1000 * error_margin, chladni_values)))))

    return Image.fromarray(image_data.astype(np.uint8))  # .resize(size=size, resample=Image.BICUBIC)
