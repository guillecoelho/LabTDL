# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
     match = re.findall(r'@(.*?)\W', texto)

     if not match:
          return ""

     res = []
     [res.append(x) for x in match if x not in res]

     ret = res[0]

     for i in range(1,len(res)):
          ret = ret + "\n" + res[i]

     ret = f"{ret}"
     
     return ret

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
