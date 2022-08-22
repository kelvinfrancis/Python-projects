"""Desarrollar un programa que solicite la carga de tres valores y
muestre el menor. Desde el bloque principal del programa llamar 2 veces
a dicha función (sin utilizar una estructura repetitiva)"""


def cual_es_menor():
    print('---Ingrese 3 valores---')
    a = int(input('Ingrese el primer valor: '))
    b = int(input('Ingrese el segundo valor: '))
    c = int(input('Ingrese el tercer valor: '))

    if a < b and a < c:
        print(f'El menor de los numeros es {a}')
    elif b < a and b < c:
        print(f'El menor de los numeros es {b}')
    else:
        print(f'El menor de los numeros es {c}')


# Bloque principal
cual_es_menor()
cual_es_menor()
