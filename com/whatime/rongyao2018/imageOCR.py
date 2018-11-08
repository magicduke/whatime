import pytesseract
from PIL import Image

im = Image.open('G://桌面/1.jpg')
imgry = im.convert('L')
#imgry.show()

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()

#pytesseract.pytesseract.tesseract_cmd = 'D://Tools/Develop Tools/Tesseract-OCR/tesseract.exe'
#text = pytesseract.image_to_string(Image.open('G://桌面/1.jpg'),lang='chi_sim')

#print(text)