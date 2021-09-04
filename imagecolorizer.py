import requests
import streamlit as st
st.markdown("<h1 style='text-align: center;color:Light Gray;'> Image Colorizer</h1>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;color:Light Gray;'>Color any Black and white image using this AI</h3>",unsafe_allow_html=True)
st.set_option('deprecation.showfileUploaderEncoding',False)
img_url=st.text_input("Enter the Image Url")
if img_url:
    if st.button('Colorize'):
        r=requests.post("https://api.deepai.org/api/colorizer",data={'image':img_url},
                        headers={'api-key':'e2629223-7c47-45f0-a6e6-fa0e74a2b7ce'})
        output=r.json()
        st.write(output)
        url=output['output_url']
        st.image(url)
        st.info("Original Image")
        st.image(img_url)
uploaded_file=st.file_uploader("Choose a file")
if uploaded_file:
    if st.button("Colorize"):
        r=requests.post("https://api.deepai.org/api/colorizer",files={'image':uploaded_file},
                        headers={'api-key':'e2629223-7c47-45f0-a6e6-fa0e74a2b7ce'})
        output=r.json()
        st.write(output)
        url=output['output_url']
        st.image(url)
        st.info("Original Image")
        st.image(uploaded_file)

