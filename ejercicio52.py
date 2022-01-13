# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n=0
t=1
c1=0
c2=0
c3=0
c4=0
puntos=int(input("Ingrese la cantidad de puntos a procesar: "))
for n in range(puntos):
    print("Punto no.",t)
    x=int(input("Ingrese la coordenadas de X:"))
    y=int(input("Ingrese la coordenadas de Y:"))
    if x>0 and y>0:
        c1=c1+1
    elif x<0 and y>0:
        c2=c2+1
    elif x<0 and y<0:
        c3=c3+1
    elif x>0 and y<0:
        c4=c4+1
    t=t+1
print("Puntos ingresados en el cuadrante 1: ",c1)
print("Puntos ingresados en el cuadrante 2: ",c2)
print("Puntos ingresados en el cuadrante 3: ",c3)
print("Puntos ingresados en el cuadrante 4: ",c4)