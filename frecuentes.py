# ===========================
#        EJERCICIO 2
# ===========================

import csv


def leer_archivo(ruta):
    '''
    Generates a list from a comma separated files (csv)
    '''
    lista = []
    with open(ruta, "rt", encoding='utf8') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                lista_de_palabras = row[0].split()
                for palabra in lista_de_palabras:
                    for letra in palabra:
                        letra = letra.lower()
                        if letra in 'áéíóú':  # change accented letters.
                            reemplazo = (('á', 'a'), ('é', 'e'),
                                         ('í', 'i'), ('ó', 'o'), ('ú', 'u'))
                            for acento in reemplazo:
                                if letra == acento[0]:
                                    letra = acento[1]
                        lista.append(letra)
            else:
                continue  # no empty lines
    return lista


def listar_frecuentes(ruta):
    '''
    Makes a list of tuple with characters and frecuency.
    '''
    lista = leer_archivo(ruta).copy()
    contador = 0  
    lista_frecuentes = []  
    letras = [] 
    for i in lista:
        if i not in letras:
            conteo = lista.count(i)
            letras.append(i)
            if conteo > contador:
                frecuente = i
                cantidad = conteo
                tupla = frecuente, cantidad
                lista_frecuentes.append(tupla)

    return lista_frecuentes


def buscar_maximo(lista):
    '''
    Finds mode character
    '''
    max = lista[0][1] 
    letra = lista[0][0]
    moda = letra, max
    for tupla in lista:
        valor = tupla[1] 
        if valor > max:  
            max = valor
            letra = tupla[0]
            moda = letra, max
    return moda


def ordenar_frecuentes(lista):
    '''
    Order tuples from minor to major.
    '''
    nueva = listar_frecuentes(lista).copy()  
    ordenada = []
    while len(nueva) != 0:
        maximo = buscar_maximo(nueva)[1]
        for i, tupla in enumerate(nueva):
            if tupla[1] == maximo:
                ordenada.append(tupla)
                nueva.pop(i)

    return ordenada


def buscar_frecuentes(lista, N):
    '''
    Takes a list with characters and returns mode character.
    '''
    frecuentes = ordenar_frecuentes(lista)
    nueva = []
    cantidad = len(frecuentes)
    if N > cantidad:  # error checking, no more values than characters.
        raise ValueError(
            f'¡Poné lo que se te cante nomás...!, tenes que poner un N menor a la cantidad de valores únicos. Podes poner entre 1 y {cantidad} ')
    for i, tupla in enumerate(frecuentes):
        if i < N:
            nueva.append(tupla)

    return nueva


def funcion_principal(argv):
    if len(argv) != 3:
        raise SystemExit(
            f'¡Poné lo que se te cante nomás...!, tenes que poner: {sys.argv[0]}, ruta del archivo txt, cantidad de letras a buscar y nada mas.')
    nueva = buscar_frecuentes(argv[1], argv[2])
    return nueva

'''
Takes csv file from console
'''
if __name__ == '__main__':
    import sys
    print(funcion_principal(sys.argv))
