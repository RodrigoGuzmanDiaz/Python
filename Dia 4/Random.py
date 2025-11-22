from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = uniform(1, 2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['rojo', 'azul', 'verde', 'amarillo']
color_aletorio = choice(colores)
print(color_aletorio)

numeros = list(range(10, 110, 10))
shuffle(numeros)
print(numeros)