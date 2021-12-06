#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional 
#(este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
#	if valor%2==0: 

n=int(input("Ingrese la cantidad de numero enteros que desea ingresar: "))
x=1
par = 0
impar = 0
while x<=n:
    num=int(input("Ingrese un numero entero: "))
    if num%2==0:
        par = par+1
    else:
        impar = impar+1
    x=x+1

print("La cantidad de numeros pares es: ",par)
print("La cantidad de numeros impares es: ",impar)
