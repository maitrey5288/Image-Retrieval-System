import cv2
import pytesseract
from pytesseract import Output
from skimage.transform import rotate
from deskew import determine_skew
import os
import numpy as np
# import xlwt
from xlwt import Workbook

    # Workbook is created
wb = Workbook()

    # add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
index =1
row =1
if not (os.path.isdir('./temp')):
    os.mkdir('temp')
def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thin_font(image):
        image = cv2.bitwise_not(image)
        kernel = np.ones((2,2),np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return (image)

def thick_font(image):
        image = cv2.bitwise_not(image)
        kernel = np.ones((2,2),np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return (image)

def deskew(_img):
        angle = determine_skew(_img)
        rotated = rotate(_img, angle, resize=True) * 255
        return rotated
def calculate_accuracy(ocr_data):
    l=[]
    total_chars = 0
    
    correct_chars = 0
    for i in range(len(ocr_data['text'])):
        confidence = int(ocr_data['conf'][i])
        if confidence >= 0:
            total_chars += 1
            if confidence >= 80:
                if ocr_data['text'][i].strip():
                    correct_chars += 1
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    l.append(correct_chars)
    l.append(total_chars)
    l.append(accuracy)

    return l
def textfunwithkeyword(img):
    global row
    global index
    text = ''
    image_file = img
    img = cv2.imread(image_file)

    dst = cv2.fastNlMeansDenoisingColored(img, None, h=3,searchWindowSize=21,templateWindowSize=7)
    cv2.imwrite('./temp/denoisecolor.jpg',dst)

    

    gray_image = grayscale(dst)
    cv2.imwrite("./temp/gray.jpg", gray_image)

    binimg = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 15, 15)
    cv2.imwrite('./temp/binarised.jpg',binimg)

   
    eroded_image =      (binimg)
    cv2.imwrite("./temp/eroded_image1.jpg", eroded_image)

  
    dilated_image = thick_font(binimg)
    cv2.imwrite("./temp/dilated_image1.jpg", dilated_image)

   

    deskew_img=deskew(binimg)
    cv2.imwrite("./temp/deskew.jpg",deskew_img)
    eroded_image = thin_font(deskew_img)
    cv2.imwrite("./temp/eroded_image2.jpg", eroded_image)
    dilated_image = thick_font(binimg)
    cv2.imwrite("./temp/dilated_image2.jpg", dilated_image)



    img =cv2.imread("./temp/deskew.jpg")
    a=pytesseract.image_to_data("./temp/binarised.jpg", output_type=pytesseract.Output.DICT)
    l = calculate_accuracy(a)
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/gray.jpg")
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/binarised.jpg")
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/eroded_image1.jpg")
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/dilated_image1.jpg")
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/eroded_image2.jpg")
    text += pytesseract.image_to_string(img)
    img =cv2.imread("./temp/dilated_image2.jpg")
    text += pytesseract.image_to_string(img)



    #print("OCR Accuracy: {:.2f}%".format(accuracy))
    a = "{:.2f}".format(l[2])

    sheet1.write(row,0,index )
    index+= 1
    # row +=1
    sheet1.write(row,1,l[0] )
    sheet1.write(row,2,l[1] )
    sheet1.write(row,3, float(a))
    wb.save('modified_prep.xls')
    row+=1


    return text
