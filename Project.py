from PIL import Image
import pytesseract
import argparse
import cv2
import os
import string
import speech_recognition as sr

loop=True
while loop:
    print("1.Use image recognition")
    print("2.Use voice recognition")
    print("3.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        a = []
        z = ''
        result = 0

        image = cv2.imread('C:/Users/Admin/Desktop/Project/Capture1.png', 0)

        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, image)
        text = pytesseract.image_to_string(Image.open(filename))
        x = len(text)
        for i in range(x):
            if text[i] == '-':
                a.append(text[0:i])
                a.append(text[i + 1:x + 1])
                result = int(a[0]) - int(a[1])
            elif text[i] == '+':
                a.append(text[0:i])
                a.append(text[i + 1:x + 1])
                result = int(a[0]) + int(a[1])
            elif text[i] == '/':
                a.append(text[0:i])
                a.append(text[i + 1:x + 1])
                d = int(a[1])
                if d == 0:
                    result = "Invalid"
                    break
                else:
                    result = int(a[0]) / int(a[1])
            elif text[i] == '*':
                a.append(text[0:i])
                a.append(text[i + 1:x + 1])
                result = int(a[0]) * int(a[1])
        print(a)

        print(result)
        os.remove(filename)
        cv2.imshow("Output", image)
        cv2.waitKey(0)


    elif ch==2:
        AUDIO_FILE = ("b.wav")

        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        try:
            print("audio file contains " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError:
            print("Couldn't get the results from Google SR")
        m = r.recognize_google(audio)
        print(m)
        dict = {}
        len = len(m)
        count = 0
        i = 0
        count1 = 0


        def check(m, i):
            z = i
            print("i=", i)
            for i in range(z, len):
                if m[i] == '+':
                    global count1
                    count1 += 1
                    m.count('+')
                    global count
                    count += 1
                    r = i
                    print("i=", i)
                    dict[count] = m[z:r - 1]
                    # print("z=",z)
                    # print("r-1=",r-1)
                    print("Printing dict[count]", dict[count])
                    count += 1
                    dict[count] = m[r + 1:len]
                    print("Printing dict[count1]", dict[count])
                    count -= 1
                    print(dict)
                    if count1 == 2:
                        return dict
                    else:
                        return check(m, r + 1)


        dict = check(m, 0)
        dict['op'] = m[0:j - 1]
        dict['op1'] = m[j + 1:len(m)]
        print(dict)
        m = 1
        l = dict['op']
        l = int(l)
        r = dict['op1']
        r = int(r)
        sum = l + r
        print(sum)

    else:
        print("Invalid Choice")