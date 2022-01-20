"""Mostrar la tabla de multiplicar del 5 empleando primero el while y seguidamente de nuevo empleando el for.
Programa: ejercicio55.py"""

#tabla del 5 con while
x=1
while x<=12:
    multi = x*5
    print("5 x",x,"=",multi)
    x=x+1

#tabla del 5 con for
for x in range(13):
    multi=x*5
    print("5 x",x,"=",multi)
    x=x+1
