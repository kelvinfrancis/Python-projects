"""Desarrollar una funcion que reciba un string como parametro y
nos muestre la cantidad de vocales. Llamarla desde el bloque principal
del programa 3 veces con string distintos."""

def detectar_vocales(palabra):
    vocales = 0
    for x in range(len(palabra)):
        if palabra[x] == 'a' or palabra[x] == 'e' or palabra[x] == 'i' or palabra[x] == 'o' or palabra[x] == 'u':
            vocales += 1

    print(f'La cantidad de vocales es: {vocales}')

print('*************** Contador de vocales *******************')
for x in range(3):
    palabra = input('Ingrese una palabra: ')
    detectar_vocales(palabra)