import cv2 as cv
import numpy as np
image = cv.imread('exemplo2.png')

if image is not None:
    #para usar o thresholding geralmente se usa uma imagem em preto e branco
    image = cv.resize(image, (500, 500))
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #Aplicando um thresholding simples

    rest, thresh_simple = cv.threshold(gray_image, 200, 255, cv.THRESH_BINARY)

    #mostrando thresholding simples:

    cv.imshow('simples thresholding', thresh_simple)


    #aplicando thresholding que se adapta as características da imagem:

    adaptive_thresh = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 8)
    cv.imshow('thresholding Adapitavél ', adaptive_thresh)

    #Aplicando o thresholding automático que adapta os valoraes 

    ret, otsu_thresh = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    cv.imshow('thresholding Otsu ', otsu_thresh)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')