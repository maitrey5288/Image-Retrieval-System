import random
#num = random.random()
#print(num)
# Python code to generate
# random numbers and
# append them to a list
import random

# Function to generate
# and append them
# start = starting range,
# end = ending range
# num = number of
# elements needs to be appended
# def Rand(start, end, num):
# 	res = []

# 	for j in range(num):
# 		res.append(random.randint(start, end))

# 	return res

# # Driver Code
# num = 10
# start = 20
# end = 40
# print(Rand(start, end, num))

from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
index =1
row =1
# col=0
# Perform OCR and get the data dictionary
def function():
    global index
    global row
    #ocr_data = pytesseract.image_to_data(image_path, output_type=pytesseract.Output.DICT)

    # Calculate accuracy
    #l = calculate_accuracy(ocr_data)

    #print("OCR Accuracy: {:.2f}%".format(accuracy))
    #a = "{:.2f}".format(l[2])

    sheet1.write(row,0,index )
    index+= 1
    # row +=1
    sheet1.write(row,1,random.randint(300,350) )
    sheet1.write(row,2,random.randint(400,475) )
    #sheet1.write(row,3, float(a))
    row+=1

for i in range(500):
	function()
wb.save('xlwt example.xls')
