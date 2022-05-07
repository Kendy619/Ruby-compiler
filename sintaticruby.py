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

'''

class -> "class" ID funcdecl body |
         "class" ID  stms  body | 

'''

def p_class_1(p): 
  '''class : CLASS ID funcdecl body
  '''
  p[0] = sa.FuncDeclConcrete(p[1], p[2], p[3], p[4])

def p_class_2(p): 
  '''class : CLASS ID stms body
  '''
  p[0] = sa.FuncDeclConcrete(p[1], p[2], p[3], p[4])


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
