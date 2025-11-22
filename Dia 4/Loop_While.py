vidas = 5

while vidas > 0:
    if  vidas == 1:
        print(f"Tengo {vidas} vida restante")
        vidas-=1
    else:
        print(f"Tengo {vidas} vidas restantes")
        vidas -= 1
else:
    print("Ya no tengo vidas")


respuesta = 's'
while respuesta == 's':
    pass
print('hola')


nombre = input("Escribe tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

nombre = input("Escribe tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)