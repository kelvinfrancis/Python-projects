"Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra."

lista=[]
while len(lista)<5:
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
print("Lista:",lista)
print("El valor minimo de la lista es:",min(lista),", y su posicion en la lista es:",lista.index(min(lista)))
