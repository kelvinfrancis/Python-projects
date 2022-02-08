"""Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, 
luego ordenar de mayor a menor e imprimir nuevamente."""

lista=[]
for x in range(5):
    valor=int(input("Ingrese un numero entero:"))
    lista.append(valor)
#orden de menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print("Lista ordenada de menor a mayor:", lista)
#orden de mayor a menor
for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print("Lista de mayor a menor:",lista)