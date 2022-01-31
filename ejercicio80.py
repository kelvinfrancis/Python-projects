'Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.'

lista=[]
while len(lista)<5:
    valor=int(input("Ingrese un numero entero:"))
    lista.append(valor)
valor_max=max(lista)
print("Lista:",lista)
print("Valor maximo de la lista es:",valor_max)