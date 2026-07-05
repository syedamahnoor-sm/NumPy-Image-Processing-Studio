import os
from datetime import datetime

import numpy as np
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from processor import apply_filter


selected_image_path = None
original_image_array = None
processed_image_array = None


def resize_for_preview(image, max_size=(300, 220)):
    image_copy = image.copy()
    image_copy.thumbnail(max_size)
    return ImageTk.PhotoImage(image_copy)


def select_image():
    global selected_image_path, original_image_array, processed_image_array

    selected_image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if not selected_image_path:
        return

    image_path_label.config(text=selected_image_path)

    image = Image.open(selected_image_path).convert("RGB")
    original_image_array = np.array(image)
    processed_image_array = None

    preview = resize_for_preview(image)
    original_preview_label.config(image=preview, text="")
    original_preview_label.image = preview

    processed_preview_label.config(image="", text="No processed image yet")
    processed_preview_label.image = None


def apply_selected_filter():
    global processed_image_array

    if original_image_array is None:
        messagebox.showerror("Error", "Please select an image first.")
        return

    filter_name = filter_dropdown.get()

    if not filter_name:
        messagebox.showerror("Error", "Please select a filter.")
        return

    options = {}

    if filter_name == "brightness":
        options["value"] = brightness_slider.get()

    elif filter_name == "contrast":
        options["factor"] = contrast_slider.get()

    elif filter_name == "threshold":
        options["threshold_value"] = threshold_slider.get()

    processed_image_array = apply_filter(filter_name, original_image_array, **options)

    processed_image = Image.fromarray(processed_image_array)
    preview = resize_for_preview(processed_image)

    processed_preview_label.config(image=preview, text="")
    processed_preview_label.image = preview


def save_processed_image():
    if processed_image_array is None:
        messagebox.showerror("Error", "Please apply a filter first.")
        return

    filter_name = filter_dropdown.get()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    os.makedirs("outputs", exist_ok=True)

    output_path = os.path.join("outputs", f"{filter_name}_{timestamp}.jpg")

    result_image = Image.fromarray(processed_image_array)
    result_image.save(output_path)

    messagebox.showinfo("Saved", f"Image saved successfully:\n{output_path}")


root = tk.Tk()
root.title("NumPy Image Processing Studio")
root.geometry("850x600")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="NumPy Image Processing Studio",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)


select_button = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    width=25
)
select_button.pack(pady=5)


image_path_label = tk.Label(
    root,
    text="No image selected",
    wraplength=700
)
image_path_label.pack(pady=5)


preview_frame = tk.Frame(root)
preview_frame.pack(pady=15)


original_frame = tk.Frame(preview_frame)
original_frame.grid(row=0, column=0, padx=25)

processed_frame = tk.Frame(preview_frame)
processed_frame.grid(row=0, column=1, padx=25)


tk.Label(original_frame, text="Original Image", font=("Arial", 12, "bold")).pack()

original_preview_label = tk.Label(
    original_frame,
    text="No image selected",
    bg="lightgray",
    width=35,
    height=12
)
original_preview_label.pack(pady=5)


tk.Label(processed_frame, text="Processed Image", font=("Arial", 12, "bold")).pack()

processed_preview_label = tk.Label(
    processed_frame,
    text="No processed image yet",
    bg="lightgray",
    width=35,
    height=12
)
processed_preview_label.pack(pady=5)


filter_dropdown = ttk.Combobox(
    root,
    values=[
        "grayscale",
        "negative",
        "brightness",
        "contrast",
        "horizontal_flip",
        "vertical_flip",
        "rotate_90",
        "threshold"
    ],
    state="readonly",
    width=35
)
filter_dropdown.set("grayscale")
filter_dropdown.pack(pady=10)


slider_frame = tk.Frame(root)
slider_frame.pack(pady=5)


tk.Label(slider_frame, text="Brightness").grid(row=0, column=0, padx=10)
brightness_slider = tk.Scale(slider_frame, from_=-100, to=100, orient="horizontal")
brightness_slider.set(40)
brightness_slider.grid(row=0, column=1, padx=10)


tk.Label(slider_frame, text="Contrast").grid(row=1, column=0, padx=10)
contrast_slider = tk.Scale(slider_frame, from_=0.5, to=3.0, resolution=0.1, orient="horizontal")
contrast_slider.set(1.5)
contrast_slider.grid(row=1, column=1, padx=10)


tk.Label(slider_frame, text="Threshold").grid(row=2, column=0, padx=10)
threshold_slider = tk.Scale(slider_frame, from_=0, to=255, orient="horizontal")
threshold_slider.set(128)
threshold_slider.grid(row=2, column=1, padx=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)


apply_button = tk.Button(
    button_frame,
    text="Apply Filter",
    command=apply_selected_filter,
    width=20
)
apply_button.grid(row=0, column=0, padx=10)


save_button = tk.Button(
    button_frame,
    text="Save Image",
    command=save_processed_image,
    width=20
)
save_button.grid(row=0, column=1, padx=10)


root.mainloop()