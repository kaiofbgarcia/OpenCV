from tkinter.filedialog import dialogstates
import cv2
from cv2 import THRESH_BINARY
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("img/dadosVerdes1.png")         
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray , 80 ,255, cv2.THRESH_BINARY)        
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)  

text = pytesseract.image_to_string(binary1, lang='por')
print(text)

cv2.imshow("Dilatation", binary1)

cv2.waitKey(0)
