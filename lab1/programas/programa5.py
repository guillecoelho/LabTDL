# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):

    res = re.sub(r'###(.*)\\n',r'<h3>\1</h3>\\n',texto)
    res = re.sub(r'##(.*)\\n',r'<h2>\1</h2>\\n',res)
    res = re.sub(r'#(.*)\\n',r'<h1>\1</h1>\\n',res)

    res = re.sub(r'\*\*(.*)\*\*',r'<strong>\1</strong>',res)
    res = re.sub(r'\*(.*)\*',r'<em>\1</em>',res)

    res = re.sub(r'~~(.*)~~',r'<s>\1</s>',res)

    return res 

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