import cv2 as cv
import numpy as np
image = cv.imread('exemplo.png', cv.IMREAD_GRAYSCALE)  
#Precisamos da   imagem em preto e branco

if image is not None:
   
    image = cv.resize(image, (500, 500)) #Só para vermos melhor o que está acontecendo
    _,binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)

    #Agora precisamos de um Kernel
    
    kernel = np.ones((5,5), np.uint8)

    #Aplicando erosão
    eroded_image = cv.erode(binary_image, kernel, iterations=1)

    cv.imshow('Imagem  erodida', eroded_image)


    #aplicando dilatação:

    dilated_image = cv.dilate(binary_image, kernel, iterations=1)

    cv.imshow('Imagem dilatada', dilated_image)

    #aplicando abertura na imagem:
    opened_image = cv.morphologyEx(binary_image, cv.MORPH_OPEN, kernel)
    cv.imshow('Imagem com abertura', opened_image)

    #aplicando fechamento
    closed_image = cv.morphologyEx(binary_image,cv.MORPH_CLOSE, kernel)
    cv.imshow('Imagem com fechamento', closed_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')