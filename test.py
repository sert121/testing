import streamlit as st
from webcam import webcam

captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)

st.download_button(data=captured_image,file_name="default.png")

