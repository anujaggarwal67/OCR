from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        from PIL import Image
        import pytesseract
        import cv2
        import os
        import numpy

        file1 = request.FILES['filename']
        image = cv2.imdecode(numpy.fromstring(file1.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        pytesseract.pytesseract.tesseract_cmd = r"/app/.apt/usr/bin/tesseract"

        text = pytesseract.image_to_string(Image.open(file1))
        context = {}
        
        text = text.split("\n")
        for i in range(len(text)):
            text[i] = text[i].strip()
        for ele in text:
            if ele=="":
                text.remove(ele)
        for j in range(len(text)):
            if("Permanent Account Number Card" in text[j]):
                context['PAN'] = text[j+1]
            if("/ Name" in text[j]):
                context['Name'] = text[j+1]
            if("Father's Name" in text[j]):
                context['FatherName'] = text[j+1]
            if("Date of Birth" in text[j]):
                context['DOB'] = text[j+1]
        return render(request,'index.html',{'context':context})
    return render(request,'index.html')