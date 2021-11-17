#Realizar un programa que pida cargar una fecha cualquiera, 
#luego verificar si dicha fecha corresponde a Navidad.

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
year = int(input("Ingrese el año: "))

if mes == 12 and dia == 25:
    print("Es navidad.!")
else:
    print("No es navidad.")