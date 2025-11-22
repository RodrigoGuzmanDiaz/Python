nombre = ['Rodrigo', 'Alberto', 'Michael', 'Freddy']
edades= [25, 37, 43]
ciudades = ['Madrid', 'Buenos Aires', 'Mixco']
nueva_lista = list(zip(nombre, edades, ciudades))

for nombre, edades, ciudades in nueva_lista:
    print(f'{nombre} tiene {edades} anios y vive en {ciudades}')