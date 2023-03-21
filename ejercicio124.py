#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.


def numeros_promedios(a, b, c):
    promedio = (a+b+c) / 3
    return f"EL promedio de los numeros es {round(promedio,2)}"
    
num1 = int(input("Ingrese primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercero numero entero: "))

print(numeros_promedios(num1, num2, num3))
