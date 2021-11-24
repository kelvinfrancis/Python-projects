#Desarrollar un programa que permita la carga de 10 valores por teclado y 
#nos muestre posteriormente la suma de los valores ingresados y su promedio.

i=1
suma=0
while i<=10:
    x = int(input("Ingrese un valor: "))
    suma=suma+x
    i=i+1
promedio = suma/10
print("La suma de los valores es: "), print(suma)
print("El promedio de los valores es: "), print(promedio)