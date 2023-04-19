import os
fileName = "abcw.txt"
mypath = f"C:/Users/luick/Downloads/{fileName}"

op = int(input("1.-read file\n2.-remove file\n"))
existeRuta = False
match op:
    case 1:
        #open file
        if os.path.exists(mypath):
            with open(mypath, 'r') as archivo:
                contenido = archivo.read()
                archivo.close()
                print(contenido)
        else:
            print("El archivo no existe en la ruta especificada.")
    case 2:
        resp = str(input("Deseas eliminar el archivo: " + fileName + " y | n: "))
        if resp == "y":
            if os.path.exists(mypath):
                os.remove(mypath)
                print(f"{mypath} se ha eliminado correctamente")
        elif resp == "n":
            print(f"{fileName} se ha conservado en {mypath}")
print("Fin")
