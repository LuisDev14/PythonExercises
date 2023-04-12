for i in range(255):
    print("{0}: {1}".format(i, repr(chr(i))))

print('\x1f')
print(chr(0))
print(ord("@"))
print(repr(chr(0)) + repr(chr(1)))


print("☺☻")
print(ord("☺"))
print(ord("☻"))
print(ord("?"))
print(ord(' '))
print(ord('♦'))