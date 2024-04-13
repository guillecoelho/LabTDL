# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    meses=["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"] #Convertir número mes a su nombre en español.

    match = re.findall(r'"timestamp": "T (\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}):\d{2}"', texto)

    if not match:
      return ""

    ret = ""
    for tupla in match:
      ret = ret + tupla[2] + " de " + meses[int(tupla[1])] + " del " + tupla[0] + " a las " + tupla[3]+":"+tupla[4] +" hs." + "\n"

    return ret[0:len(ret)-1] #Elimino el último salto de linea 

if __name__ == '__main__':
     entrada = sys.argv[1]  # archivo entrada (param)
     salida = sys.argv[2]   # archivo salida (param)

     f = open(entrada, 'r') # abrir archivo entrada
     datos = f.read()       # leer archivo entrada
     f.close()              # cerrar archivo entrada

     ret = prog(datos)      # ejecutar er

     f = open(salida, 'w')  # abrir archivo salida
     f.write(ret)           # escribir archivo salida
     f.close()              # cerrar archivo salida
