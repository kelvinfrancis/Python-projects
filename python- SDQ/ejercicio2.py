'''Crear una lista de 5 colores, luego preguntar
al usuario que introduzca un color, almacenarlo en
una variable. Luego imprime si el color esta en la lista
o no '''

color = input('Hola, escribe un color: ').lower()
colores = ['azul', 'verde', 'rojo', 'amarillo', 'negro']

if color in colores:
    print("El color esta en la lista.")
else:
    print('El color NO esta en la lista.')