nombre= input("Dime tu nombre: ")
ventas = input("Dime tus ventas (en dolares): ")
ventas = int(ventas)
comision = round((ventas*13)/100,2)

print(f"Gracias por tu aporte {nombre}, debido a tus ventas de ${ventas}, tu comision es ${comision}. Felicidades!")