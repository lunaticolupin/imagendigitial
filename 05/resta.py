import cv2 as cv
import numpy as np

imagen1 = cv.imread('foto1.jpg')
imagen2 = cv.imread('foto2.jpg')

cv.imshow('Imagen A',imagen1)
cv.waitKey(0)
cv.imshow('Imagen B',imagen2)
cv.waitKey(0)
cv.destroyAllWindows()

temp = np.copy(imagen1)
largo = len(temp)
ancho = len(temp[0])

for i in range(1, largo):
    color = [0,0,0]
    for j in range(1, ancho): 
        color[0] = imagen1[i,j,0]*1 - imagen2[i,j,0]*1
        color[1] = imagen1[i,j,1]*1 - imagen2[i,j,1]*1
        color[2] = imagen1[i,j,2]*1 - imagen2[i,j,2]*1

        if (color[0]<0):
            color[0]=0

        if (color[1]<0):
            color[1]=0

        if (color[2]<0):
            color[2]=0
            
        temp[i,j,0] = color[0]
        temp[i,j,1] = color[1]
        temp[i,j,2] = color[2]

cv.imshow('Suma de Imagenes',temp)
cv.waitKey(0)
cv.destroyAllWindows()

nombre = "operador_xor_2.png"
cv.imwrite(nombre, temp)

