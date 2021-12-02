#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:18:28 2021

@author: cassio
"""
import secrets
import string

lista= string.ascii_uppercase + string.ascii_letters + string.digits + string.hexdigits + string.punctuation + "ḉçÇḈ"
x=""
y=""


inp2 = input("¿Número de caracteres de la contraseña?(32): ")
try:
    inp2 = int(inp2)
    rango = int(inp2 or 32)
except ValueError:
    rango = 32
    print("ADVERTENCIA: Se va a tomar el número de caracteres por defecto; 32.")




rng = secrets.SystemRandom(); 
for i in range(rango):
    x += secrets.choice(lista)
    y += '-'
    
print(y)
print(x)



