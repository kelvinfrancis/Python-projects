#se cargan 3 numeros, debe imprimir el mas grande de ellos

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

print("El numero mayor es: ")

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
elif num2>num3:
    print(num2)
else:
    print(num3)