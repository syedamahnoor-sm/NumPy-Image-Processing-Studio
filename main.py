import os

import numpy as np
from PIL import Image

from filters import grayscale
from filters import negative


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


# Create Output Folder
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Function to Save Image
def save_image(image, filename):

    filepath = os.path.join(output_folder, filename)

    if os.path.exists(filepath):
        print(f"{filename} already exists. Skipping...\n")
        return

    image.save(filepath)
    print(f"{filename} saved successfully.\n")


#GRAYSCALE FILTER
gray_array = grayscale(image_array)

gray_image = Image.fromarray(gray_array)
gray_image.save("outputs/grayscale.jpg")

print("Grayscale image saved successfully.")

#NEGATIVE FILTER
negative_array = negative(image_array)

negative_image = Image.fromarray(negative_array)

save_image(negative_image, "negative.jpg")