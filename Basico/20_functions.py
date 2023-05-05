def myMsg():
    print('hello world in a function')


myMsg()
            #parameter
def fgreeting(name):
    print(f"Hello {name}")

           #arg
fgreeting('Luis')
fgreeting('manuel')

def fullName(name, last_name):
    print(f"You're {name} {last_name}")

fullName('luis','wzy')

#If you try to call the function with 1 or 3 arguments, you will get an error:
#fullName('luis','abc','dd')#fullName() takes 2 positional arguments but 3 were given
#fullName('luis') #fullName() missing 1 required positional argument: 'last_name'

#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
print('* to many arguments')
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print('keyword Arguments')
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** 
before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
print('**kwargs')
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
"""
print("Default parameter value")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:
"""
print("Passing a List as an Argument")
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

"""
Return Values
To let a function return a value, use the return statement:
"""

print('return values')
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print('mult')
def mult(num):
    multi = []
    for i in range(1,11):
        multi.append(i*num)
    return multi

print(mult(7))

"""
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.
"""
print("pass statement")
def myfunction():
  pass
