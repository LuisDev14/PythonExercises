 #Operadores aritmeticos
x = 10
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y) #the floor division // rounds the result down to the nearest whole number

#Operadores de asignacion
#Son usados para asignar valores a las variables
print("Operadores de asignacion")
x=5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)

x %= 3
print(x)

x //= 3
print(x)

print("y")
y = 15
y**=3 #y=y**3
print(y)

#operadores a nivel de bit
n1= 5
n2 = 3
print(bin(n1))
print(bin(n2))
print(bin(-4))

print(n1&n2)
print(n1|n2)
print(n1^n2)
print(~5)


print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
print(100 + 5 * 3)

print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""