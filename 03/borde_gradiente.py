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
for i in range(0, largo-1):
    for j in range(0, ancho-1):
        pixel_derecha = imagen[i+1,j]*1
        pixel_arriba = imagen[i,j+1]*1
        pixel_actual = imagen[i,j]*1

        pixel_der = abs(pixel_derecha - pixel_actual)
        pixel_arr = abs(pixel_arriba - pixel_actual)

        color = 0.5 * math.sqrt(pixel_der**2 + pixel_arr**2)
            
        temp[i,j] = color

plt.title("Detección de borde gradiente")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()