import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_hesapla(goruntu):
    histogram = np.zeros(256)

    for piksel in np.nditer(goruntu):
        histogram[piksel] += 1

    return histogram

goruntu = cv2.imread("images.jpeg", 0)

histogram = histogram_hesapla(goruntu)

plt.plot(histogram, color='black')
plt.xlabel('Piksel Değerleri')
plt.ylabel('Piksel Sayısı')
plt.show()