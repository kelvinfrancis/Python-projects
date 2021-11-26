#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

print("------Promedio de alturas de la cantidad de personas ingresadas------")
n=int(input("Ingrese la cantidad de personas: "))
x=1
suma=0
while x<=n:
    altura=float(input("Ingresa la altura en METROS: "))
    suma=suma+altura
    x=x+1
promedioAltura=suma/n
print("La altura promedio de las personas ingresadas es: ")
print(promedioAltura)

