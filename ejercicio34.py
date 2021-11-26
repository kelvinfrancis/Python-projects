#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 
#y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=9&codigo=9&inicio=0

n=int(input("Ingrese la cantidad de empleados: "))
x=1
entre100y300 = 0
masde300 = 0
importe=0
while x<=n:
    sueldo=int(input(print("Ingrese el sueldo del empleado:")))
    if 100<sueldo<=300:
        entre100y300=entre100y300+1
    elif sueldo>300:
        masde300=masde300+1
    x=x+1
    importe=importe+sueldo
print("La cantidad de empleados que ganan entre $100 y $300 es: ")
print(entre100y300)
print("La cantidad de empleados que ganan mas de $300 es: ")
print(masde300)
print("El importe que gasta la empresa en sueldo al personal es: ")
print(importe)
