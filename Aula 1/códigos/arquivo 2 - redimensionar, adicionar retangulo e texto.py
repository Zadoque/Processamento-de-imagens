#Primeiro importamos a biblioteca OpenCV
import cv2 as cv

image =  cv.imread('a.PNG') #lendo a imagem

if image is not None: #verifica se a imagem foi lida corretamente
    
    image_redimensionada = cv.resize(image,(500,500))#redimensiona a imagem
    cv.imshow('primeira imagem',image) #mostrar a imagem em uma nova janela

    cv.imshow('imagem Redimensionada',image_redimensionada) #mostrar a imagem em uma nova janela

    cv.imwrite('a_redimensionada.PNG', image_redimensionada) # salva a imagem redimensionada
    #na mesma pasta do código
    5
    #As duas linhas abaixo são para esperar qualquer tecla para fechar as janelas
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Falha ao carregar imagem")


