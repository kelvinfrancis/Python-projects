'''Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""'''

oracion=input("Ingrese una oracion:")
eblancos = oracion.count(" ")
print("La cantidad de espacios en blancos en la oracion es:",eblancos)