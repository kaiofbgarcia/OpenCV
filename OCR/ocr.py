import cv2
import pytesseract
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("img/meme.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
text = pytesseract.image_to_string(binary, lang='por')
print(text)
language = 'pt'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")