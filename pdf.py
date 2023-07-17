from pdf2image import convert_from_path
import os
import textfun
import jsonfunction
from pathlib import Path
 
dir = './static/a.pdf'
print(Path(dir).stem) 
print(os.path.dirname('./static/a.pdf'))
print(os.path.basename('./static/a.pdf'))

def pdfconvert(file_path):
    images = convert_from_path(file_path,poppler_path = r"C:\poppler-23.05.0\Library\bin" )
    newpath =f"{os.path.dirname(file_path)}/{Path(file_path).stem}/"
    if not (os.path.exists(newpath)):
      os.mkdir(newpath)
    for i in range(len(images)):
      images[i].save(f'{newpath}/page'+ str(i) +'.jpg', 'JPEG')


    imagelist = os.listdir(newpath) 
    pdf_data ={}
    for i in imagelist:
        print(f"{os.path.dirname(file_path)}/{i}")
        text_data = textfun.textfunwithkeyword(f"{newpath}/{i}") 
        pdf_data[i] =text_data   
    jsonfunction.jsonsavepdf(os.path.basename(file_path),pdf_data)

# pdfconvert(dir)