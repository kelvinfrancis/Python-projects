"""Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema."""
x=0
suma=0
x=int(input("Ingrese un valor: "))
while x != -1:
    suma=suma+x
    x=int(input("Ingrese el siguiente valor: "))
print("El total de la suma es:",suma)