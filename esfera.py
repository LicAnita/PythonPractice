import math

#Ingreso el radio mediante un input y lo hago float para poder usarlo en la fórmula.
radio = float(input('Ingrese el radio de la esfera: '))
#Si no pongo el denominador en float, me redondea a valor 1 en lugar de 1,66.
volumen = (4/float(3) * math.pi * math.pow(radio, 3))
print(volumen)
