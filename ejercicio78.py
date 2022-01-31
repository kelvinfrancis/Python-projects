'''Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.'''

lista_altura_personas=[]
suma=0
while len(lista_altura_personas)<5:
    altura=float(input("Ingrese la altura en metros:"))
    lista_altura_personas.append(altura)
    suma=suma+altura
promedio=suma/len(lista_altura_personas)

x=0
mayores_al_promedio=0
menores_al_promedio=0
for x in range(len(lista_altura_personas)):
    if lista_altura_personas[x]>promedio:
        mayores_al_promedio +=1
    else:
        menores_al_promedio +=1
    x=x+1
print("Lista de alturas:",lista_altura_personas)
print("Promedio de alturas:",promedio)
print("Cantidad de personas mayores al promedio:",mayores_al_promedio)
print("Cantidad de personas menores al promedio:",menores_al_promedio)

    