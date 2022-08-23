"""Confeccionar una función que reciba tres enteros y nos muestre el
mayor de ellos. La carga de los valores hacerlo por teclado."""


def numero_mayor(a, b, c):
    print('El valor mayor de los tres numeros es: ')
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)


def carga_valores():
    print('**** Calcular el valor mayor de 3 numeros enteros  **** \n')
    v1 = int(input('Ingrese el primer valor entero: '))
    v2 = int(input('Ingrese el segundo valor entero: '))
    v3 = int(input('Ingrese el tercer valor entero: '))
    numero_mayor(v1, v2, v3)


# Bloque principal
carga_valores()
