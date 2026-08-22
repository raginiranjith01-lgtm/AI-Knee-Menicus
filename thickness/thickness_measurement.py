import cv2
import numpy as np


def calculate_thickness(mask, pixel_spacing=1.0):
    """
    Estimate the maximum thickness of the segmented meniscus.

    mask: binary segmentation mask
    pixel_spacing: mm per pixel
    """

    thickness_values = []

    for y in range(mask.shape[0]):

        pixels = np.where(mask[y] > 0)[0]

        if len(pixels) > 1:
            thickness_pixels = pixels.max() - pixels.min()
            thickness_mm = thickness_pixels * pixel_spacing
            thickness_values.append(thickness_mm)

    if not thickness_values:
        return 0.0

    return max(thickness_values)


if __name__ == "__main__":

    mask = cv2.imread(
        "meniscus_mask.jpg",
        cv2.IMREAD_GRAYSCALE
    )

    if mask is None:
        print("Mask image not found.")
    else:
        thickness = calculate_thickness(
            mask,
            pixel_spacing=1.0
        )

        print(
            f"Estimated medial meniscus thickness: "
            f"{thickness:.2f} mm"
        )
