import secrets
import datetime
from time import sleep

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
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")


def seed1():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")


def seed2():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(ccm) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed3():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    #x += random(consecuencia) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed4():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(cct) + " "
    x += random(ccm) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed5():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(consecuencia) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed6():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(cct) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed7():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccm) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed8():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccm) + " "
    #x += random(consecuencia) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed9():
    x=""
    x += random(negacion) + " "
    x += random(verbo) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(cct) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")

def seed10():
    x=""
    x += random(negacion) + " "
    x += random(sujeto) + " "
    x += random(ccl) + " "
    x += random(cct) + " "
    x += random(ccm) + " "
    #x += random(consecuencia) + " "
    print(x.strip("_ "))
    sleep(0.45)
    return x.strip("_ ")


while True:
    locals()['seed' + str(secrets.randbelow(11))]()+"\n"

