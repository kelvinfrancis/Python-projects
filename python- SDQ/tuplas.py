# ----- Tuplas

# Forma 1 
frutas = ('manzana', 'kiwi', 'cereza')
# Forma 2
vocales = tuple(('a','e','i','o','u'))

# tuplas con un solo elemento SIEMPRE tiene que tener una ',' despues.
cosas = ('camisa', ) 

# operaciones con tuplas
nueva = frutas + vocales 
nueva2 = frutas *2
print(nueva)
print(nueva2)

# Desempaquetar, asignar un nombre de variable a los elemento de la tupla seleccionados
datos = ('Kelvin', 'Programador', 4000, 'TI', 'seguro')
# se utiliza '*variable' para referirse a los valores que deseamos ignorar
(name, position, salary, departament, *otros) = datos

print(name)
print(salary)

# --- Metodos 
#count, para contar las veces que aparece un elemento en la tuple
print(f"count kiwi: {frutas.count('kiwi')}")

#index, para saber el indice de un elemento
print(f"indice de kiwi: {frutas.index('kiwi')}")