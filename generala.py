import random


def tirar(guardados):
#Rolls a dice five times.
    tirada = []
    for i in range(5-guardados):
        tirada.append(random.randint(1, 6))
    return tirada

#takes the repeatest value 
def es_generala(tirada):
    dados = []
    maximo = 0

    for d in tirada:
        tupla = d, tirada.count(d)

        dados.append(tupla)
        if tirada.count(d) > maximo:
            maximo = tirada.count(d)
            guardado = d, maximo

    retorno = tirada, guardado

    return retorno

#rolls again the not saved dice.
def es_generala_pro(tirada, suerte, guardados):
    dados = []
    maximo = 1
    mas = suerte in tirada
    guardado = suerte, guardados

    if mas == True:
        guardado = suerte, tirada.count(suerte)+guardados

    else:
        for d in tirada:
            tupla = d, tirada.count(d)
            dados.append(tupla)

            if tupla[1] > guardados:
                maximo = tupla[1]
                guardado = d, maximo

    return guardado


#calculates the probability
def prob_generala(N):
    generala = 0
    for i in range(N):
        mano1 = es_generala(tirar(0))
        guardados1 = mano1[1][1]
        suerte = mano1[1][0]

        print(mano1)
        if mano1[1][1] == 5:
            print('Sos un crack, metiste generala, FENÓMENO!!')

        mano2 = es_generala_pro(tirar(guardados1), suerte, guardados1)
        guardados2 = mano2[1]
        print(mano2)

        if mano2[1] == 5:
            print('Sos un crack, metiste generala, FENÓMENO!!')

        mano3 = es_generala_pro(tirar(guardados2), suerte, guardados2)

        if mano3[1] < 5:
            print(mano3, 'que mala suerte, che!')

        else:
            print(mano3)
            print('Sos un crack, metiste generala, FENÓMENO!!')
            generala += 1

    probabilidad = generala/N
    return probabilidad


print('Tu probabilidad fue de... ', prob_generala(1000))
