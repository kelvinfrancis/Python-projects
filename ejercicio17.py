#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
#Mostrar un mensaje de error si el número de cifras es mayor.
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=7&codigo=7&inicio=0

num = int(input("Ingrese un numero menor de 3 cifras:"))

if num<10:
    print("Este numero tiene UN digito.")

elif num<100:
    print("Este numero tiene DOS digitos.")

elif num<1000:
    print("Este numero tiene TRES digitos.")

else:
    print("Este numero tiene MAS de TRES digitos.")

