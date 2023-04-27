diccionario = {
    "marca": "ford",
    "modelo": "abc"
}

print(diccionario["marca"])
print(diccionario.get("modelo"))
keys = diccionario.keys()

diccionario["color"] = "negro"
diccionario["color"] = "azul"
print(keys)
print(diccionario)
print(diccionario.values())
print(diccionario.items())

print("marcas" in diccionario)

diccionario.update({"marca": "mazda"})
print(diccionario)

# eliminar un elemento especifico
diccionario.pop("marca")
print(diccionario)
# elimina el ultimo elemento
diccionario.popitem()
print(diccionario)

diccionario1 = {
    "marca": "mazda",
    "modelo": "ASDF",
    "año": 2023
}

diccionario2 = {
    "marca": "nisan",
    "modelo": "ASDF",
    "año": 2023
}

diccionario3 = {
    "marca": "tesla",
    "modelo": "ASDF",
    "año": 2021
}
print(diccionario1)
# elimina todo u diccionario
# del diccionario1
print(diccionario1)
diccionario2.clear()
print(diccionario2)

print("imprimir con for")

for j in diccionario3:
    print(j, diccionario3[j])

for x in diccionario3.values():
    print(x)

for x in diccionario3.keys():
    print(x)

for x in diccionario3.items():
    print(x)

# Make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Create a dictionary that contain three dictionaries:
# diccionarios anidados
people = {
    "Alice": {"age": 28, "city": "New York"},
    "Bob": {"age": 35, "city": "San Francisco"},
    "Charlie": {"age": 42, "city": "Chicago"}
}

print(people)
print(people["Alice"]["age"])

"""
for name in people:
	print(name)
    for key in people.keys():
    	print(key)
 """

# Para imprimir las claves y valores de un diccionario anidado
for person, info in people.items():
    print("Person:", person)
    for key, value in info.items():
        print(key + ":", value)
    print()