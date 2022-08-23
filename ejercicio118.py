"""Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie."""

def calcular_perimetro_superficie():
    lado_cuadrado = float(input('Ingrese la medida del lado de un cuadrado: '))
    
    pregunta_1 = input('Le gustaria saber el perimetro? (si \ no): ')
    pregunta_2 = input('Le gustaria saber la superficie? (si \ no): ')
    
    if pregunta_1 == 'si':
        perimetro = lado_cuadrado * 4
        print(f'El perimetro es: {perimetro}')
    elif pregunta_1 == 'no':
        pass
    
    if pregunta_2 == 'si':
        superficie = lado_cuadrado ** 2
        print(f'La superficie es: {superficie}')
    elif pregunta_2 == 'no':
        pass


calcular_perimetro_superficie()