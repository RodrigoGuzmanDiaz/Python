lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(f'El nombre {nombre} SI comienza con L')
    else:
        print(f'El nombre {nombre} NO comienza con L')


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_total = 0
for valor in lista_numeros:
    suma_total = suma_total + valor

print(f'La suma total de los numeros es: {suma_total}')

for a in (1,2,3):
    print(a)

#iterando diccionario con keys()
diccionario = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for valor in diccionario:
    print(valor)

#iterando diccionario con values()
diccionario = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for valor in diccionario.values():
    print(valor)

#iterando diccionario con items()
diccionario = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in diccionario.items():
    print(item)