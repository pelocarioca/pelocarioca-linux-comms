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

#Se declaran las variables, x para el resultado, los diccionarios de palabras
# y los caracteres.
x=""
diccionario_ing = open('/usr/share/dict/spanish')
diccionario_sp = open('/usr/share/dict/words')
caracteres = string.ascii_uppercase + string.ascii_letters + string.digits + string.hexdigits + string.punctuation + "ḉçÇḈ"


#Función de salida, toma el secrets.choice sobre la lista escogida (puede ser 
# o los diccionarios o los caracteres, depende de la respuesta incial).
def salida(rango, inp1, x, lista):
    
    #En el rango del rango (numero de caracteres o palabras):
    for i in range(rango):
        #Si se escogió sí a que sea human readable, esto añade un espacio al 
        # final de cada palabra.
        if inp1 == "y" or inp1 == "Y":
            x += secrets.choice(lista) + " "        
        #Si se escogió que no, no añade espacio después de cada carácter.
        else:
            x += secrets.choice(lista)
    #Print de los espacios y el resultado.
    print()
    print(x)
    print()

#Función que define los inputs:
def inputs():
    #Aquí se escoge si se genera una passphrase o una contraseña.
    #El valor por defecto es "Y"
    inp1 = (input("¿Legible por humanos?(Y/n/c): ") or "Y")
    
    #En caso de que sí, se genera una passphrase
    if inp1 == "y" or inp1 == "Y":
        
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
        salida(rango, inp1, x, lista)
    
    #En caso de que no, se genera una contraseña.
    elif inp1 == "n" or inp1 == "N":
        
        #Se añaden a la lista el diccionario de caracteres.
        lista = caracteres
        
        #Número de caracteres para la contraseña.
        inp2 = (input("¿Número de caracteres de la contraseña?(32): ") or 32)
        
        #Comprueba que inp2 sea un INT, si nó se asigna el valor por defecto 
        # y se continúa
        try:
            rango = int(inp2)
        except ValueError:
            rango = 32
            print("ADVERTENCIA: Se va a tomar el número de caracteres por defecto; 32.")
        
        #Función de salida asignando las variables del no.
        salida(rango, inp1, x, lista)
            
    #En caso de que se aborte el programa, se hace una salida.
    elif inp1 == "c" or inp1 == "C":
        
        #Salida con mensaje de excepción.
        sys.exit("Se ha cerrado el keygen")
    
    #En caso de que no se escoja ni Y, ni N, ni C, vuelve a ejecutar la
    # función de los inputs, pueden surgir problemas si no se escoje ninguna 
    # opción múltiples veces.
    else:
       inputs()
       
#Este es el principio del programa, en el que se ejecuta inputs().
inputs()