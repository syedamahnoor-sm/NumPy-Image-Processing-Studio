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


def apply_filter(filter_name, image_array, **kwargs):
    if filter_name == "grayscale":
        return grayscale(image_array)

    elif filter_name == "negative":
        return negative(image_array)

    elif filter_name == "brightness":
        return brightness(image_array, kwargs.get("value", 40))

    elif filter_name == "contrast":
        return contrast(image_array, kwargs.get("factor", 1.5))

    elif filter_name == "horizontal_flip":
        return horizontal_flip(image_array)

    elif filter_name == "vertical_flip":
        return vertical_flip(image_array)

    elif filter_name == "rotate_90":
        return rotate_90(image_array)

    elif filter_name == "crop":
        return crop(
            image_array,
            kwargs.get("start_row", 20),
            kwargs.get("end_row", 120),
            kwargs.get("start_col", 30),
            kwargs.get("end_col", 180)
        )

    elif filter_name == "threshold":
        return threshold(image_array, kwargs.get("threshold_value", 128))

    else:
        raise ValueError(f"Unknown filter: {filter_name}")