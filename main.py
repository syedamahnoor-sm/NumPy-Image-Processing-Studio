import os

import numpy as np
from PIL import Image

from filters import (
    grayscale,
    negative,
    brightness,
    contrast,
    horizontal_flip,
    vertical_flip,
    rotate_90,
    crop,
    threshold
)

#Load the image
image = Image.open("images/input.jpg")

#Convert the image to numpy array
image_array = np.array(image)


print("Image loaded successfully.\n")

print(f"Shape       : {image_array.shape}")
print(f"Data Type   : {image_array.dtype}")
print(f"Dimensions  : {image_array.ndim}")
print(f"Total Pixels: {image_array.shape[0] * image_array.shape[1]}")
print(f"First Pixel : {image_array[0, 0]}")

# Function to Save Image
def save_image(array, filename):
    os.makedirs("outputs", exist_ok=True)
    image = Image.fromarray(array)
    image.save(os.path.join("outputs", filename))
    print(f"{filename} saved")


image = Image.open("images/input.jpg").convert("RGB")
image_array = np.array(image)

save_image(grayscale(image_array), "grayscale.jpg")
save_image(negative(image_array), "negative.jpg")
save_image(brightness(image_array), "brightness.jpg")
save_image(contrast(image_array, 1.5), "contrast.jpg")
save_image(horizontal_flip(image_array), "horizontal_flip.jpg")
save_image(vertical_flip(image_array), "vertical_flip.jpg")
save_image(rotate_90(image_array), "rotate_90.jpg")
save_image(crop(image_array, 20, 120, 30, 180), "crop.jpg")
save_image(threshold(image_array, 128), "threshold.jpg")