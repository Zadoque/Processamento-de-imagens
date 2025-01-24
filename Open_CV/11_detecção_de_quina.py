import cv2 as cv
import numpy as np
image = cv.imread('exemplo.png', cv.IMREAD_GRAYSCALE)  
#Precisamos da   imagem em preto e branco

if image is not None:
    image = cv.resize(image, (500,500))
    laplacian = cv.Laplacian(image, cv.CV_64F)
    cv.imshow('Detequição de borda de Laplace', laplacian)

    sobelx = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(image, cv.CV_64F, 0 ,1, ksize=5)

    cv.imshow('Detequição de borda sobelx', sobelx)
    cv.imshow('Detequição de borda sobely', sobely)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')