# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("lena_gray.png")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

#Borde por recorrido horizontal
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        pixel_izquierda = imagen[i-1,j]*1
        pixel_arrriba = imagen[i,j-1]*1
        pixel_derecha = imagen[i+1,j]*1
        pixel_abajo = imagen[i,j+1]*1
        pixel_actual = imagen[i,j]*1

        color = -1*pixel_izquierda-pixel_abajo+4*pixel_actual-pixel_derecha-pixel_abajo  
        color = abs(color)

        if (color > 255):
            color=255

        temp[i,j] = color

plt.title("Detección de borde gradiente")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()
