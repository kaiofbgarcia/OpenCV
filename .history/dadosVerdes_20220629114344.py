from tkinter.filedialog import dialogstates
import cv2
from cv2 import THRESH_BINARY
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("img/dadosVerdesFila.png")         
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray , 60 ,255, cv2.THRESH_BINARY)        
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)  
kernel = np.ones((5,5), np.uint8)                   # Erosão
dilation = cv2.dilate(binary1, kernel, iterations=2)  # Erosão
text = pytesseract.image_to_string(dilation, lang='por')
print(text)

cv2.imshow("Dilatation", dilation)

cv2.waitKey(0)
