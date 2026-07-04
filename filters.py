import numpy as np


def grayscale(image_array):
    red = image_array[:, :, 0]
    green = image_array[:, :, 1]
    blue = image_array[:, :, 2]

    gray = (0.299 * red) + (0.587 * green) + (0.114 * blue)

    return gray.astype(np.uint8)


def negative(image_array):
    return (255 - image_array).astype(np.uint8)


def brightness(image_array, value=40):
    """Apply brightness to an RGB image"""

    bright = image_array.astype(np.int16) + value
    bright = np.clip(bright, 0, 255)
    return bright.astype(np.uint8)

def contrast(image_array, factor=1.5):
    image = image_array.astype(np.float32)
    contrasted = 128 + factor * (image - 128)
    contrasted = np.clip(contrasted, 0, 255)
    return contrasted.astype(np.uint8)


def horizontal_flip(image_array):
    return image_array[:, ::-1, :]


def vertical_flip(image_array):
    return image_array[::-1, :, :]


def rotate_90(image_array):
    return np.rot90(image_array)


def crop(image_array, start_row, end_row, start_col, end_col):
    return image_array[start_row:end_row, start_col:end_col, :]


def threshold(image_array, threshold_value=128):
    red = image_array[:, :, 0]
    green = image_array[:, :, 1]
    blue = image_array[:, :, 2]

    gray = (0.299 * red) + (0.587 * green) + (0.114 * blue)

    black_white = np.where(gray >= threshold_value, 255, 0)

    return black_white.astype(np.uint8)
