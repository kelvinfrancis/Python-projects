#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=21&codigo=21&inicio=15
"""Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días."""

empleados=[]
diasFaltas=[]

for k in range(3):
    nombre=input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    diasf=int(input("Cantidad de dias que falto el empleado: "))
    diasFaltas.append([])
    for x in range(diasf):
        dia=int(input("Ingrese el numero de dias que falto: "))
        diasFaltas[k].append(diasf)

print("Nombre de empleados y dias que falto.")

for k in range(3):
    print(empleados[k])
    for x in range (len(diasFaltas[k])):
        print(diasFaltas[k][x])

print("Nombre del empleado y la cantidad de inasistencias")
for x in range(3):
    print(empleados[x], len(diasFaltas[x]))

menor=len(diasFaltas[0])
for x in range(1,3):
    if len(diasFaltas[x]) < menor:
        menor= len(diasFaltas[x])

print("Empleados que faltaron menos: ")
for x in range(3):
    if len(diasFaltas[x])==menor:
        print(empleados[x])