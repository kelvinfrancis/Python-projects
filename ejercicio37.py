#Realizar un programa que permita cargar dos listas de 15 valores cada una. 
#Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

x=1
while x<=15:
    L1=int(input(x,"Ingrese un valor a la lista 1:"))
    L1=L1+L1
    L2=int(input(x,"Ingrese un valor a la lista 2:"))
    L2=L2+L2
    x=x+1
if L1>L2:
    print("Lista 1 mayor")
elif L2>L1:
    print("Lista 2 mayor")
else:
    print("Lista iguales")