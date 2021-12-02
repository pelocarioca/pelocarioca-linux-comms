#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:18:28 2021

@author: cassio
"""
#Se importan los módulos necesarios.
import secrets
import string
import sys
import qrcode
from datetime import datetime

#Se declaran las variables, x para el resultado, los diccionarios de palabras
# y los caracteres. (NOTA: Los diccionarios se encuentran en esa dirección en Linux Mint 20.1 Ulyssa)
x=""
diccionario_ing = open('/usr/share/dict/spanish')
diccionario_sp = open('/usr/share/dict/words')
caracteres = string.ascii_uppercase + string.ascii_letters + string.digits + string.hexdigits + string.punctuation + "ḉçÇḈñÑ"


#Función de salida, toma el secrets.choice sobre la lista escogida (puede ser 
# o los diccionarios o los caracteres, depende de la respuesta incial).
def salida(rango, inp1, x, lista, img):
    
    #En el rango del rango (numero de caracteres o palabras):
    for i in range(rango):
        #Si se escogió sí a que sea human readable, esto añade un espacio al 
        # final de cada palabra.
        if inp1 == "y" or inp1 == "Y":
            x += secrets.choice(lista) + " "        
        #Si se escogió que no, no añade espacio después de cada carácter.
        else:
            x += secrets.choice(lista)
    #Por último, si se escoge que se genere una img qr la guarda:
    if img:
        nombre="qr"+str(datetime.now())+".png"
        qrcode.make(x).save(nombre)
        print()
        print("Se ha creado una imagen qr con la contraseña: " + nombre)
    #Print de los espacios y el resultado.
    print()
    print(x)
    print()

#Funcion que pregunta si generar QR:
def imgqr():
    
    #Pregunta si genera QR:
    inpqr = (input("¿Generar imagen QR?((Y)es/(n)o): ") or "Y")
    if inpqr == "y" or inpqr == "Y":
        
        #Mete a inputs que sea True, genera qr.
        inputs(True)
        
    elif inpqr == "n" or inpqr == "N":
        
        #Mete a inputs que sea False, no genera qr.
        inputs(False)
        
    else: 
        imgqr()


#Función que define los inputs:
def inputs(img):
    #Aquí se escoge si se genera una passphrase o una contraseña.
    #El valor por defecto es "Y"
    inp1 = input("¿Passphrase o contraseña?((p)assphrase/pass(w)ord/(c)ancelar): ")
    
    #En caso de que sí, se genera una passphrase
    if inp1 == "p" or inp1 == "P":
        
        #Se añaden a la lista los diccionarios español y genérico del sistema
        # operativo, sólo para Linux.
        lista = [word.strip() for word in diccionario_sp]
        lista += [word.strip() for word in diccionario_ing]
        
        #Número de palabras para la passphrase.
        inp2 = (input("¿Número de palabras para la contraseña?(6): ") or 6)
        
        #Comprueba que inp2 sea un INT, si nó se asigna el valor por defecto 
        # y se continúa
        try:
            rango = int(inp2)
        except ValueError:
            rango = 6
            print("ADVERTENCIA: Se va a tomar el número de palabras por defecto; 6.")
        
        #Función de salida asignando las variables del sí.
        salida(rango, inp1, x, lista, img)
    
    #En caso de que no, se genera una contraseña.
    elif inp1 == "c" or inp1 == "C":
        
        #Se añaden a la lista el diccionario de caracteres.
        lista = caracteres
        
        #Número de caracteres para la contraseña.
        inp2 = (input("¿Número de caracteres de la contraseña?(16): ") or 16)
        
        #Comprueba que inp2 sea un INT, si nó se asigna el valor por defecto 
        # y se continúa
        try:
            rango = int(inp2)
        except ValueError:
            rango = 32
            print("ADVERTENCIA: Se va a tomar el número de caracteres por defecto; 32.")
        
        #Función de salida asignando las variables del no.
        salida(rango, inp1, x, lista, img)
            
    #En caso de que se aborte el programa, se hace una salida.
    elif inp1 == "c" or inp1 == "C":
        
        #Salida con mensaje de excepción.
        sys.exit("Se ha cerrado el keygen")
    
    #En caso de que no se escoja ni Y, ni N, ni C, vuelve a ejecutar la
    # función de los inputs, pueden surgir problemas si no se escoje ninguna 
    # opción múltiples veces.
    else:
       inputs(img)
       
#Este es el principio del programa.
imgqr()
