import cv2 as cv

image = cv.imread('exemplo.png')



if image is not None:
    gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('imagem em preto e branco', gray_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')