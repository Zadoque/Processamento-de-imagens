import cv2 as cv

image = cv.imread('a.png')

if image is not None:
    
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('Falha ao carregar a imagem')