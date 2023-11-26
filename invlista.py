#opcion Pro 1

def invertir_lista_pro(lista):
    invertida = []
    for e in reversed(lista):
        invertida.append(e)
    return invertida

#opcion pro 2

def invertir_lista_pro2(lista):
    lista=lista[::-1]
    return lista


#opcion manual

def invertir_lista(lista):
    l=len(lista)
    invertida=[]
    while l>0:
        l-=1
        invertida.append(lista[l])
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista_pro([6, 7, 8, 9, 10]))
print(invertir_lista_pro2([11, 12, 13 ,14 ,15]))

