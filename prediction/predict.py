from preprocessing.image_preprocessing import preprocess_mri
from segmentation.meniscus_segmentation import segment_meniscus
from thickness.thickness_measurement import calculate_thickness


def analyze_knee(image_path, pixel_spacing=1.0):

    # Step 1: Preprocess MRI
    processed_image = preprocess_mri(image_path)

    # Step 2: Segment meniscus
    meniscus_mask = segment_meniscus(processed_image)

    # Step 3: Measure thickness
    thickness = calculate_thickness(
        meniscus_mask,
        pixel_spacing
    )

    return {
        "meniscus_thickness_mm": round(thickness, 2)
    }


if __name__ == "__main__":

    image_path = "sample_mri.jpg"

    result = analyze_knee(
        image_path,
        pixel_spacing=1.0
    )

    print("----- AI KNEE ANALYSIS -----")
    print(
        "Estimated Meniscus Thickness:",
        result["meniscus_thickness_mm"],
        "mm"
    )
