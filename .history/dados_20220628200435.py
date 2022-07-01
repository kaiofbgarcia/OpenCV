import cv2
from cv2 import THRESH_BINARY
import numpy as np
from numpy import binary_repr

imagem = cv2.imread("img/dados1.jpg")          # Carregar a imagem
res = cv2.resize(imagem, dsize=( 598, 800), interpolation=cv2.INTER_CUBIC) # Redimensionar Img ################
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)     # GrayScale
blur = cv2.blur(gray,(1,1))                       # Blur ###############

ret,binary = cv2.threshold(blur , 127 ,255, cv2.THRESH_BINARY)         # Binarização ################
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)   # Inverter a Binarização

kernel = np.ones((6,6), np.uint8)
dilation = cv2.dilate(binary1, kernel, iterations=3)   # Dilatar ####################

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Procura os Objetos
cont = len(contours)                                                                     # Conta os Objetos
    
print("Numero de Objetos Encontrados: ",cont)

cv2.imshow("Dilatation", dilation)


cv2.waitKey(0)