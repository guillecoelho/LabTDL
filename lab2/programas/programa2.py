# -*- coding: utf-8 -*-

import sys
import io
import nltk

def replace(tree):
     if isinstance(tree, nltk.Tree):
          if tree.label() == 'S' or tree.label() == 'A':
               if len(tree) == 5:
                    left_operand = replace(tree[1])
                    operator = tree[2]
                    right_operand = replace(tree[3])
                    return f'{operator}({left_operand},{right_operand})'
               elif len(tree) == 3:
                    left_operand = replace(tree[0])
                    operator = tree[1]
                    right_operand = replace(tree[2])
                    return f'{operator}({left_operand},{right_operand})'
               elif len(tree) == 1:
                    return replace(tree[0])
          elif tree.label() == 'X':
               return tree.leaves()[0]
     return ''.join(tree.leaves())

# grammar definition
grammar = """
S -> A '+' A | A '-' A | A '/' A | A '*' A | X
A -> '(' A '+' A ')' | '(' A '-' A ')' | '(' A '*' A ')' | '(' A '/' A ')' | X
X -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
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
               salida = replace(tree[0])
          else:
               salida = "NO PERTENECE"
     except ValueError:
          salida = "NO PERTENECE - FUERA DE ALFABETO"
     f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
     f.write(salida)
     f.close()
