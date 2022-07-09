from PIL import Image
import pytesseract
import argparse
import cv2
import os
import string
import speech_recognition as sr

loop = True
while loop:
    print("1.Use image recognition")
    print("2.Use voice recognition")
    print("3.Exit")
    ch = int(input("Enter the choice:"))
    if ch == 1:
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


    elif ch == 2:
        AUDIO_FILE = ("minus.wav")
        print("Enter any no of operands as long as the operations to be performed on them is the same")
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
        dict={}

        len = len(m)
        countp = 0
        countm = 0

        countd = 0
        result = 0
        i = 0
        count1 = 0
        count2 = 0

        count4 = 0


        def check(m, i):
            z = i

            for i in range(z, len):
                if (m[i] == '+'):
                    global count1
                    count1 += 1
                    x = m.count('+')
                    global countp
                    countp += 1
                    r = i

                    dict[countp] = m[z:r - 1]

                    countp += 1
                    dict[countp] = m[r + 1:len]

                    countp -= 1

                    if count1 == x:
                        # Add opr name at the end of dict and read it outside check and perform
                        dict.update({'Num':countp+1})
                        dict.update({'op': 'plus'})
                        return dict
                    else:
                        return check(m, r + 1)

                if m[i]=='-' :
                    global count2
                    count2+=1
                    y=m.count('-')
                    global countm
                    countm+=1
                    r=i

                    dict[countm]=m[z:r-1]

                    countm+=1
                    dict[countm]=m[r+1:len]

                    countm-=1

                    if count2==y:
                        #dict.update({'Num': countm + 1})
                        #dict.update({'op': 'minus'})
                        return dict
                    else:
                        return check(m,r+1)



        dict = check(m, 0)

        # print(result)
        result = 0
        print(dict)
        """if dict['op'] == 'plus':
            x = dict['Num']
            for i in range(x):
                result = result + int(dict[i + 1])
        if dict['op'] == 'minus':
            x = dict['Num']
            for i in range(x):
                result = int(dict[i]) - int(dict[i+1])"""

        #print(result)


        print(dict)

    elif (ch==3):
        break

    else:
        print("Invalid Choice")










