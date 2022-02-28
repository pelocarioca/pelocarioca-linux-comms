"""
Para poder elegir números aleatorios, y de esta forma seleccionar las partes de
las normas aleatoriamente, se requiere de un módulo específico llamado "secrets".
Se le llama con la línea 8 y para utilizar sus funciones se le trata como
un objeto.
"""
import secrets

"""
Se van a generar archivos con normas, para que cada vez que se ejecute el generador
no se sobreescriba el anterior archivo se incluirá la fecha y hora en que se crearon.
Para esto se utiliza el módulo "datetime", que puede dar la fecha y hora momentáneamente.
"""
import datetime

"""
Se toman las variables para construir las frases, para ello se lee un archivo y
se forma un array (una "lista") con las líneas de texto de cada archivo.

Las líneas de lectura de los archivos tienen tres partes:

    (negacion =) - Se asigna el array de la lectura del archivo a la variable "negacion".
    (open("partes-normas/negacion","r")) - Lee el archivo "negacion" de la carpeta "partes-normas".
    (.read().splitlines())  - Asigna cada línea del archivo a un ítem del array.

De esta forma la variable "negacion" terminaría funcionando como:

negacion["no", "jamás",(...)]

Aligerando así el código del generador
"""
negacion = open("partes-normas/negacion","r").read().splitlines()
verbo = open("partes-normas/verbo","r").read().splitlines()
sujeto = open("partes-normas/sujeto","r").read().splitlines()
ccl = open("partes-normas/ccl","r").read().splitlines()
cct = open("partes-normas/cct","r").read().splitlines()
ccm = open("partes-normas/ccm","r").read().splitlines()
consecuencia = open("partes-normas/consecuencia","r").read().splitlines()

"""
Para hacer más visual el código, se va a crear un alias de la función "choice()"
del módulo secrets llamado "random()", así cada vez que se quiera seleccionar un
elemento aleatorio de un array de datos aparecerá como "random(y)" en vez de como
"secrets.choice(y)". Esto es puramente visual.
"""
def random(a):
    return secrets.choice(a)

"""
Ahora se definen las funciones que actúan como seeds, cada seed es una estructura
de normas, de esta forma las seeds (denominadas seed0, seed1,...seed10) tienen
diferentes componentes, como una negación, un complemento circunstancial de un tipo
u otro o una consecuencia. De esta forma se crean frases con diversas estructuras,
lo que hace menos repetitivas las normas.

El funcionamiento de una seed N es el siguiente:

    def seedN():                        - Es la declaración de la función.
        x=""                            - Inicializa la variable x, en la que se añadirán las partes de la norma.
        x += random(negacion) + " "     - Añade a la variable x vacía una negación aleatoria y añade un espacio.
        x += random(verbo) + " "        - Añade a la negación y al espacio un verbo aleatorio con un espacio delante.
        x += random(sujeto) + " "       - Añade a la negación y al verbo un sujeto. Añade un espacio delante, aunque no es necesario.
        return x.strip("_ ")            - Devuelve la norma guardada en la variable x, le quita un posible "_"
                                        del archivo de negaciones. Al devolver la variable esta se convierte en
                                        la salida de la funcion, es como si fuera su resultado.

Se pueden añadir y quitar partes a las seeds para dar variedad a las frases.
"""

def seed0():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(cct) + " "
    x += random(ccm) + " "
    x += random(consecuencia) + " "
    return x.strip("_ ")


def seed1():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    return x.strip("_ ")


def seed2():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(ccm) + " "
    return x.strip("_ ")

def seed3():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    #x += random(consecuencia) + " "
    return x.strip("_ ")

def seed4():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(cct) + " "
    x += random(ccm) + " "
    return x.strip("_ ")

def seed5():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(consecuencia) + " "
    return x.strip("_ ")

def seed6():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(cct) + " "
    return x.strip("_ ")

def seed7():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccm) + " "
    return x.strip("_ ")

def seed8():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccm) + " "
    #x += random(consecuencia) + " "
    return x.strip("_ ")

def seed9():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(cct) + " "
    return x.strip("_ ")

def seed10():
    x=""
    x += random(negacion) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(cct) + " "
    x += random(ccm) + " "
    #x += random(consecuencia) + " "
    return x.strip("_ ")

"""
Ahora se crea el nombre del archivo, que tendrá la estructura:

output-YYYY-MM-DD_HH.MM.SS.mmmmm.txt

    "generadas/output-"+            - Guarda en la carpeta "generadas", el nombre del archivo comienza por "output".

    str(datetime.datetime.now()).replace(" ", "_").replace(":", ".")+   - Obtiene la fecha y hora y las formatea.

    ".txt"          - Terminación del archivo, al ser este de texto.

En la siguiente línea a la de la inicialización de nombre_archivo se "crea"
(abre) un archivo vacío con ese nombre, la opción "w" indica que se va a escribir.
"""
nombre_archivo = "generadas/output-"+str(datetime.datetime.now()).replace(" ", "_").replace(":", ".")+".txt"
output = open(nombre_archivo, "w")

"""
Ahora se utiliza un bucle para que se añadan 50 normas generadas aleatoriamente
al archivo abierto. Ahora se explicarán las partes de la línea de output.(...):

    output.write(...)               - Lo que se encuentre dentro del paréntesis se va a escribir en el archivo abierto.

    locals()[...]() + "\n"          - locals() se trata de una "lista" con las funciones del programa,
                                    entre otras funciones de python se encuentran las seeds. Para seleccionar una seed
                                    en concreto se utilizan los corchetes, de forma que entre ellos se escribe el nombre
                                    de la función que se quiera utilizar. Si a este locals()[...] se le añade un paréntesis
                                    "()", se ejecutará la función que se haya escrito en los corchetes.
                                        Por ejemplo "locals()[seed5]()" ejecutará la función seed5().
                                    Esto se utiliza porque interesa que lo que se ejecute (lo que hay entre los corchetes)
                                    sea aleatorio. Y esto es más sencillo si se llama a la seed desde locals().
                                    Por último, el (+ "\n")  sirve para que haya un salto de línea al final de cada norma.

    'seed' + str(secrets.randbelow(11))     - Esto es lo que se encontraría dentro de los corchetes, de igual forma que con
                                            el nombre del archivo se le añade a la palabra "seed" un número aleatorio por
                                            debajo de 11. Este número debe ser convertido a formato texto para poderse adjuntar
                                            a seed, de ahí que se utilice el str(...).

En conclusión, por cada iteración del bucle se añade al archivo el "resultado"
(la norma correspondiente) de una de las funciones seed. Siendo esta elegida
aleatoriamente.
"""
for i in range(50):
    output.write(locals()['seed' + str(secrets.randbelow(11))]()+"\n")

"""
Por último, se cierra el archivo abierto con close(). Esto se suele utilizar
para que en archivos grandes la memoria del ordenador no se sobrecargue, en este
caso no resulta del todo necesario pero se trata de una buena práctica de programación.
"""
output.close()
