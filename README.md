# 🖼️ NumPy Image Processing Studio

A lightweight desktop application that demonstrates fundamental image processing techniques using **NumPy**. The project applies common image filters and transformations by directly manipulating image arrays, providing a practical understanding of how digital image processing works under the hood.

The application features a simple **Tkinter GUI** that allows users to load images, apply filters, preview the results, and save processed images.

---

## 🚀 Features

- Convert images to **Grayscale**
- Generate **Negative** images
- Adjust **Brightness**
- Adjust **Contrast**
- **Horizontal Flip**
- **Vertical Flip**
- **90° Rotation**
- **Image Cropping**
- **Thresholding (Black & White)**
- Live image preview
- Save processed images with unique timestamps

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pillow (Image Loading & Saving)
- Tkinter (GUI)

---

## 📂 Project Structure

```
numpy-image-processing-studio/
│
├── images/                # Sample input images
├── outputs/               # Processed images
│
├── filters.py             # Image processing algorithms
├── processor.py           # Filter controller
├── app.py                 # Tkinter GUI
├── main.py                # Backend testing
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📸 Supported Filters

| Filter | Description |
|---------|-------------|
| Grayscale | Converts RGB images into grayscale using weighted luminance calculation |
| Negative | Inverts every RGB channel to create a photographic negative |
| Brightness | Increases or decreases pixel intensity |
| Contrast | Enhances or reduces image contrast |
| Horizontal Flip | Mirrors the image along the vertical axis |
| Vertical Flip | Mirrors the image along the horizontal axis |
| Rotate 90° | Rotates the image counter-clockwise |
| Crop | Extracts a selected rectangular region |
| Threshold | Converts the image into a black & white representation |

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/syedamahnoor-sm/numpy-image-processing-studio.git
```

Navigate into the project

```bash
cd numpy-image-processing-studio
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

## 🧠 What I Learned

This project helped me gain hands-on experience with:

- NumPy array manipulation
- Multi-dimensional indexing and slicing
- Image representation as matrices
- Vectorized operations
- Broadcasting
- Data type conversion
- Image transformations
- Modular Python project structure
- Building desktop applications with Tkinter

---

## 💡 Future Improvements

- Blur filter
- Sharpen filter
- Edge detection
- Additional rotation angles
- Undo/Redo functionality
- Image histogram visualization
- Drag-and-drop image support
- Dark mode interface
- Multiple image format export

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Syed Mahnoor**

