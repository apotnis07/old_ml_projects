import cv2,time

camera_port = 0

camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

a = 1

while True:
    a = a + 1
    check,frame=camera.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
camera.release(1)
cv2.destroyAllWindows()

