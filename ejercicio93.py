"""Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. 
Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.
Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor debemos 
intercambiar los nombres para que las listas continúen paralelas 
(es decir que en los mismos subíndices de cada lista continúe la información relacionada)"""
alumnos=[]
notas=[]
for x in range(5):
    nombre=input("Ingrese el nombre del alumno: ")
    alumnos.append(nombre)
    nota=int(input("Ingrese la nota del alumno:"))
    notas.append(nota)
print("---Lista de alumnos y sus notas:")
for x in range(5):
    print(notas[x],alumnos[x])
#orden de mayor a menor
for k in range(4):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux=notas[x]
            aux1=alumnos[x]
            notas[x]=notas[x+1]
            alumnos[x]=alumnos[x+1]
            notas[x+1]=aux
            alumnos[x+1]=aux1
print("---Lista ordenada de mayor a menor:")
for x in range(5):
    print(notas[x],alumnos[x])
