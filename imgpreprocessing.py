import cv2
import pytesseract
from pytesseract import Output
from skimage.transform import rotate
from deskew import determine_skew
import os
#import numpy as np

if not (os.path.isdir('./temp')):
    os.mkdir('temp')




def textfunwithoutkeyword():
    
    image_file = "Untitled.png" #abc.jpg
    img = cv2.imread(image_file)



    dst = cv2.fastNlMeansDenoisingColored(img, None, h=3,searchWindowSize=21,templateWindowSize=7)
    cv2.imwrite('temp/denoisecolor.jpg',dst)

    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = grayscale(dst)
    cv2.imwrite("temp/gray.jpg", gray_image)

    binimg = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 15, 15)
    cv2.imwrite('temp/binarised.jpg',binimg)



    def deskew(_img):
        

        angle = determine_skew(_img)
        rotated = rotate(_img, angle, resize=True) * 255
        return rotated

    deskew_img=deskew(binimg)
    deskew_img=deskew(deskew_img)
    cv2.imwrite("temp/deskew.jpg",deskew_img)


    img =cv2.imread("./temp/deskew.jpg")

    height ,width, _ = img.shape

    data = pytesseract.image_to_data(img,output_type=Output.DICT)


    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        # if float(data['conf'][i]) > 50:
            (x,y,width,height) = (data['left'][i],data['top'][i],data['width'][i],data['height'][i] )
            img = cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
            img = cv2.putText(img,data['text'][i],(x,y+height+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)

    # cv2.imshow("img",img)
    cv2.imwrite("temp/final.jpg",img)
