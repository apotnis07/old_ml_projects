import cv2,time
camera_port = 0

camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

check,frame = camera.read()

print(check)

print(frame)

time.sleep(3)

cv2.imshow("Capture", frame)

cv2.waitKey(0)

camera.release()

cv2.destroyAllWindows()