"""Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El 
segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos."""

lista=[]
elementos=int(input("Ingrese la cantidad de elemntos en la lista: "))
sublista=int(input("Ingrese la cantidad de elementos de las sublistas: "))
for x in range(elementos):
    lista.append([])
    for k in range(sublista):
        valor=int(input("Ingrese un valor: "))
        lista[x].append(valor)
sumatotal=0
for x in range(len(lista)):
    for k in range(sublista):
        sumatotal=sumatotal+lista[x][k]
print("Lista completa")
print(lista)
print("La suma total de los valores es:",sumatotal)