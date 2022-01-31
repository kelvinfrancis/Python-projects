"Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos"

lista_sueldos=[]
suma=0
while len(lista_sueldos)<5:
    sueldo=int(input("Ingrese un sueldo:"))
    lista_sueldos.append(sueldo)
    suma=suma+sueldo
promedio=suma/len(lista_sueldos)
print("Lista de sueldos:",lista_sueldos)
print("Promedio:",promedio)

