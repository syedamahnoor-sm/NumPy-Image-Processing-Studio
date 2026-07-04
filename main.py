import os

import numpy as np
from PIL import Image

from processor import apply_filter

# Function to Save Image
def save_image(array, filename):
    os.makedirs("outputs", exist_ok=True)
    image = Image.fromarray(array)
    image.save(os.path.join("outputs", filename))
    print(f"{filename} saved")


image = Image.open("images/input.jpg").convert("RGB")
image_array = np.array(image)

filters_to_apply = [
    ("grayscale", {}),
    ("negative", {}),
    ("brightness", {"value": 40}),
    ("contrast", {"factor": 1.5}),
    ("horizontal_flip", {}),
    ("vertical_flip", {}),
    ("rotate_90", {}),
    ("crop", {
        "start_row": 20,
        "end_row": 120,
        "start_col": 30,
        "end_col": 180
    }),
    ("threshold", {"threshold_value": 128})
]

for filter_name, options in filters_to_apply:
    result = apply_filter(filter_name, image_array, **options)
    save_image(result, f"{filter_name}.jpg")