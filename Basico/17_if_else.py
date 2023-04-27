
"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
a = 330
b = 200
if b > a:
  print("b is greater than a")
else:
    print(b, "is less than ", a)

#elif
note = 95
if note == 100:
    print("Excelente")
elif note >=90:
    print("Bien")
elif note >=80:
    print("Regular")
elif note >=70:
    print("aceptable")
else:
    print("no acreditado")

#If you have only one statement to execute, you can put it on the same line as the if statement.
x = 100
y = 20
if x>y:print("x es mayor ",x)
#
print(x,"si es mayor x") if x>y else print(y,"es mayor y")



name = 'alex'
password = 4567
#example 1
if name == 'luis' and password == 4567:
    print(f"Welcome {name}")
#example 2
if name == 'alex' or name =='luis' and password == 4567:
    print(f'Welcome {name}')
#operador not
if not name == 'luis':
    print('El nombre no es luis')

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


string = ""

if not string:
    print("El string está vacío")
else:
    print("El string no está vacío")

#Nested If
nombre = "luis"
passw = 1234
if nombre == "luis":
    print(f"Welcome {nombre}")
    if nombre == "luis" and passw == 1234:
        print(f"Welcome to the world {nombre}")
    else:
        print("Incorrect password")
else:
    print(f"{nombre} no tiene acceso")


"""
La sentencia pass en Python es una operación nula que no hace nada. A veces se utiliza como marcador de posición en el código, para indicar que se debe realizar una tarea o 
implementar una función en una sección determinada del código, pero que todavía no se ha hecho
"""
n1 = 123
n2 = 456
if n1>n2:
    print(f"{n1} es mayor")
else:
    pass

