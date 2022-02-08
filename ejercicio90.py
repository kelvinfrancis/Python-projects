"Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla."

paises=[]
while len(paises)<5:
    pais=input("Ingrese el nombre del pais:")
    paises.append(pais)
print("Lista de paises:",paises)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("Lista de paises ordenada alfabeticamente:",paises)