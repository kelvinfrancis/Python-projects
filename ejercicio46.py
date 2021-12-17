#Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000(n se carga por teclado)
#Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. 
#Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. 
#Dicha variable se carga antes de entrar a la estructura repetitiva for.

n = int(input("Ingrese la cantidad de valores: "))
x=0
mayorigualmil=0
menormil=0

for x in range(n):
    valor= int(input("Ingrese un numero entero: "))
    if valor<1000:
        menormil = menormil+1
    else:
        mayorigualmil = mayorigualmil+1

print("La cantidad de valores mayores o iguales a mil es: ", mayorigualmil)
print("La cantidad de valores menores a mil es: ", menormil)
