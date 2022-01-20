#Realizar la carga por teclado del nombre, edad y altura de dos personas. 
#Mostrar por pantalla el nombre de la persona con mayor altura.
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=12&codigo=12&inicio=0

n1=input("Ingrese el primero nombre:")
a1=float(input("Ingrese la altura de la primera persona en metros: "))
n2=input("Ingrese el segundo nombre:")
a2=float(input("Ingrese la altura de la segunda persona en metros: "))

if a1>a2:
    print("La persona con la altura mayor es: ",n1)
else:
    print("La persona con la altura mayor es: ",n2)