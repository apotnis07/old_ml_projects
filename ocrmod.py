# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
a=[]
sum=0
import string
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())
# load the example image and convert it to grayscale
image = cv2.imread('C:/Users/Admin/Desktop/Project/Test1.jpg',0)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
#1if args["preprocess"] == "thresh":
 #2   image = cv2.threshold(image, 0, 255,
 # 3                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
#4elif args["preprocess"] == "blur":
# 5   image = cv2.medianBlur(image, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, image)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

text = pytesseract.image_to_string(Image.open(filename))
x=len(text)
for i in range(x):
    if text[i]=='-':

        a.append(text[0:i])

        a.append(text[i+1:x+1])
print(a)
result=int(a[0])-int(a[1])
print(result)
os.remove(filename)
#print(text)

# show the output images
#cv2.imshow("Image", image)
cv2.imshow("Output", image)
cv2.waitKey(0)
