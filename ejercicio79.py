"""Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos."""

lista_dia=[]
lista_tarde=[]
sueldo_tarde=0
while len(lista_dia)<4:
    sueldo_dia=int(input("Ingrese los sueldos de los empleados de la mañana:"))
    lista_dia.append(sueldo_dia)  
while len(lista_tarde)<4:
    sueldo_tarde=int(input("Ingrese los sueldos de los empleados de la tarde:"))
    lista_tarde.append(sueldo_tarde)
print("Salarios del turno de la mañana:",lista_dia)
print("Salarios del turno de la tarde:",lista_tarde)
