import cv2 as cv 
import numpy as np

image = cv.imread('exemplo.png')

if image is not None:


    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')