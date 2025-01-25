import cv2 as cv
import numpy as np

diamond_image = cv.imread('diamond.png')
diamond_template = cv.imread('diamond_template.png', 0)

if diamond_image is not None and diamond_template is not None:
    #Precisamos da imagem em preto e branco:
    
    gray_diam = cv.cvtColor(diamond_image, cv.COLOR_BGR2GRAY)
    #Agora armazenamos a altura (h) e a largura (w):
    h, w = diamond_template.shape[::-1]
    #Realizando busca:
    res = cv.matchTemplate(gray_diam, diamond_template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(diamond_image, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 1)

    cv.imshow('Resultado da busca', diamond_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('Alguma  imagem não foi carregada com sucesso')