import cv2


def segment_meniscus(image):

    # Convert image to grayscale if required
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding for initial segmentation
    _, mask = cv2.threshold(
        image,
        80,
        255,
        cv2.THRESH_BINARY
    )

    # Morphological operations
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (5, 5)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    return mask


print("Meniscus segmentation module loaded successfully.")
