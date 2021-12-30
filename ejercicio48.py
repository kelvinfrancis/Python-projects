# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados

n=0
suma=0
for n in range(10):
    valor = int(input("Ingrese un valor: "))
    n=n+1
    if n>5:
        suma=valor+suma
        
print("La suma de los ultimos 5 valores es: ", suma)