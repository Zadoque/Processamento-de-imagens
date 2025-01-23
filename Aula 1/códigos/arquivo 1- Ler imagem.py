#Primeiro importamos a biblioteca OpenCV
import cv2 as cv

image =  cv.imread('a.PNG') #lendo a imagem

if image is not None: #verifica se a imagem foi lida corretamente
    cv.imshow('primeira imagem',image) #mostrar a imagem em uma nova janela
    #As duas linhas abaixo são para esperar qualquer tecla para fechar as janelas
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Falha ao carregar imagem")


