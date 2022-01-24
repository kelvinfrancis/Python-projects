'''Realizar la carga de dos nombres de personas distintos. 
Mostrar por pantalla luego ordenados en forma alfabética.'''

n1=input("Ingrese el primer nombre:")
n2=input("Ingrese el segundo nombre:")
if n1>n2:
    print("El orden alfabeticamente es: 1-",n2,"2-",n1)
else:
    print("El orden alfabeticamente es: 1-",n1,"2-",n2)