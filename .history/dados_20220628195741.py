import cv2
from cv2 import THRESH_BINARY
import numpy as np
from numpy import binary_repr

imagem = cv2.imread("img/dados3.jpg")          # Carregar a imagem
res = cv2.resize(imagem, dsize=( 598, 800), interpolation=cv2.INTER_CUBIC) # Redimensionar Img ################
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)     # GrayScale
blur = cv2.blur(gray,(2,2))                       # Blur ###############

ret, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU)
ret1, binary1 = cv2.threshold(binary, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(binary, kernel, iterations=1)   # Dilatar ####################

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Procura os Objetos
cont = len(contours)                                                                     # Conta os Objetos
    
print("Numero de Objetos Encontrados: ",cont)

cv2.imshow("Dilatation", binary)


cv2.waitKey(0)