'''Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.'''
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=14&codigo=14&inicio=0

lista=[1,2,3,4,5]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("La suma total de los valores es:",suma)
