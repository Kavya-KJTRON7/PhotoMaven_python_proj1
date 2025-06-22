import cv2 as cv
import Streamlit as stream

def high(photo):
    height,width=photo.shape[:2]
    # dimensity=(height,width)
    return height 

def wide(photo):
    height,width=photo.shape[:2]
    # dimensity=(height,width)
    return width

# rotate Function
def rotate(photo,rotate_angle,rotpoint=None):

    height,width = (photo.shape[:2])

    if rotpoint==None:
        rotpoint=(width//2,height//2)

    dimensions=(width,height)
    rotMat=cv.getRotationMatrix2D(rotpoint,rotate_angle,scale=1.0)
    return cv.warpAffine(photo,rotMat,dimensions)


#flip
def fliping(photo, fliped_horizontal=0, fliped_vertical=0):
    if fliped_horizontal == 1 and fliped_vertical == 1:
        return cv.flip(photo, -1)
    elif fliped_horizontal == 1:
        return cv.flip(photo, 0)
    elif fliped_vertical == 1:
        return cv.flip(photo, 1)
    else:
        return photo  # no flip, return original


#Text 
def txt(photo,text_to_be_add,scales):
    
    height,width = (photo.shape[:2])
    return cv.putText(photo,text_to_be_add,(width//2, height//2), cv.FONT_HERSHEY_TRIPLEX, scales,(255, 0, 255),thickness=7)

#crop

def cropping(photo,crop_in_top,crop_in_bottom,crop_in_left,crop_in_right):
    height,width=photo.shape[:2]
    
    photo= photo[crop_in_top : height - crop_in_bottom, crop_in_left : width - crop_in_right]
    return photo


#effects 1)Grayscale 2)gaussian blur 3)Canny edges


def effects(photo,choice_user):
    if choice_user == "Gaussian Blur":
        return cv.GaussianBlur(photo,(11,11),cv.BORDER_DEFAULT)
    
    if choice_user == "Grayscale" :
        return cv.cvtColor(photo,cv.COLOR_RGB2GRAY)
    
    if choice_user == "Canny Edge detection":
        return cv.Canny(photo,125,175)
    
    else:
        pass
