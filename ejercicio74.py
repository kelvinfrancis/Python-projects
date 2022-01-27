'''Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.'''

lista_nombres=["Kelvin","Alicia","juan","jose","ana"]
contador=0
x=0
while x<len(lista_nombres):
    if len(lista_nombres[x]) >= 5:
        contador=contador+1
    x=x+1
print("Lista de nombres:",lista_nombres)
print("Cantidad de nombres con 5 o mas caracteres",contador)