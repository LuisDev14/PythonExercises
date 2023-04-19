
"""
ruta = 'C:/Users/luick/Downloads/xarchivo1495.txt'
with open(ruta, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

"""


import os

ruta = 'C:/Users/l/Downloads/abcw.txt'

if os.path.exists(ruta):
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe en la ruta especificada.")

