import numpy as np
from PIL import Image
from filters import grayscale

#Load the image
image = Image.open("images/input.jpg")

#Convert the image to numpy array
image_array = np.array(image)

#Implement grayscale
gray_array = grayscale(image_array)

gray_image = Image.fromarray(gray_array)
gray_image.save("outputs/grayscale.jpg")

print("Grayscale image saved successfully.")