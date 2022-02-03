'''Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.'''
lista1=[]
lista2=[]

while len(lista1)<4:
    valor1=int(input("Ingrese un numero entero:"))
    lista1.append(valor1)
    valor2=int(input("Ingrese un numero entero:"))
    lista2.append(valor2)
x=0
suma=0
lista3=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
print("Lista 1:",lista1)
print("Lista 2:",lista2)
print("Suma de las 2 listas:",lista3)