from tkinter.filedialog import dialogstates
import cv2
from cv2 import THRESH_BINARY
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("img/dadosVerdesFila.png")         
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret,binary = cv2.threshold(blur , 65 ,255, cv2.THRESH_BINARY)        
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)                   
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(binary1, kernel, iterations=1)

text = pytesseract.image_to_string(dilation, lang='por')
#print(text)

def getSum(n):  
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
n = text
print(getSum(n))

cv2.imshow("Dilatation", dilation)
print(sum)
cv2.waitKey(0)
