"""Crear y cargar en un lista los nombres de 5 países y 
en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. 
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente."""

paises=[]
habitantes=[]
for x in range(5):
    p=input("Ingrese el nombre del pais:")
    paises.append(p)
    h=int(input("Ingrese la cantidad de habitantes del pais:"))
    habitantes.append(h)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
print("Lista de paises ordenados alfabeticamente:")
for x in range(5):
    print(paises[x],habitantes[x])