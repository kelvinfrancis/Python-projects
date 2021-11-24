#Codificar un programa que solicite la carga de un valor positivo y 
#nos muestre desde 1 hasta el valor ingresado de uno en uno.
#Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.

x = int(input("Ingrese hasta que valor desea contar: "))
y = 1
if x<=0:
    print("Este valor no es un numero positivo")
else:
    while y<=x:
        print(y)
        y=y+1