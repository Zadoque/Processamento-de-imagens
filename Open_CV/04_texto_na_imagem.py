import cv2 as cv

image = cv.imread('a.png')

if image is not None:
    cv.putText(image, 'Exemplo de texto na imagem', (20,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0), 4)
    cv.imshow('Imagem com texto', image)


    cv.waitKey(0)
    cv.destroyAllWindows()
    
else:
    print('Falha ao carregar a imagem')