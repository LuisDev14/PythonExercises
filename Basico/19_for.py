fruits = ['apple', 'pineapple', 'grape', 'orange', 'strawberry']

for x in fruits:
    print(x)

fruit = 'banana'
for x in fruit:
    print(x)

print('Break statement')
fruits2 = ['apple', 'pineapple', 'grape', 'orange', 'strawberry']

for x2 in fruits2:
    print(x2)
    if x2 == "grape":
        break
print('continue statement')
for x2 in fruits2:
    print(x2)
    if x2 == "grape":
        continue

'''
o loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
'''
print('range')
for x in range(10):
    print(x)
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
print('range 2 to 6')
for x in range(2,6):
    print(x)
print('start, end, increment')
for x in range(1,10,2):
    print(x)

"""
Nested Loops
"""
print('Nested Loops')
numbers = [1, 2, 3, 4]
fruits3 = ['apple', 'pineapple', 'grape', 'orange']
for n in numbers:
    for f in fruits3:
        print(n,f)

print('pass example')
for y in [0, 1, 2, 4]:
    pass