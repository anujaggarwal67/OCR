from PIL import Image
import pytesseract
import cv2
import os
import numpy


image = cv2.imread("D:\\anuj\\New Doc 2018-06-21_1.jpg")
pytesseract.pytesseract.tesseract_cmd = r"C:\\Tesseract\\tesseract.exe"

text = pytesseract.image_to_string(image)
# print(text)
text = text.split("\n")
for i in range(len(text)):
    text[i] = text[i].strip()
for ele in text:
    if ele=="":
        text.remove(ele)
for j in range(len(text)):
    if("Permanent Account Number Card" in text[j]):
        print(text[j+1])
    if("/ Name" in text[j]):
        print(text[j+1])
    if("Father's Name" in text[j]):
        print(text[j+1])
    if("Date of Birth" in text[j]):
        print(text[j+1])