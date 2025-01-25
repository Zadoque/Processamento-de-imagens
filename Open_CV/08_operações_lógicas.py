import cv2 as cv 
import numpy as np

image1 = cv.imread('exemplo.png')
image2 = cv.imread('exemplo2.png')
if image1 is not None and image2 is not None:
    #as duas imagens devem ter o mesmo tamanho para as operações 
    image1 = cv.resize(image1, (500,500))
    image2 = cv.resize(image2,(500,500))
    cv.imshow('imagem 1', image1)
    cv.imshow('imagem 2', image2)

    #Operação and
    and_image = cv.bitwise_and(image1, image2)

    #Operação or

    or_image = cv.bitwise_or(image1, image2)

    #operação Not
    not_image = cv.bitwise_not(image1)

    #Operação XOR

    xor_image = cv.bitwise_xor(image1, image2)

    ## Você pode ver o resultado de cada operação usando o comando cv.imshow que vc já
<<<<<<< HEAD
    #aprendeu!

=======
    #aprendeu! 
    cv.imshow('imagem 2', or_image)
>>>>>>> Dev
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')