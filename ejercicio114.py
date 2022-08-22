"""Desarrollar un programa con dos funciones.
La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
LLamar desde el bloque del programa principal a ambas funciones."""


def cuadrado_de_un_numero():
    print('-----------Cuadrado de un numero-------------------')
    num = int(input('Ingrese un numero entero: '))
    print(f'El cuadrado del numero es {num * num} \n')


def producto_de_un_numero():
    print('---------------Producto de dos numeros-----------------')
    v1 = float(input('Ingrese un numero: '))
    v2 = float(input('Ingrese otro numero: '))
    print(f'El producto de los numeros ingresados es: {v1 * v2}')


# Bloque principal
cuadrado_de_un_numero()
producto_de_un_numero()
