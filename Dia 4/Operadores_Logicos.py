# Ejemplos de operadores lógicos en Python, de fácil a más complejos

# Ejemplo sencillo: operador AND (and)
mi_bool = True and True
print(mi_bool)  # True

mi_bool = True and False
print(mi_bool)  # False

# Ejemplo con comparación usando AND
mi_bool = (10 > 5) and (8 == 8)
print(mi_bool)  # True

mi_bool = (10 == 5) and (8 == 8)
print(mi_bool)  # False

# Operador OR (or) básico
mi_bool = True or False
print(mi_bool)  # True

mi_bool = False or False
print(mi_bool)  # False

# Ejemplo con comparación usando OR
mi_bool = (5 > 10) or (8 == 8)
print(mi_bool)  # True

mi_bool = (5 > 10) or (8 != 8)
print(mi_bool)  # False

# Operador NOT (not) básico
mi_bool = not True
print(mi_bool)  # False

mi_bool = not False
print(mi_bool)  # True

# Ejemplos con strings y el operador 'in' (devuelve booleano)
texto = "hola mundo"

print('hola' in texto)  # True (porque "hola" está dentro de texto)
print('adios' in texto) # False (porque "adios" no está en texto)

# Combinando operadores lógicos con strings
mi_bool = ('a' in 'manzana') and (10 > 5)
print(mi_bool)  # True

mi_bool = ('x' in 'manzana') or (5 > 10)
print(mi_bool)  # False

mi_bool = not ('z' in 'manzana')
print(mi_bool)  # True

# Ejemplo más complejo combinando varias condiciones
edad = 20
tiene_licencia = True
tiene_multa = False

puede_conducir = (edad >= 18) and tiene_licencia and not tiene_multa
print(puede_conducir)  # True porque cumple todas las condiciones
