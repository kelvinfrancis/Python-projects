"""Confeccionar una aplicación que muestre una presentación en pantalla
del programa. Solicite la carga de dos valores y nos muestre la suma.
Mostrar finalmente un mensaje de despedida del programa."""

def mensaje(mensaje):
    print('******************************************************************')
    print(mensaje)
    print('******************************************************************')

def suma():
    v1 = int(input('Ingrese un numero entero: '))
    v2 = int(input('Ingrese otro numero entero: '))
    print(f'La suma de los valores ingresados es {v1 + v2}')


# Bloque principal
mensaje_inicio = input('Ingrese un mensaje de bienvenida: ')
mensaje_fin = input('Ingrese un mensaje de despedida: ')
mensaje(mensaje_inicio)
suma()
mensaje(mensaje_fin)
