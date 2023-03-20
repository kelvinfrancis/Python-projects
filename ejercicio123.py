# Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def contar_caracteres(palabra):
    cant_de_letras = 0
    for letra in palabra:
        cant_de_letras += 1
        
    return cant_de_letras
    
name1 = input("Ingrese el primer nombre: ")
name2 = input("Ingrese el segundo nombre: ")

if contar_caracteres(name1) > contar_caracteres(name2):
    print(f"{name1} tiene mas caracteres que {name2}")
else:
    print(f"{name2} tiene mas caracteres que {name1}")
