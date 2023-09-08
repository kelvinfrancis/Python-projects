# --------Listas

# forma 1
frutas = ['manzana', 'pera', 'uva']
print(frutas)

# forma 2
vocales = list(('a', 'i', 'e', 'u'))
print(vocales)

# ----- Metodos de listas
# append, (agregar) se agrega al final
frutas.append('coco')

# clear, (vacia la lista)
frutas.clear()
print(frutas)

# count, cuenta la cantidad de elementos especificos
print(f"Count de a: {vocales.count('a')}")

# extend, extiende la lista con otra variable iterable (otra lista, tuples, sets)
frutas.extend(('banana', 'melocoton', 'uva verde', 'kiwi', 'coco'))
print(frutas)

# index, saber la posicion exacta de un valor en la lista.
print(f"index de banana: {frutas.index('banana')}")

# insert, inserta un elemento en la posicion que quiera en la lista
vocales.insert(1,'o')
print(f"o agregada con insert: {vocales}")

# pop, elimina un elemento usando el index
frutas.pop(1)
print(f" pop remueve melocoton: {frutas}")

# remove, elimina un elemendo usando el valor, si esta repetido solo elimina la primera
vocales.remove('i')
print(f"remove a 'i' de la lista: {vocales}")

# reverse, desordena la lista
print(f"reverse desordenada: {frutas.reverse()}")

# sort, ordena la lista
print(f"sort ordenada: {vocales.sort()}")

# copy, crea una lista nueva a partir de una existente desvinculada de la original
lista_nueva = frutas.copy()

# ----- Comprension de listas
# crear una lista nueva con las frutas que no tengan 'a' de la lista frutas
frutas_sin_a = [fruta for fruta in frutas if 'a' not in fruta]
print(f"fruta sin a: {frutas_sin_a}")



