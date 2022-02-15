"""Crear y cargar una lista con los nombres de tres alumnos. 
Cada alumno tiene dos notas, almacenar las notas en una lista paralela. 
Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas."""

nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese un nombre: ")
    nombres.append(nom)
    n1=int(input("Ingrese la primera nota: "))
    n2=int(input("Ingrese la segunda nota: "))
    notas.append([n1,n2])
for x in range(len(nombres)):
    print(notas[x],nombres[x])