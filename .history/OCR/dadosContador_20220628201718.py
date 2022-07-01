import cv2
from cv2 import THRESH_BINARY
from cv2 import erode
import numpy as np
from numpy import binary_repr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

imagem = cv2.imread("img/dados2.jpg")          # Carregar a imagem
res = cv2.resize(imagem, dsize=( 598, 800), interpolation=cv2.INTER_CUBIC) # Redimensionar Img ################
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
ret1, binary1 = cv2.threshold(binary, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

text = pytesseract.image_to_string(binary, lang='por')

print(text)

cv2.imshow("Dilatation", binary)


cv2.waitKey(0)