import cv2
import numpy as np


camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break


    hsvDonusum = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    DusukAralık_red = np.array([160, 100, 100])
    YuksekAralık = np.array([179, 255, 255])


    mask = cv2.inRange(hsvDonusum, DusukAralık_red, YuksekAralık)


    res = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('Kırmızı', res)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
