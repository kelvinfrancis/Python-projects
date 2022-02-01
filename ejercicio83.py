"Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)"
lista=[]
while len(lista)<5:
    valor=int(input("Ingrese un numero entero:"))
    lista.append(valor)
mayor=max(lista)
if lista.count(mayor) >=2:
    print("Lista",lista)
    print("El mayor es",mayor,"y se encuentra en",lista.count(mayor),"posiciones en la lista.")
else:
    print("Lista",lista)
    print("El mayor es:",mayor)