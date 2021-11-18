#Escribir un programa que pida ingresar la coordenada de un punto en el plano, 
#es decir dos valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
#(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("Ingrese el valor de X: "))
y = int(input("Ingrese el valor de Y: "))

if x == 0 and y == 0:
    print("Ingrese valores diferentes de cero. ")
elif x>0 and y>0:
    print("1er cuadrante.")

elif x<0 and y>0:
    print("2do cuadrante.")

elif x<0 and y<0:
    print("3er cuadrante.")
else:
    print("4to cuadrante")


