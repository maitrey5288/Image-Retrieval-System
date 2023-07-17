import pytesseract
import os
# import random
# num = random.random()
# print(num)


# import xlwt
from xlwt import Workbook

    # Workbook is created
wb = Workbook()

    # add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

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

# Image file path
index =1
row =1
# col=0
# Perform OCR and get the data dictionary
def function(image_path):
    
    global index
    global row
    
    # if row==11:
    #     wb.save('abc example.xls')
    #     exit()
    ocr_data = pytesseract.image_to_data(image_path, output_type=pytesseract.Output.DICT)

    # Calculate accuracy
    l = calculate_accuracy(ocr_data)

    #print("OCR Accuracy: {:.2f}%".format(accuracy))
    a = "{:.2f}".format(l[2])

    sheet1.write(row,0,index )
    index+= 1
    # row +=1
    sheet1.write(row,1,l[0] )
    sheet1.write(row,2,l[1] )
    sheet1.write(row,3, float(a))
    row+=1
    


    

    # print(a)

# dir_list = os.listdir('./PNG')

#for i in dir_list :
function('./l.jpg')

# function('./PNG/0a46d21b0b60ed73b2d00472da2c9d14e702934afe7131f6be18e55de694e44e_0017.png')

# Writing to an excel
#wb.save('abc example.xls')
wb.save('modified1.xls')

# sheet using Python