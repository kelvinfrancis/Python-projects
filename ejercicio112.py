"""Confeccionar una aplicación que muestre una presentación en
pantalla del programa. Solicite la carga de dos valores y nos muestre la suma.
Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones."""


def presentacion():
    print("Este programa realiza la suma de dos valores.")


def carga_suma():
    valor1 = int(input('Ingrese un valor: '))
    valor2 = int(input('Ingrese otro valor entero: '))
    suma = valor1 + valor2
    print(f"El valor de la suma es: {suma}")

def finalizacion():
    print('Gracias por utilizar el programa.')


presentacion()
carga_suma()
finalizacion()



