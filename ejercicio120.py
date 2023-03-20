#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenarEnteros(a, b, c):
    if a > b and a > c:
        if b > c:
            return c, b, a
        else:
            return b, c, a
    elif b > a and b > c:
        if a > c:
            return c, a, b
        else:
            return a, c, b
    elif c > a and c > b:
        if a > b:
            return b, a, c
        else:
            return a, b, c
    else:
        return "Son el mismo numero."

def ingresarnum():
        num1 = int(input("Ingrese un numeros:" ))
        num2 = int(input("Ingrese un numeros:" ))
        num3 = int(input("Ingrese un numeros:" ))
    
        print(ordenarEnteros(num1, num2, num3))

ingresarnum()
