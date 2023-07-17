import pytesseract
import cv2
img =cv2.imread("./d.png")
text = pytesseract.image_to_string(img)
print(text)