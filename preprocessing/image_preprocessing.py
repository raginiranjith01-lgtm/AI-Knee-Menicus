import cv2
import numpy as np


def preprocess_mri(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("MRI image could not be loaded")

    # Resize MRI image
    image = cv2.resize(image, (256, 256))

    # Reduce noise
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Normalize image intensity
    image = cv2.normalize(
        image,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return image


print("MRI preprocessing module loaded successfully.")
