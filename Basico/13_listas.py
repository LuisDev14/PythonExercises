frutas = ["manzana", "uva", "fresa", 'pera', 'sandia', 'melon']
print(frutas[2:5])  # imprime desde la posicion 2 a la 5 incluyendo el 2 pero no el 5
print(frutas[0])
print(len(frutas))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list1))
print(list1[-1]) # imprime el ultimo elemento de la lista


l1 = list(("a", "b", "c"))  # creación de lista mediante creacion de un objeto
print(l1[0])

# verificar si un elemento esta en la lista
fruta = "papaya"
if fruta in frutas:
    print(f"{fruta} si esta en frutas")
else:
    print(f"{fruta} no esta en frutas")

frutas[0] = "cereza" # cambiar valor de un elemento
print(frutas)
frutas[2:5] = ["melon", "naranja", "lima"] # cambiar valor en un rango de elementos
print(frutas)
frutas.append("piña") # add an item to the end of list
print(frutas)
frutas.insert(0, "guayaba") # insert item in especific index
print(frutas)

# remove items by index or item
frutas.remove("melon") # remove the specified item
print(frutas)
frutas.pop(0)
print(frutas) # remove the specified index
# del frutas[0] # del also removes the specified index
# print(frutas)
# del frutas # del all the list
frutas.clear() # The clear() method empties the list. The list still remains, but it has no content.
print(frutas)

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)
numbers.reverse()
# What if you want to reverse the order of a list, regardless of the alphabet? The reverse() method reverses the current sorting order of the elements.
print(numbers)

thislist2 = ["apple", "banana", "cherry"]
mylist = thislist2.copy()
print(mylist)


# Join 2 lists
# operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# append
for x in list2:
    list1.append(x)
print(list1)

# extend
l2 = ["s", "a"]
list1.extend(l2)
print(list1)

nElements = list1.count("a")
print(nElements)
