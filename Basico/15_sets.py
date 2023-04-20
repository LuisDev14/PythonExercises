thisSet = {1, 2, 3, 4, 5}
thisSet2 = {"a", "b", "c", "d", True, 1, 2}
set3 = {True, False, False, True}
set4 = {1, 1, 1, 2, 2, 3, 4, 5}
print(thisSet)
print(thisSet2)
print(set3)
print(set4)
# access items
for x in thisSet2:
    print(f"valor de thisSet2 {x}")


print(1 in thisSet2)
set4.add("Orange")
print(set4)

# To add items from another set into the current set, use the update() method.
thisset4 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset4.update(tropical)
print(thisset4)

# To remove an item in a set, use the remove(), or the discard() method.
thisset5 = {"apple", "banana", "cherry"}
thisset5.remove("banana")
print(thisset5)
#If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset6 = {"apple", "banana", "cherry"}
thisset6.discard("bananas")
print(thisset6)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

#Remove a random item by using the pop() method:
thisset7 = {"apple", "banana", "cherry"}
x = thisset7.pop()
print(x)
print(thisset7)
# The clear() method empties the set:
thisset8 = {"apple", "banana", "cherry"}
thisset8.clear()
print(thisset8)

# The del keyword will delete the set completely:
thisset9 = {"apple", "banana", "cherry"}
del thisset9
#print(thisset9)