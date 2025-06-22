import cv2 as cv


img = cv.imread("D:/val_facerecog/messi1.jpg")


# def effects(photo,choice_user):
#     if choice_user == "Gaussian Blur":
#         return cv.GaussianBlur(photo,(5,5),cv.BORDER_DEFAULT)
    
#     if choice_user == "Grayscale" :
#         return cv.cvtColor(photo,cv.COLOR_RGB2GRAY)
    
#     if choice_user == "Canny Edge detection":
#         return cv.Canny(photo,125,175)

# effects(img,choice_user="Grayscale" )

# cv.imshow("effet",effects(img,choice_user="Grayscale" ))

# def cropping(photo,crop_in_top,crop_in_bottom,crop_in_left,crop_in_right):
# height,Width=img.shape[:2]
# y1=50
# y2=20
# x1=20
# x2=50
# photo=img[y1:height-y2,x1:Width-x2]

# cv.imshow("pic",img)

# def cropping(photo,crop_in_top,crop_in_bottom,crop_in_left,crop_in_right):
#     height,width=photo.shape[:2]
    
#     photo=photo[crop_in_top:height-crop_in_bottom,crop_in_left:width-crop_in_right]
#     return photo

# cropimag=cropping(img,50,30,10,15)
# cv.imshow("pic",cropimag)

# cv.waitKey(0)

def effects(photo,choice_user):
    if choice_user == "Gaussian Blur":
        return cv.GaussianBlur(photo,(5,5),cv.BORDER_DEFAULT)
    
    if choice_user == "Grayscale" :
        return cv.cvtColor(photo,cv.COLOR_RGB2GRAY)
    
    if choice_user == "Canny Edge detection":
        return cv.Canny(photo,125,175)
    
    else:
        pass

effected=effects(img,"Grayscale")
cv.imshow("hyulullu",effected)

cv.waitKey(0)