'''Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100'''

lista_enteros=[1,2,3,4,99,101,110,120]
def mayor_100(lista_enteros):
    contador=0
    x=0
    for numero in lista_enteros:
        if lista_enteros[x]>100:
            contador=contador+1
        x=x+1
    return contador

numeros_mayor100 = mayor_100(lista_enteros)
print("Lista de numeros ingresados:",lista_enteros)
print("Lista de numero mayores a 100:",numeros_mayor100)
