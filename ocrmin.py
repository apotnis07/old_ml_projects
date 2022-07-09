from PIL import Image
import pytesseract
import argparse
import cv2
import os
import string
a=[]
z=''
result=0
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#                help="type of preprocessing to be done")
args = vars(ap.parse_args())

image = cv2.imread('C:/Users/Admin/Desktop/Project/Capture1.png',0)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, image)
text = pytesseract.image_to_string(Image.open(filename))
x=len(text)
for i in range(x):
    if text[i]=='-':
        a.append(text[0:i])
        a.append(text[i+1:x+1])
        result=int(a[0])-int(a[1])
    elif text[i]=='+':
        a.append(text[0:i])
        a.append(text[i + 1:x + 1])
        result = int(a[0]) + int(a[1])
    elif text[i]=='/':
        a.append(text[0:i])
        a.append(text[i + 1:x + 1])
        d=int(a[1])
        if d==0:
            result="Invalid"
            break
        else:
            result = int(a[0]) / int(a[1])
    elif text[i]=='*':
        a.append(text[0:i])
        a.append(text[i + 1:x + 1])
        result = int(a[0]) * int(a[1])
print(a)
"""if z=='+':
    result=int(a[0])+int(a[1])
elif z=='-':
    result=int(a[0])-int(a[1])
elif z=='/':
    result=int(a[0])/int(a[1])
elif z=='*':
    result=int(a[0])*int(a[1])"""
print(result)
os.remove(filename)
cv2.imshow("Output", image)
cv2.waitKey(0)
