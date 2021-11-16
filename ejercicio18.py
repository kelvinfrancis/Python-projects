#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
#cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente.
#Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido,y sabiendo que:
#   Nivel máximo:	Porcentaje>=90%.
#	Nivel medio:	Porcentaje>=75% y <90%.
#	Nivel regular:	Porcentaje>=50% y <75%.
#	Fuera de nivel:	Porcentaje<50%.

preguntasRealizadas = int(input("Ingrese la cantidad de preguntas realizadas en el test: "))
preguntasCorrectas = int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))

promedioTest = (preguntasCorrectas/preguntasRealizadas)*100

if promedioTest >=90:
    print("Nivel máximo")
elif 75 <=promedioTest<90:
    print("Nivel medio")
elif 50 <=promedioTest<75:
    print("Nivel regular")
else: print("Fuera de nivel")