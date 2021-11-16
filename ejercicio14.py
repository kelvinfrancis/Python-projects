#ejercicio de notas con condicionales#
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedioNotas = (nota1+nota2+nota3)/3

if promedioNotas>=7:
    print("Promocionado")
elif promedioNotas>=4:
    print("Regular")
else:
    print("Reprobado")