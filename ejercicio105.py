"""Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor."""

paises=[]
temperaturas=[]
promediotemp=[]

for x in range(4):
    nombre=input("Ingrese el nombre del pais:")
    paises.append(nombre)
    temp1=int(input("Ingrese la primera temperatura:"))
    temp2=int(input("Ingrese la segunda temperatura:"))
    temp3=int(input("Ingrese la tercera temperatura:"))
    temperaturas.append([temp1,temp2,temp3])

print("Paises y temperaturas medias de los ultimos 3 meses")
for x in range(4):
    print(paises[x], temperaturas[x][0], temperaturas[x][1],temperaturas[x][2])

for x in range(4):
    prom=(temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])/3
    promediotemp.append(prom)

print("Listado de paises y temperaturas media trimestrales")
for x in range(4):
    print(paises[x], promediotemp[x])

posmayor=0
for x in range(1,4):
    if promediotemp[x]>promediotemp[posmayor]:
        posmayor=x
print("Pais con temperatura media trimestral mayor",paises[posmayor])