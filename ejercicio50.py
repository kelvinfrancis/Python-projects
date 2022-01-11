# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo 
# (los primeros 12 términos) Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

n=0
x=1
num=int(input("Ingrese un numero del 1 al 10: "))
while num<0 or num>10:
    num=int(input("Debe ingresar un numero entre 1 y 10: "))
else:
    print("Tabla de multiplicacion del numero", num)
    for n in range(12):
        multi=num*x
        print(num,"x",x," = ",multi)
        x=x+1