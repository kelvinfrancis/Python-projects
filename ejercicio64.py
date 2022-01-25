'''Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@"'''
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=13&codigo=13&inicio=0

email=input("Ingrese un correo electronico: ")
ocurrencias=email.count('@')
while ocurrencias>=2:
    email=input("Correo electronico no valido, favor ingresar un correo valido: ")
print("Correo electronico valido, solo tiene una @.")
