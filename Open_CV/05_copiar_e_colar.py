import cv2 as cv

image = cv.imread('exemplo.png')

x,y,w,h = 100,100,200,200

if image is not None:
    imagem_cortada = image[y:y+h,x:x+w]
    cv.imshow('imagem copiada', imagem_cortada)
    parte_copiada = image[50:150,50:200].copy()
    image[150:250,150:300] = parte_copiada
    cv.imshow('imagem modificada', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')