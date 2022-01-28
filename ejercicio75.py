'''Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.'''
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=15&codigo=15&inicio=0

lista=[]
x=0
for x in range(5):
    valor=int(input("Ingrese un numero entero: "))
    lista.append(valor)
    x=x+1
print("los valores de la lista son:",lista)