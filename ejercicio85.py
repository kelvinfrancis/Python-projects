'''Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. 
Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.'''
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=17&codigo=17&inicio=15

productos=[]
precios=[]
while len(productos)<5:
    prod=input("Ingrese el nombre del producto:")
    productos.append(prod)
    precio=float(input("Ingrese el precio del producto: RD$"))
    precios.append(precio)
x=0
print("Los productos con precio mayor al primer producto ingresado""(",productos[0],") - RD$",precios[0])
for x in range(5):
    if precios[x]>precios[0]:
        print("*",productos[x],"- RD$",precios[x])
