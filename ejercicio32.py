#Escribir un programa que solicite ingresar 10 notas de alumnos 
# y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

print("----Ingrese 10 notas----")
x=1
mayorigual=0
menor=0
while x<=10:
    nota=int(input("Ingrese la nota: "))
    if nota>=7:
        mayorigual = mayorigual+1
    else:
        menor = menor+1
    x=x+1
print("La cantidad de alumnos con notas mayores o iguales a 7 son: ")
print(mayorigual)
print("La cantidad de alumnos con notas menores de 7 son: ")
print(menor)