import cv2
import numpy as np
import random

def Kenar_Ekleme(cerceve):
    gri_cevirme = cv2.cvtColor(cerceve, cv2.COLOR_BGR2GRAY)

    esik_deger = 100

    _, beyaz_maskeleme = cv2.threshold(gri_cevirme, esik_deger, 255, cv2.THRESH_BINARY)


    cont, _ = cv2.findContours(beyaz_maskeleme, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cont:
        Alan = cv2.contourArea(contour)
        if Alan > 100:

            sınır_rengi = (255, 0, 0)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(cerceve_, (x, y), (x + w, y + h), sınır_rengi, 5)

    return cerceve_

kamera= 'http://192.168.77.88:4747/video'

cv2.imshow('Objects Without Border & Gray Image', kamera)
cv2.waitKey()
while True:
    ret, cerceve_ = kamera.read()


    if not ret:
        break


    dıs_cerceve = Kenar_Ekleme(cerceve_)

    cv2.imshow('cerceveli resim', dıs_cerceve)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()
