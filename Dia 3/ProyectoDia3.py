texto = input("ingresa un texto: ")
texto = texto.lower()

letra1 = input("ingresa la letra 1: ")
letra2 = input("ingresa la letra 2: ")
letra3 = input("ingresa la letra 3: ")

#cuando la cantidad de palabras usando la funcion count() con el parametros de la letra que se pide en los input
cantidadLetra1= texto.count(letra1)
cantidadLetra2= texto.count(letra2)
cantidadLetra3= texto.count(letra3)

#convierto el texto en una lista
textoEnlista = texto.split(" ")

#cuento la cantidad de palabras usando el metodo len() para contar el numero de elementos de la lista
cantidadPalabras = len(textoEnlista)

#decur primera y ultima letra del texto usando indice de 0 para la primera letra y el -1 para la ultima
primeraLetra = texto[0]
ultimaLetra = texto[-1]

#se invierte el orden de las palabras usando factores
textoInvertido = textoEnlista[::-1]
textoInvertido = ' '.join(textoInvertido)
aparecePython = ("python" in texto)

print(f"""
La cantidad de veces que aparece la letra {letra1} es {cantidadLetra1}
La cantidad de veces que aparece la letra {letra2} es {cantidadLetra2}
La cantidad de veces que aparece la letra {letra3} es {cantidadLetra3}
La cantidad de palabras son: {cantidadPalabras}
La primera letra es {primeraLetra}
La ultima letra es {ultimaLetra}
El orden inverso de la palabra es {textoInvertido}
Aparece python en el texto? {aparecePython}
""")