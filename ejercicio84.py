'''Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)'''
nombres=[]
edades=[]
while len(nombres)<5:
    nombre=input("Ingrese un nombre:")
    nombres.append(nombre)
    edad=int(input("Ingrese una edad:"))
    edades.append(edad)
x=0
print("Personas mayores de edad (18+):")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
    x+=1