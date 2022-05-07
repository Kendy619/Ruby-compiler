import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa
import Visitor as vis
import SemanticVisitor as sv

'''
signature -> "def" ID "(" sigParams ")" | 
              "def" ID  sigParams |
              "def" ID
'''

def p_program(p):
  '''program : funcdecl
             | funcdecl program
             | exp
             | exp program
  '''
 #como diferenciar o tipo de expressão aqui? já que apenas pelo tamanho não é possível


def p_funcdecl(p):
  '''funcdecl : signature body
  '''
  p[0] = sa.FuncDeclConcrete(p[1], p[2])

def p_signature(p):
  '''signature : DEF ID LPAREN sigParams RPAREN 
               | DEF ID sigParams
               | DEF ID
  '''
  #ou seria:
    '''signature : DEF ID LPAREN sigParams RPAREN 
               | DEF ID LPAREN RPAREN
               | DEF ID
    '''
