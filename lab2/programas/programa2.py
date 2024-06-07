# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl

from nltk.tree import Tree

from nltk.parse.generate import generate

from nltk import CFG

def replace(tree):

     return ''

# grammar definition
grammarCFG = CFG.fromstring("""
S -> S '+' S | S '-' S | S '/' S | S '*' S | N
N -> X | X X | X '0' | '100' | '0'
X -> '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

grammar = """
S -> A '+' A | A '-' A | A '/' A | A '*' A | N
A -> '(' A '+' A ')' | '(' A '-' A ')' | '(' A '*' A ')' | '(' A '/' A ')' | N
N -> X | X X | X '0' | '100' | '0'
X -> '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
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
     #print(grammarCFG.start())
     #print(grammarCFG.productions())
     #for s in generate(grammarCFG, n=3):
     #     print(' '.join(s))
     archivo_entrada = sys.argv[1]
     archivo_salida = sys.argv[2]
     f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
     s = f.read()
     f.close()
     try:
          tree = parse(s, grammar)
          if tree:
               #tree[0].draw()
               #print(tree[0])
               #print(replace(tree[0]))
               salida = "PERTENECE"
          else:
               salida = "NO PERTENECE"
     except ValueError:
          salida = "NO PERTENECE - FUERA DE ALFABETO"
     f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
     f.write(salida)
     f.close()
