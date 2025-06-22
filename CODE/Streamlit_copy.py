import streamlit as st
import cv2 as cv
from PIL import Image
import numpy as np
import transformations as pt

st.cache_data.clear()

st.title("🖼️ Welcome to PhotoMaven")
st.badge("Upload the image ", icon="🔃" , color="green")


#uploading image
pic = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])


if pic is not None:
    img= Image.open(pic)
    st.image(img, caption="Uploaded pic " , use_container_width=True)
    img_arry= np.array(img)
    #rotated_img_RGB=cv.cvtColor(img_arry, cv.COLOR_RGB2BGR) #since the PIL image is in RGB format but OPENCV Needs BGR FORMAT

    #Sidebar
    st.sidebar.subheader("🎆 Transform")

    # Effects 
    with st.sidebar.expander("🎨 Effects"):
        st.write("Apply image filters here")
        choice=st.selectbox("Choose an Effect", ["None","Grayscale","Gaussian Blur","Canny Edge detection"])
        # print(choice)

    #effects actual function call
    if img_arry is not None:
        if choice=="None":
            st.image(img_arry, caption="Effects Image", use_container_width=True)
        else:
            img_arry=pt.effects(img_arry,choice)
            st.image(img_arry, caption="Effects Image", use_container_width=True)

    # Rotate section
    with st.sidebar.expander("🌀 Rotate"):
        rotate_degrees = st.slider("Rotate (degrees)", -180, 180, 0)

    #ROTATE actual function call
    img_arry =pt.rotate(img_arry,rotate_degrees)
    st.image(img_arry, caption="Rotated Image", use_container_width=True)


    # Flip section
    
    with st.sidebar.expander("🔁 Flip"):
        flip_horizontal = st.checkbox("Flip Horizontally")
        flip_vertical = st.checkbox("Flip Vertically")
        # print(flip_horizontal,flip_vertical)

    #flip actual function call
    if flip_horizontal==0 and flip_vertical==0:
        pass
    
    elif img_arry is not None:
        img_arry=pt.fliping(img_arry,flip_horizontal,flip_vertical)
        st.image(img_arry, caption="Flipped image", use_container_width=True)


    # Shear & Translate section
    with st.sidebar.expander("↔️ Shear & Translate"):
        shear_x = st.slider("Shear X", -0.5, 0.5, 0.0)
        shear_y = st.slider("Shear Y", -0.5, 0.5, 0.0)

    #add text to image 
    with st.sidebar.expander("💬Text"):
        add_txt= st.text_input("Text")
        scaled=st.number_input("scale",1,30,1)
        

    #text actual function call
    if add_txt== ("").strip:
        pass
    else:
        img_arry=pt.txt(img_arry,add_txt,scales=scaled)
        st.image(img_arry, caption="text image", use_container_width=True)


    # Crop section
    with st.sidebar.expander("✂️ Crop"):
        crop_left = st.number_input("Left", 0, pt.wide(img_arry), 0)
        crop_top = st.number_input("Top", 0, pt.high(img_arry), 0)
        crop_right = st.number_input("Right", 0, pt.wide(img_arry), 0)
        crop_bottom = st.number_input("Bottom", 0, pt.high(img_arry), 0)
    
    if(crop_left>0 or crop_top >0 or crop_right>0 or crop_bottom >0):
        if img_arry is not None:
            img_arry= pt.cropping(img_arry,crop_top,crop_bottom,crop_left,crop_right)
            st.image(img_arry, caption="Crop image", use_container_width=True)
    else:
          st.image(img_arry, caption="Crop image", use_container_width=True)