#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. 
#Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

mul3 = 0
mul5 = 0
mul3y5=0
nomul=0
x=0
for x in range (10):
    valor = int(input("Ingrese un numero entero: "))
    if valor % 3 ==0:
        mul3 = mul3+1
    elif valor % 5 ==0:
        mul5 = mul5+1
    elif valor % 3 ==0 and valor % 5 ==0:
        mul3y5 = mul3y5+1
    else:
        nomul=nomul+1

print("La cantidad de numeros que son multiplos de 3 es: ", mul3)
print("La cantidad de numeros que son multiplos de 5 es: ", mul5)
print("La cantidad de numeros que son multiplos de 3 y 5 es: ", mul3y5)
print("La cantidad de numeros que no son multiplos ni de 3 ni de 5 es: ", nomul)

