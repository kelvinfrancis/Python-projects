'''Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.'''

lista_enteros=[1,2,7,8,10]
x=0
print("Lita de numeros ingresada:",lista_enteros)
print("Elementos mayores o iguales a 7:")
while x<len(lista_enteros):
    if lista_enteros[x]>=7:
        print(lista_enteros[x])
    x=x+1
