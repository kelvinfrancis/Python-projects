#Ingresar un numero el cual se identifique si es positivo, negativo o nulo (0)#

num = int(input("Ingrese un numero: "))

if num==0:
    print("Este numero es Nulo (0)")
elif num<0:
    print("Este numero es Negativo")

else: print("Este numero es Positivo")

