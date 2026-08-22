import streamlit as st
from prediction.predict import analyze_knee


st.set_page_config(
    page_title="AI Knee Meniscus Assessment",
    page_icon="🦵",
    layout="centered"
)

st.title("🦵 AI-Assisted Knee Assessment")

st.write(
    "Upload a knee MRI image to perform a prototype "
    "meniscus thickness assessment."
)

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_path = "uploaded_mri.jpg"

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.image(
        uploaded_file,
        caption="Uploaded MRI Image",
        use_container_width=True
    )

    if st.button("Analyze MRI"):

    try:
        result = analyze_knee(
            file_path,
            pixel_spacing=1.0
        )

        thickness = result[
            "meniscus_thickness_mm"
        ]
        femur = result["femur_width_mm"]
        tibia = result["tibia_width_mm"]
        implant = result["implant_size"]

        st.success("Analysis completed!")

        st.metric(
            "Estimated Meniscus Thickness",
            f"{thickness:.2f} mm"
        )

        st.metric(
            "Femur Width",
            f"{femur:.2f} mm"
        )

        st.metric(
            "Tibia Width",
            f"{tibia:.2f} mm"
        )

        st.success(f"Recommended Implant Size: {implant}")

    except Exception as error:
        st.error(
            f"Unable to process image: {error}"
        )   


st.warning(
    "This is an academic prototype and is not intended "
    "for clinical diagnosis or treatment decisions."
)
return {
    "meniscus_thickness_mm": thickness,
    "femur_width_mm": femur,
    "tibia_width_mm": tibia,
    "implant_size": implant
}
