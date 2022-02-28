import secrets
import datetime


negacion = open("partes-normas/negacion","r").read().splitlines()
verbo = open("partes-normas/verbo","r").read().splitlines()
sujeto = open("partes-normas/sujeto","r").read().splitlines()
ccl = open("partes-normas/ccl","r").read().splitlines()
cct = open("partes-normas/cct","r").read().splitlines()
ccm = open("partes-normas/ccm","r").read().splitlines()
consecuencia = open("partes-normas/consecuencia","r").read().splitlines()


def random(a):
    return secrets.choice(a)

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


nombre_archivo = "generadas/output-"+str(datetime.datetime.now()).replace(" ", "_").replace(":", ".")+".txt"
output = open(nombre_archivo, "w")

for i in range(50):
    output.write(locals()['seed' + str(secrets.randbelow(11))]()+"\n")

output.close()
