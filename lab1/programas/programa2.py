# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
     match = re.findall(r'"user": "(.*)",', texto)

     if not match:
          return ""

     res = []
     [res.append(x) for x in match if x not in res]

     resAux = []

     for x in res:
          contador = 0
          for y in match:
               if x == y:
                    contador += 1
          resAux.append([x,contador])

     ret = resAux[0][0] + ": " + str(resAux[0][1])

     for i in range(1,len(resAux)):
          ret = ret + "\n" + resAux[i][0] + ": " + str(resAux[i][1])

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
