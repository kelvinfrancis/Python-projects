"""Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. 
Definir varias líneas de comentarios indicando el nombre del programa, el programador y 
la fecha de la última modificación. Utilizar el caracter # para los comentarios."""

#Suma de 10 valores ingresados por teclado.
#Programador: Kelvin F. Moquete P.
#Fecha: 20/01/2022
x=0
n=0
suma=0
for x in range(10):
    n=int(input("Ingrese un valor: "))
    suma=suma+n
print("La suma total de los valores ingresados es:",suma)
