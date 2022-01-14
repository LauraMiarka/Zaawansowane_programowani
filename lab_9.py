import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_1 = cv2.cvtColor(cv2.imread('photo.JPG'), cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(cv2.imread('photo2.JPG'), cv2.COLOR_BGR2GRAY)
img_3 = cv2.cvtColor(cv2.imread('photo3.JPG'), cv2.COLOR_BGR2GRAY)
img_4 = cv2.cvtColor(cv2.imread('photo4.JPG'), cv2.COLOR_BGR2GRAY)


def read_from_image(img):
     return pytesseract.image_to_string(img)


print(read_from_image(img_1))
print(read_from_image(img_2))
print(read_from_image(img_3))
print(read_from_image(img_4))
