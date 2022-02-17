"""Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre."""

padres=[]
hijos=[]
for x in range(3):
    padres.append([])
    hijos.append([])
    for k in range(3):
        papa=input("Ingrese el nombre del padre: ")
        mama=input("Ingrese el nombre de la madre: ")
        sons=input("Ingrese los nombres de los hijos. Si no tienen, escribir -ninguno-: ")
        padres[x].append(papa,mama)
        hijos[x].append(sons)
for x in range(len(padres)):
    print("Lista de padres e hijos:")
    print(padres[x],hijos[x])



