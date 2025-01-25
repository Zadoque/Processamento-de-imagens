import cv2 as cv
import numpy as np
image = cv.imread('maze.png')  
#Precisamos da   imagem em preto e branco

if image is not None:
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
   #Detecção de quinas simples:
    quinas_simples = cv.goodFeaturesToTrack(gray_img,50,0.01, 10 )
    quinas_simples = np.int_(quinas_simples)
    for i in quinas_simples:
        x, y = i.ravel()
        cv.circle(image, (x,y), 2, 255, -1)

    cv.imshow('Detequição simples', image)

   #Detecção de quinas harris:
    gray_img = np.float32(gray_img)
    harris = cv.cornerHarris(gray_img, 2, 3, 0.04)

    image[harris>0.1*harris.max()] = [0, 0, 255]

    cv.imshow('Detequição Harris', image)
    #Detecção de quinas harris com dilatação:

    dilated_harris = cv.dilate(harris, None)

    image[dilated_harris>0.1 * dilated_harris.max()] = [0,255,0]

    cv.imshow('Detequição harris após dilatação', image)


    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('imagem não carregada com sucesso')