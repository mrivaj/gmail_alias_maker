#!/usr/bin/python
from random import randint

valores_dni = {0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D',10:'X',11:'B',
              12:'N',13:'J',14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E'}

def construye_dni(dni_sin_letra):
  dni = str(dni_sin_letra) + obtener_letra(dni_sin_letra) 
  return dni

def obtener_letra(dni_sin_letra):
  return valores_dni.get(int(dni_sin_letra) % 23)

def valida_dni(dni):
  return obtener_letra(dni[0:8]) == dni[8]
  
def generar_dni():
  dni = "4"
  for number in range(7):
    dni += str(randint(0,9))
  dni += obtener_letra(dni)
  if (valida_dni(dni)):
    return dni
  else:
    generar_dni()
