import cv2 as cv

image = cv.imread('exemplo.png')


if image is not None:
    blue, green, red = cv.split(image)
    cv.imshow('canal azul',blue)
    cv.imshow('canal verde',green)
    cv.imshow('canal vermelho',red)
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print('Imagem não carregada com sucesso')