import streamlit as st
from webcam import webcam
from io import BytesIO
import base64 

def get_image_download_link(img,filename,text):
	img = img.convert('RGB')
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
	return href


captured_image = webcam()


if captured_image is None:
	st.write("Waiting for capture...")
else:
	st.write("Got an image from the webcam:")
	# st.write(type(captured_image))
	st.image(captured_image)
	# link = get_image_download_link(captured_image,"default",)
	st.markdown(get_image_download_link(captured_image,"capt_img.png",'Download img'), unsafe_allow_html=True)

	# st.download_button(label="Download image",data=captured_image,file_name="default.png")

