"""Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado"""
nombres=[]
sueldos=[]
for x in range(3):
    nom=input("Ingrese el nombre del empleado: ")
    nombres.append(nom)
    v1=float(input("Ingrese el sueldo del primer mes: "))
    v2=float(input("Ingrese el sueldo del segundo mes: "))
    v3=float(input("Ingrese el sueldo del tercer mes: "))
    sueldos.append([v1,v2,v3])
suma1=sum(sueldos[0])
suma2=sum(sueldos[1])
suma3=sum(sueldos[2])
print("Empleados y sueldos:")
print(nombres[0],"RD$",suma1)
print(nombres[1],"RD$",suma2)
print(nombres[2],"RD$",suma3)
print("El empleado con el acumulado mayor es:")
if suma1>suma2 and suma1>suma3:
    print(nombres[0])
elif suma2>suma1 and suma2>suma3:
    print(nombres[1])
else:
    print(nombres[2])
