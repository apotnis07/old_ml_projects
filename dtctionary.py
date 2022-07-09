
import speech_recognition as sr
AUDIO_FILE=("3add.wav")

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google SR")
a=r.recognize_google(audio)
print(a)
dict={}
#print(dict)
print(len(a))
for i in range(len(a)):
    #a[0:i+1]
    if(a[i]=='+'):
        j=i
        print(a[0:i])
        print(a[i+1:len(a)])

dict['op'] = a[0:j-1]
dict['op1'] = a[j+1:len(a)]
print(dict)
a=1
x=dict['op']
x=int(x)
y=dict['op1']
y=int(y)
sum=x+y
print(sum)
