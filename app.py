import time
for i in range(0,100):
    time.sleep(1)
    time.strftime('%I:%M:%S %p %Z')
    if (time.strftime('%I:%M:%S') == '12:00:30'):
        print("Good night")
        break