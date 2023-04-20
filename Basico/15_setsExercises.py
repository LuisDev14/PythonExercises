# remove duplicates
numeros = [1, 2, 3, 3, 2, 1, 54, 3, 9]
print(numeros)
noRepetidos = list(set(numeros))
print(noRepetidos[0])

# Operations with sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union = set1.union(set2)
interseccion = set1.intersection(set2)
diferencia = set1.difference(set2)
print(union)         # Salida: {1, 2, 3, 4, 5, 6, 7}
print(interseccion)  # Salida: {3, 4, 5}
print(diferencia)    # Salida: {1, 2}

#symmetric_difference(): Este método devuelve un nuevo conjunto que contiene elementos que están en uno u otro conjunto, pero no en ambos.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
resultado = set1.symmetric_difference(set2)
print(resultado)  # Salida: {1, 2, 6, 7}

#issubset(): Este método devuelve True si el conjunto dado es un subconjunto del conjunto sobre el que se llama, de lo contrario, devuelve False.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = {6, 7}
print(set2.issubset(set1))  # Salida: True
print(set3.issubset(set1))  # Salida: False

#update(): Este método agrega elementos del conjunto dado al conjunto sobre el que se llama.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Salida: {1, 2, 3, 4, 5}

#intersection_update(): Este método actualiza el conjunto sobre el que se llama para que contenga solo los elementos que también están en el conjunto dado.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.intersection_update(set2)
print(set1)  # Salida: {3, 4, 5}

