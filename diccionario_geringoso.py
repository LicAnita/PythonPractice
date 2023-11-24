def traducir(cadena):
    cadepenapa = ''
    vocales = 'aeiou'
    diccionario = {}
    # Separo las palabras
    for palabra in cadena:
        # busco cada letra
        for c in palabra:
            # identifico las vocales
            cadepenapa += c

            if c in vocales:

                # agrego la p
                cadepenapa += 'p'
                # repito la vocal
                cadepenapa += c
        # almaceno la palabra nueva con la original como key en el objeto
        diccionario[palabra] = cadepenapa
        # vacio la variable porque sino me almacena todo junto
        cadepenapa = ''
    print(diccionario)


geringoso = ['banana', 'manzana', 'mandarina']
traducir(geringoso)
