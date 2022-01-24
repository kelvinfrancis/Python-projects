'''Solicitar la carga del nombre de una persona en minúsculas. 
Mostrar un mensaje si comienza con vocal dicho nombre.'''

nombre=input("Ingrese el nombre en minusculas:")
if 'a'==nombre[0] or 'e'==nombre[0] or 'i'==nombre[0] or 'o'==nombre[0] or 'u'==nombre[0]:
    print("El nombre ingresado empieza con una vocal.")
else:
    print("EL nombre ingresado empieza con una consonante.")