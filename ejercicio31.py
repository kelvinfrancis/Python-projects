#--PROBLEMA 4--- https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=9&codigo=9&inicio=0
#Una planta que fabrica perfiles de hierro posee un lote de n piezas.
#Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil;
#sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas.
# Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

x=1
n=int(input("Ingrese la cantidad de piezas que desea ingresar: "))

while x<=n:
    longitudPieza = float(input("Ingrese la longitud de la pieza: "))
    if 1.20<longitudPieza<1.30:
        cantidad = cantidad+1
    x=x+1
print("La cantidad de piezas aptas que hay en el lote son: ")
print(cantidad)