#Escribir un programa en el cual: dada una lista de tres valores numéricos distintos 
# se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=8&codigo=8&inicio=0

v1 = int(input("Ingrese el primer valor: "))
v2 = int(input("Ingrese el segundo valor: "))
v3 = int(input("Ingrese el tercer valor: "))

if v1==v2 and v2==v3:
    print("Los tres valores son iguales.")
elif v1>v2 and v2>v3:
    print("El valor mayor es: "), print(v1)
    print("El valor menor es: "), print(v3)
elif v1>v3 and v2<v3: 
    print("El valor mayor es: "), print(v1)
    print("El valor menor es: "), print(v2)
elif v2>v1 and v1>v3:
    print("El valor mayor es: "), print(v2)
    print("El valor menor es: "), print(v3)
elif v2>v3 and v1<v3:
    print("El valor mayor es: "), print(v2)
    print("El valor menor es: "), print(v1)
elif v3>v1 and v1>v2:
    print("El valor mayor es: "), print(v3)
    print("El valor menor es: "), print(v2)
elif v3>v2 and v1<v2:
    print("El valor mayor es: "), print(v3)
    print("El valor menor es: "), print(v1)
