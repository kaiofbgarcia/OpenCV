import cv2
from cv2 import THRESH_BINARY
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread("img/dadosVerdes1.png")          # Carregar a imagem
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
text = pytesseract.image_to_string(binary, lang='por')
print(text)
