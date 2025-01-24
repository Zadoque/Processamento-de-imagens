import cv2 as cv


image = cv.imread('exemplo.png')

if image is not None:
    cv.rectangle(image, (50,50),(200,200), (0,255,0), 3)
    cv.imshow('imagem com retângulo', image)


    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print('Falha ao carregar a imagem')