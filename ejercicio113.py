"""Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma."""

def carga_suma():
    v1 = int(input('Ingrese un numero entero: '))
    v2 = int(input('Ingrese un numero entero: '))
    suma = v1 + v2
    print(f'La suma de los valores es {suma}')

def separacion():
    print('***************************************************')


for x in range(5):
    carga_suma()
    separacion()