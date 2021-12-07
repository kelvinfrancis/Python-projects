# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio. 
# Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.
sum=0
promedio=0
for x in range(10):
    valor = int(input("Ingrese un valor: "))
    sum = valor+sum
promedio = sum/10
print("La suma total de los valores es: ", sum)
print("El promedio total de los valores es: ", promedio)
