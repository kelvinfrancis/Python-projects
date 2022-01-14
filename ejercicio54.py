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

for n in range(5): #mañana
    edadM=int(input("Ingrese la edad del estudiante: "))
    sumaM=sumaM+edadM
    
    for n in range(6): #tarde
        edadT=int(input("Ingrese la edad del estudiante: "))
        sumaT=sumaT+edadT
        
        for n in range(11): #noche
            edadN=int(input("Ingrese la edad del estudiante: "))
            sumaN=sumaN+edadN
            x=x+1