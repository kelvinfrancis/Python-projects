#Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie

def calcularSuperficie(lado):
    sup = lado*lado
    return f"La supeficie del cuadrado es: {sup}"
    
lado = float(input("Ingrese el lado del cuadrado: "))
print(calcularSuperficie(lado))
