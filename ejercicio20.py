#Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) 
#Cargar por teclado el valor numérico del día, mes y año.
#Ejemplo: dia:10 mes:2 año:2018

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
year = int(input("Ingrese el año: "))

if mes == 1 or mes == 2 or mes == 3:
    print("Corresponde al primer trimestre del año")