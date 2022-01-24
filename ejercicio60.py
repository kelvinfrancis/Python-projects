'''Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.'''

opcion='si'
suma=0
while opcion =='si':
    x=int(input("Ingrese el valor que desea sumar:"))
    suma=suma+x
    opcion=input("Desea ingresar otro valor? (si/no):")
print("La suma total de los valores es:",suma)
