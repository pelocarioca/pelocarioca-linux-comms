#!/usr/bin/python

import sys
from pathlib import Path
import re

arg = sys.argv              #pilla los argumentos del comando

def escribir(a):            #escribe el archivo
    archivo.write("%Generada por resultados.py\n")
    archivo.write("\n")
    for i in range(a):
        i= str(i+1)
        archivo.write("%"+i+" \n")
        archivo.write("\\begin{figure}[H]\n")
        archivo.write("\\centering\n")
        archivo.write("\\includegraphics[scale=0.60]{"+i+"} \n")
        archivo.write("\\caption{} \n")
        archivo.write("\\end{figure}\n")
        archivo.write("\\newpage\n")
        archivo.write("\n")
    archivo.close()

def error(string):
    print("Syntax error: "+string)
    print("Please use 'python3 resultados.py --help' or 'pyhton3 resultados.py -h' for more information.")

try:
    ent = arg[1]
except:
    error('Not enough arguments.')
    sys.exit(1)

#en caso de que el primer argumento sea el de ayuda
if ((str(arg[1]) == '-h') or (str(arg[1]) == '--help')):
    print('Usage: python3 resultados.py {-h, --help | <int> [<dir>]}')
    print("Where:")
    print("   <int> : creates a 'resultados.tex' file in <dir>, if not specified creates the file in the same directory as 'resultados.py', with many figures as <int> indicates.")
    print("   <dir> : Path to the directory where 'resultados.tex' will be created.")
    sys.exit(1)

#si hay demasiados argumentos
if len(arg) > 3:
    error('Too many arguments.')
    sys.exit(1)


#Se comprueba que el primer argumento sea un número (después de la ayuda porque si no siempre tira error)
try:
    ent = int(arg[1])
except:
    error('First argument must be an integer.')
    sys.exit(1)

#Se comprueba que el segundo argumento (path) exista.
try:
    path = Path(str(arg[2]))
except:
    archivo = open("resultados.tex", "w")
    escribir(ent)
    sys.exit(1)

#Si existe el segundo argumento (path).
try:
    if path.is_dir(): #Si existe y es un directorio
        archivo = open(str(path.joinpath('resultados.tex')), "w")
        print(str(path.joinpath('resultados.tex')))
        escribir(ent)
    else:
        if path.parent.exists() and str(arg[2])[-1] != '/': #Si existe y sus padres existen (y no han puesto / al final porque sería un directorio)
            archivo = open(str(path), "w")
            escribir(ent)
        else:   #Si todo falla es porque no existe
            error("El directorio no existe.")

#En caso de que falle cualquier cosa mientras existe el path
except Exception as e:
    print(str(e))
    error("Couldn't create the file.")


sys.exit(1)
