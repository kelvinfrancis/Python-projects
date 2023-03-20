#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor

def numero_mayor(a, b):
    if a > b:
        return a
    else:
        return b
    
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))

print(f"El mayor es: {numero_mayor(a, b)}")
