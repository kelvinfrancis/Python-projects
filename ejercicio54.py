#Se cuenta con la siguiente información:
#Las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde.
#Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)
#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.


n=0
x=1
edadM=0
sumaM=0
edadT=0
sumaT=0
edadN=0
sumaN=0

print("Turno de la mañana")
for n in range(5): #mañana
    edadM=int(input("Ingrese la edad del estudiante: "))
    sumaM=sumaM+edadM
    
print("Turno de la tarde")
for n in range(6): #tarde
    edadT=int(input("Ingrese la edad del estudiante: "))
    sumaT=sumaT+edadT
        
print("Turno de la Noche")
for n in range(11): #noche
    edadN=int(input("Ingrese la edad del estudiante: "))
    sumaN=sumaN+edadN
    x=x+1

promedioM = sumaM/5
promedioT = sumaT/6
promedioN = sumaN/11

print("EL promedio de edades de los estudiantes del turno de la mañana es: ","{:.2f}".format(promedioM))
print("EL promedio de edades de los estudiantes del turno de la tarde es: ","{:.2f}".format(promedioT))
print("EL promedio de edades de los estudiantes del turno de la noche es: ","{:.2f}".format(promedioN))

if promedioM>promedioT and promedioM>promedioN:
    print("El promedio mayor es el turno de la mañana:","{:.2f}".format(promedioM))
elif promedioT>promedioM and promedioT>promedioN:
    print("El promedio mayor es el turno de la tarde:","{:.2f}".format(promedioT))
elif promedioN>promedioM and promedioN>promedioT:
    print("El promedio mayor es el turno de la noche:","{:.2f}".format(promedioN))