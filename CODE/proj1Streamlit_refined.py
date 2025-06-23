import streamlit as st
import cv2 as cv
from PIL import Image
import numpy as np
import transformations as pt
from io import BytesIO

#converting the numpy array to pil image to byte io to make it downloadable
def convert_img_tobytes(img_arry):
    image_pil=Image.fromarray(img_arry)
    buff=BytesIO()
    image_pil.save(buff,format='PNG')
    byte_im=buff.getvalue()
    return byte_im

def main():
    st.cache_data.clear()

    st.title("🖼️ Welcome to PhotoMaven")
    st.badge("Upload the image", icon="🔃", color="green")

    # Upload image with unique key
    pic = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"], key="upload_main")

    if pic is not None:
        img = Image.open(pic)
        st.image(img, caption="⬆️ Uploaded pic", use_container_width=True)
        img_arry = np.array(img)
        

        # Sidebar
        st.sidebar.subheader("🎆 Transform")

        # Effects
        with st.sidebar.expander("🎨 Effects"):
            st.write("Apply image filters here")
            choice = st.selectbox(
                "Choose an Effect",
                ["None", "Grayscale", "Gaussian Blur", "Canny Edge detection"],
                key="effect_select"
            )

        if choice == "None":
            st.image(img_arry, caption="⬆️ Effects Image", use_container_width=True)
            st.download_button("Download effects Image", data=convert_img_tobytes(img_arry),file_name="effected_image.png", mime="image/png", key="dl1_effects")
        else:
            img_arry = pt.effects(img_arry, choice)
            st.image(img_arry, caption=f"⬆️ {choice} Effect Image", use_container_width=True)
            st.download_button("Download effects Image", data=convert_img_tobytes(img_arry),file_name="effects_image.png", mime="image/png", key="dl2_effects")

        # Rotate
        with st.sidebar.expander("🌀 Rotate"):
            rotate_degrees = st.slider("Rotate (degrees)", -180, 180, 0, key="rotate_slider")
        img_arry = pt.rotate(img_arry, rotate_degrees)
        st.image(img_arry, caption="⬆️ Rotated Image", use_container_width=True)
        st.download_button("Download Rotated Image", data=convert_img_tobytes(img_arry),file_name="rotated_image.png", mime="image/png", key="dl_rotated")

        # Flip
        with st.sidebar.expander("🔁 Flip"):
            flip_horizontal = st.checkbox("Flip Horizontally", key="flip_h")
            flip_vertical = st.checkbox("Flip Vertically", key="flip_v")

        if flip_horizontal or flip_vertical:
            img_arry = pt.fliping(img_arry, flip_horizontal, flip_vertical)
            st.image(img_arry, caption="⬆️ Flipped Image", use_container_width=True)
            st.download_button("Download Flipped Image", data=convert_img_tobytes(img_arry),file_name="Flipped_image.png", mime="image/png", key="dl_Flipped")

        # Shear & Translate
        with st.sidebar.expander("↔️ Shear & Translate"):
            shear_x = st.slider("Shear X", -0.5, 0.5, 0.0, key="shear_x")
            shear_y = st.slider("Shear Y", -0.5, 0.5, 0.0, key="shear_y")

        if shear_x != 0 or shear_y != 0:
            img_arry = pt.shear(img_arry, shearing_x=shear_x, shearing_y=shear_y)
            st.image(img_arry, caption="⬆️ Sheared Image", use_container_width=True)
            st.download_button("Download Sheared Image", data=convert_img_tobytes(img_arry),file_name="Sheared_image.png", mime="image/png", key="dl1_Sheared")
        else:
            st.image(img_arry, caption="⬆️ Sheared Image (No Shear Applied)", use_container_width=True)
            st.download_button("Download Sheared Image", data=convert_img_tobytes(img_arry),file_name="Sheared_image.png", mime="image/png", key="dl2_Sheared")            

        # Text
        with st.sidebar.expander("💬 Text"):
            add_txt = st.text_input("Text", key="text_input")
            scaled = st.number_input("Scale", 1, 30, 1, key="scale_input")

        if add_txt.strip() != "":
            img_arry = pt.txt(img_arry, add_txt, scales=scaled)
            st.image(img_arry, caption="⬆️ Text Added Image", use_container_width=True)
            st.download_button("Download text Image", data=convert_img_tobytes(img_arry),file_name="txt_image.png", mime="image/png", key="dl_text")
        if add_txt.strip() == "":
            st.image(img_arry, caption="⬆️ Text   Image", use_container_width=True)

        # Crop
        with st.sidebar.expander("✂️ Crop"):
            img_width = pt.wide(img_arry)
            img_height = pt.high(img_arry)

            crop_left = st.number_input("Left", 0, img_width, 0, key="crop_left")
            crop_top = st.number_input("Top", 0, img_height, 0, key="crop_top")
            crop_right = st.number_input("Right", 0, img_width, 0, key="crop_right")
            crop_bottom = st.number_input("Bottom", 0, img_height, 0, key="crop_bottom")

        if crop_left > 0 or crop_top > 0 or crop_right > 0 or crop_bottom > 0:
            if (crop_left + crop_right < img_width) and (crop_top + crop_bottom < img_height):
                img_arry = pt.cropping(img_arry, crop_top, crop_bottom, crop_left, crop_right)
                st.image(img_arry, caption="⬆️ Cropped Image", use_container_width=True)
                st.download_button("Download Cropped Image", data=convert_img_tobytes(img_arry),file_name="Cropped_image.png", mime="image/png", key="dl1_Cropped")

            else:
                st.warning("⚠️ Cropping values exceed image dimensions. Please adjust them.")
        else:
            st.image(img_arry, caption="⬆️ Cropped Image (No Cropping Applied)", use_container_width=True)
            st.download_button("Download Cropped Image", data=convert_img_tobytes(img_arry),file_name="Cropped_image.png", mime="image/png", key="dl2_Cropped")



# Prevent double run
if __name__ == "__main__":
    main()
