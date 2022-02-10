"""Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal."""

lista=[[1,2,3,4,5],[1,2,3,4,5]]
for x in range(len(lista)):
    suma=0
    for k in range(len(lista[x])):
        suma=suma+lista[x][k]
print("La suma total es:",suma)


    