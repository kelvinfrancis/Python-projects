# De un operario se conoce su sueldo y los años de antigüedad. 
#Se pide confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, 
# otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, 
# otorgarle un aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios

#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=8&codigo=8&inicio=0

sueldo = int(input("Ingrese su sueldo: "))
tiempo = int(input("Ingrese los años trabajados: "))

if sueldo<500 and tiempo>=10:
    aumento = (sueldo*0.2) + sueldo
    print("El sueldo a pagar es: ")
    print(aumento)
elif sueldo<500 and tiempo<10:
    aumento = (sueldo*0.05) + sueldo
    print("El sueldo a pagar es: ")
    print(aumento)
elif sueldo>=500:
    print("El sueldo no se le otorga aumento: ")
    print(sueldo)