i = 1
while i <= 10:
    print(i)
    i += 1
#With the break statement we can stop the loop even if the while condition is true:
print('Break ')
j = 0
while j < 8:
    print(j)
    if j == 5:
        print('Finish')
        break
    j = j+1
#With the continue statement we can stop the current iteration, and continue with the next:
print('continue statement')
k = 0
while k < 10:
    print(k)
    k = k+1
    if k == 7:
        print('continue')
#With the else statement we can run a block of code once when the condition no longer is true:
print('Else statements')
z = 1
while z < 10:
    print(z)
    z = z+1
else:
    print(f'{z} es mayor o igual que 10')
