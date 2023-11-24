import random

valores=[i+1 for i in range(13)]
palos=['oro', 'copa', 'espada', 'basto']
naipes=[(valor, palo) for valor in valores for palo in palos]

jugador1=random.choices(naipes, k=3)