'Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.'

lista=[]
valor=int(input("Ingrese un numero entero:"))
while valor != 0:
    lista.append(valor)
    valor=int(input("Ingrese un numero entero:"))
print("Cantidad de valores:",len(lista))
print("Lista de valores",lista)
