palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)


lista = [letra for letra in 'python']
print(lista)

millas = [1, 2, 3]
lista = [km * 1609 for km in millas]
print(lista)