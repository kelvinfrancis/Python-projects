"""En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8,
 "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”."""


nombres=[]
notas=[]
condiciones=[]

while len(nombres)<4:
    nombre=input("Ingrese el nombre del estudiante:")
    nombres.append(nombre)
    nota=float(input("Ingrese la nota del estudiante en base a 10:"))
    notas.append(nota)
x=0
alumnos_buenos=0
for x in range(4):
    if notas[x]>=8:
        condicion="Muy Bueno"
        condiciones.append(condicion)
        alumnos_buenos+=1
    elif 4<notas[x]<7:
        condicion="Bueno"
        condiciones.append(condicion)
    else:
        condicion='Insuficiente'
        condiciones.append(condicion)
print("Nombres:",nombres)
print("Notas:",notas)
print("Cantidad de alumnos Muy Buenos:",alumnos_buenos)