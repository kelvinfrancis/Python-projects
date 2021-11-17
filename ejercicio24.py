#Se ingresan tres valores por teclado, 
#si todos son iguales se imprime la suma del primero con el segundo y 
# a este resultado se lo multiplica por el tercero.

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if num1 == num2 and num2 == num3:
    resultado = (num1+num2)*num3
    print("El resultado de la suma de los dos primeros valores x el tercer valor es: ")
    print(resultado)
else:
    print("Los numeros no son iguales.")