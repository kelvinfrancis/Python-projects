#Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
x=1
n=0
print("--- Tabla de multiplicacion del 5 ---")
for n in range(10):
    multi = 5*x
    print("5 x",x,"= ",multi)
    x=x+1
