import numpy as np

def grayscale(image_array):
    
    """
    Convert an RGB image to grayscale.
    """
    
    red = image_array[:, :, 0]
    green = image_array[:, :, 1]
    blue = image_array[:, :, 2]

    gray = (0.299 * red) + (0.587 * green) + (0.114 * blue)

    return gray.astype(np.uint8)


def negative(image_array):
    
    """
    Convert an RGB image to negative.
    """
    
    return (255 - image_array).astype(np.uint8)