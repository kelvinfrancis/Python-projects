"Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético."

lista=[]
while len(lista)<5:
    valor=input("Ingrese un nombre:")
    lista.append(valor)
print("Lista",lista)
print("El nombre  menor en orden alfabetico es:", min(lista))