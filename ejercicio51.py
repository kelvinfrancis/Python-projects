#Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=10&codigo=10&inicio=0

n=0
trgulos=int(input("Ingrese la cantidad de triangulos que desea: "))
x=1
equi=0 #equilatero
esca=0 #escaleno
isos=0 #isosceles
for n in range(trgulos):
    print("Triangulo no.",x)
    l1=int(input("Ingrese el primer lado: "))
    l2=int(input("Ingrese el segundo lado: "))
    l3=int(input("Ingrese el tercer lado: "))
    if l1 == l2 and l2 == l3 and l1 == l3:
        equi=equi+1
    elif l1 == l2 and l1 != l3 and l2 != l3:
        isos=isos+1
    elif l1 != l2 and l2 != l3 and l1 != l3:
        esca=esca+1
    x=x+1

print("La cantidad de triangulos equilateros es: ", equi)
print("La cantidad de triangulos isósceles es: ", isos)
print("La cantidad de triangulos escalenos es: ", esca)