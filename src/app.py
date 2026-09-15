import streamlit as st

st.set_page_config(
    page_title="AI PCB Doctor",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI PCB Doctor")
st.subheader("AI-Powered PCB Fault Detection & Diagnosis")

st.write(
    "Upload a PCB image to perform AI-assisted visual inspection."
)

uploaded_file = st.file_uploader(
    "Upload PCB Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded PCB Image",
        use_container_width=True
    )

    st.info("AI analysis module will process the uploaded PCB image.")
