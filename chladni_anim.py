import numpy as np
from PIL import Image
from moviepy.editor import ImageSequenceClip

def chladni_equation(a, b, n, m, x, y):
    pi = np.pi
    a_term = np.sin(pi * n * x) * np.sin(pi * m * y)
    b_term = np.sin(pi * m * x) * np.sin(pi * n * y)
    eq_value = (a * a_term) + (b + b_term)
    return eq_value


def get_gif_varying_a(image_width, image_height, bound_value, a0, an, b, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    fps = 10
    sec = 5

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    image_data = np.empty((image_width, image_height, 3))
    frames = []
    a_values = np.linspace(a0, an, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a_values[idx_mod], b, n, m, x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_a.gif', fps=fps)

def get_gif_varying_n(image_width, image_height, bound_value, a, b, n0, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    fps = 10
    sec = 5

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    image_data = np.empty((image_width, image_height, 3))
    frames = []
    n_values = np.linspace(n0, n, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a, b, n_values[idx_mod], m, x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_n.gif', fps=fps)

def get_gif_varying_m(image_width, image_height, bound_value, a, b, n, m0, mn, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    fps = 10
    sec = 5

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    image_data = np.empty((image_width, image_height, 3))
    frames = []
    m_values = np.linspace(m0, mn, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a, b, n, m_values[idx_mod], x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_m.gif', fps=fps)

def get_gif_varying_b(image_width, image_height, bound_value, a, b0, bn, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    fps = 5
    sec = 5

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    image_data = np.empty((image_width, image_height, 3))
    frames = []
    b_values = np.linspace(b0, bn, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a, b_values[idx_mod], n, m, x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_b.gif', fps=fps)

def get_gif_varying_a_n(image_width, image_height, bound_value, a0, an, b, n0, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    fps = 5
    sec = 3

    image_data = np.empty((image_width, image_height, 3))
    frames = []

    a_values = np.linspace(a0, an, fps*sec)
    n_values = np.linspace(n0, n, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a_values[idx_mod], b, n_values[idx_mod], m, x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_a_n.gif', fps=fps)

def get_gif_varying_a_b(image_width, image_height, bound_value, a0, an, b0, bn, n, m, error_margin):
    chladni_left_bound = -1 * bound_value
    chladni_right_bound = bound_value
    chladni_down_bound = -1 * bound_value
    chladni_up_bound = bound_value

    x_ratio = (chladni_right_bound - chladni_left_bound) / image_width
    y_ratio = (chladni_up_bound - chladni_down_bound) / image_height

    fps = 20
    sec = 15

    image_data = np.empty((image_width, image_height, 3))
    frames = []

    a_values = np.linspace(a0, an, fps*sec)
    b_values = np.linspace(b0, bn, fps*sec)

    for idx_mod in range(fps*sec):
        for idx_x in range(image_width):
            for idx_y in range(image_height):
                x = chladni_left_bound + (idx_x * x_ratio)
                y = chladni_up_bound - (idx_y * y_ratio)
                chladni_value = chladni_equation(a_values[idx_mod], b_values[idx_mod], n, m, x, y)
                if (chladni_value >= 0 - error_margin) and (chladni_value <= 0 + error_margin):
                    image_data[idx_x][idx_y] = [255, 255, 255]
                else:
                    image_data[idx_x][idx_y] = [0, 0, 0]
        frames.append(image_data.copy())

    frames_wr = frames.copy()
    for i in range(len(frames)-2, 0, -1):
        frames_wr.append(frames[i])

    clip = ImageSequenceClip(list(frames_wr), fps=fps)
    clip.write_gif('chladni_var_a_b.gif', fps=fps)