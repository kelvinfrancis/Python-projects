# Escribir un programa que solicite por teclado 10 notas de alumnos y 
# nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
# https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=10&codigo=10&inicio=0

a=0
r=0
f=0
for f in range(10):
    nota=int(input("Ingrese la calificacion: "))
    if nota>=7:
        a=a+1
    else:
        r=r+1
print("La cantidad de alumnos con notas mayores o iguales a 7 son: ",a)
print("La cantidad de alumnos con notas menores a 7 son: ",r)