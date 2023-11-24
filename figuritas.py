import random
import numpy as np
import matplotlib.pyplot as plt


def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album


def comprar_paquete(album, figus_total):
    for i in range(5):
        figurita = random.randint(0, figus_total-1)
        album[figurita] += 1
    return album


def album_incompleto(album):
    flag = 0 in album
    return flag


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    contador = 0
    while album_incompleto(album) == True:
        album = comprar_paquete(album, figus_total)
        contador += 1
    return contador


def cuantos_paquetes(n_repeticiones, figus_total):
    l = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    m = [i for i in l if i <= 850]
    afortunado = len(m)/n_repeticiones
    promedio = np.mean(l)
    resultado = f'El promedio para llenar el álbum es de {promedio} paquetes de figuritas y la probabilidad de llenarlo con 850 paquetes o menos es de {afortunado}'
    return resultado

#How many packs of figurines do I need to fill the album given the total number of figurines? And what are the odds that I will fill it with x amount of packs? 
print(cuantos_paquetes(100, 670))
