# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base 
# y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input("Ingrese la cantidad de triangulos: "))
x=0
c=1
superficiemayor=0
for x in range(n):
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    superficie = base*altura
    print("Triangulo ",c,"Base: ",base," Altura: ",altura," Superficie: ",superficie)
    x=x+1
    if superficie >12:
        superficiemayor=superficiemayor+1
    
print("La cantidad de triangulos cuya superficie es mayor a 12 es: ",superficiemayor)