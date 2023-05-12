"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Sintax
lambda arguments : expression
"""
x = lambda a: a+10
print(x(4))

funL = lambda a, b: a*b
print(funL(4,5))

funL = lambda a, b, c: a+b+c
print(funL(4,8,23))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#lambda function
square = lambda x:x**2
print(square(5))

#traditional function
def funSquare(x):
    return x**2
print(funSquare(3))


lambda_func = lambda x: True if x**2 >= 10 else False
lambda_func(3) # Retorna False
lambda_func(4) # Retorna True


def myfunc(n):
  return lambda a : a * n


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
