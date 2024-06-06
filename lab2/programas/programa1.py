# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl

# grammar definition
grammar = """
S -> S1 | S2 | S3
S1 -> A B
A -> '0' A '1' | '0' '1'
B -> '2' B | '2'
S2 -> C D
C -> '0' C | '0'
D -> '1' '1' D '2' | '1' '1' '2'
S3 -> '0' '0' '0' S3 '2' | '0' '0' '0' E '2'
E -> '1' E | '1'
"""

def parse(s, grammar):
     # parser
     grammar = nltk.CFG.fromstring(grammar)
     parser = nltk.LeftCornerChartParser(grammar)

     # tokenize
     s_tokenized = nltk.word_tokenize(s)

     # parse
     tree = list(parser.parse(s_tokenized))[:1]
     return tree

if __name__ == '__main__':
     archivo_entrada = sys.argv[1]
     archivo_salida = sys.argv[2]
     f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
     s = f.read()
     f.close()
     try:
          tree = parse(s, grammar)
          if tree:
               salida = "PERTENECE"
          else:
               salida = "NO PERTENECE"
     except ValueError:
          salida = "NO PERTENECE - FUERA DE ALFABETO"
     f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
     f.write(salida)
     f.close()
