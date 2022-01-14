#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=10&codigo=10&inicio=0

n=0
x=1
negativos=0
positivos=0
multiplo15=0
sumapares=0
for n in range(10):
    valor=int(input("Ingrese un valor: "))
    if valor<0:
        negativos=negativos+1
    elif valor>0:
        positivos=positivos+1
    
    if valor % 15 ==0:
        multiplo15=multiplo15+1
    
    if valor % 2 == 0:
        sumapares=sumapares+valor

print("La cantidad de valores ingresados negativos es: ",negativos)
print("La cantidad de valores ingresados positivos es: ",positivos)
print("La cantidad de valores multiplos de 15 es: ",multiplo15)
print("El valor acumulado de los sumeros ingresados pares es: ",sumapares)

