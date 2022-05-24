"""Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)"""

empleados = []
sueldos = []

cantidad = int(input("Ingrese la cantidad de empleados que tiene la empresa: "))
for x in range(cantidad):
    nom = input("Ingrese el nombre del empleado: ")
    empleados.append(nom)
    pago = int(input("Ingrese su sueldo mensual: "))
    sueldos.append(pago)

print("Lista de empleados compleda: ")
for x in range(cantidad):
    print(empleados[x], sueldos[x])

for x in range(cantidad):
    if sueldos[x] > 10000:
        sueldos.pop(x)
        empleados.pop(x)

print("Lista de empleados con sueldo menor a 10000: ")
for x in range(len(empleados)):
    print(empleados[x], sueldos[x])