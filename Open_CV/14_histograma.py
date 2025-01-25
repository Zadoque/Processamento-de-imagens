import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

image = cv.imread('raio_x.jpg', 0)

if image is not None:

    image_hist = cv.calcHist([image], [0], None, [256], [0, 256] )
    plt.subplot(231),plt.imshow(image, 'gray')
    plt.subplot(234),plt.plot(image_hist)
    

    equalized_hist = cv.equalizeHist(image)
    image_hist_equal = cv.calcHist([equalized_hist], [0], None, [256], [0, 256] )

    plt.subplot(232),plt.imshow(equalized_hist, 'gray')
    plt.subplot(235),plt.plot(image_hist_equal)
    

    #Clahe
    clahe =cv.createCLAHE(clipLimit=2, tileGridSize= (8,8))
    cli = clahe.apply(image)
    cl_equal = cv.calcHist([cli],  [0], None, [256], [0, 256])
    plt.subplot(233),plt.imshow(cli, 'gray')
    plt.subplot(236),plt.plot(cl_equal)
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print('Deu merda, a imagem não foi carregada')