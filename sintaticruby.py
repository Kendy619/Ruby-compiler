import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa
import Visitor as vis
import SemanticVisitor as sv


def p_program1(p):
  '''program : funcdecl'''
  p[0] = sa.ProgramConcrete(p[1])


def p_program2(p):
  '''program : funcdecl program'''
  p[0] = sa.ProgramConcrete(p[1], p[2])


def p_program3(p):
  '''program : class'''
  p[0] = sa.ProgramConcrete(p[1])


def p_program4(p):
  '''program : class program'''
  p[0] = sa.ProgramConcrete(p[1], p[2])


def p_program5(p):
  '''program : stm'''
  p[0] = sa.ProgramConcrete(p[1])


def p_program6(p):
  '''program : stm program'''
  p[0] = sa.ProgramConcrete(p[1], p[2])

  
def p_class_1(p): 
  '''class : CLASS ID funcdecl body
  '''
  p[0] = sa.ClassConcrete(p[1], p[2], p[3], p[4])

def p_class_2(p): 
  '''class : CLASS ID stms body
  '''
  p[0] = sa.ClassConcrete(p[1], p[2], p[3], p[4])




def p_funcdecl(p):
  '''funcdecl : signature body
  '''
  p[0] = sa.FuncDeclConcrete(p[1], p[2])


def p_signature1(p):
    '''signature : DEF ID LPAREN sigParams RPAREN 
    '''
    p[0] = sa.SignatureConcrete(p[1], p[2], p[3], p[4], p[5])

def p_signature2(p):
    '''signature : DEF ID LPAREN RPAREN
    '''
    p[0] = sa.SignatureConcrete(p[1], p[2], p[3], p[4])

def p_signature3(p):
    '''signature : DEF ID
    '''
    p[0] = sa.SignatureConcrete(p[1], p[2])




def p_sigParams1(p):
    '''sigParams : ID'''
      p[0] = sa.SigParamsConcrete(p[1])

def p_sigParams2(p):
    '''sigParams : ID , sigParams'''
      p[0] = sa.SigParamsConcrete(p[1],p[2])


def p_body(p):
    '''body : stms END '''
     p[0] = sa.BodyConcrete(p[1], p[2])


def p_stms1(p):
    '''stms : stm '''
    p[0] = sa.STMSConcrete(p[1])

def p_stms2(p):
    '''stms : stm  stms '''
    p[0] = sa.STMSConcrete(p[1],p[2])



def p_stm1(p):
    '''stm : exp'''
    p[0] = sa.STMConcrete(p[1])

def p_stm2(p):
    '''stm : LPAREN exp RPAREN'''
    p[0] = sa.STMConcrete(p[1],p[2],p[3])

def p_stm3(p):
    '''stm : exp PONTOVIRGULA'''
    p[0] = sa.STMConcrete(p[1],p[2])

def p_stm4(p):
    '''stm : WHILE exp body'''
    p[0] = sa.STMConcrete(p[1],p[2],p[3])

def p_stm5(p):
    '''stm : WHILE LPAREN exp RPAREN body'''
    p[0] = sa.STMConcrete(p[1],p[2],p[3],p[4],p[5])

def p_stm6(p):
    '''stm : FOR ID IN exp DO body''' 
    p[0] = sa.STMConcrete(p[1],p[2],p[4],p[5],p[6])

def p_stm7(p):
    '''stm :  FOR ID IN exp body'''
    p[0] = sa.STMConcrete(p[1],p[2], p[3], p[4], p[5])

def p_stm8(p):
    '''stm : IF exp body'''
    p[0] = sa.STMConcrete(p[1],p[2],P[3])

def p_stm9(p):
    '''stm: IF exp THEN body'''
    p[0] = sa.STMConcrete(p[1],p[2],P[3],p[4])

def p_stm10(p):
    '''stm : exp'''
    p[0] = sa.STMConcrete(p[1])

def p_stm11(p):
    '''stm : IF LPAREN exp RPAREN body'''
    p[0] = sa.STMConcrete(p[1],p[2], p[3], p[4], p[5])

def p_stm12(p):
    '''stm :  IF LPAREN exp RPAREN THEN body'''
p[0] = sa.STMConcrete(p[1],p[2], p[3], p[4], p[5], p[6])

def p_stm13(p):
    '''stm : IF LPAREN exp RPAREN body'''
   p[0] = sa.STMConcrete(p[1],p[2], p[3], p[4], p[5])

def p_stm14(p):
    '''stm : RETURN exp '''
    p[0] = sa.STMConcrete(p[1],p[2])

def p_stm15(p):
    '''stm : RETURN exp PONTOVIRGULA'''
    p[0] = sa.STMConcrete(p[1],p[2],p[3])


def p_exp1(p):
    '''exp : exp PLUS exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp2(p):
    '''exp : exp MINUS exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp3(p):
    '''exp : exp TIMES exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp4(p):
    '''exp : exp DIV exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp5(p):
    '''exp : exp EXPO exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp6(p):
    '''exp : exp REST exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])


  
def p_exp7(p):
    '''exp : exp DOUBLEEQUAL exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp8(p):
    '''exp : exp TRIPLEEQ exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp9(p):
    '''exp : exp SMALL exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp10(p):
    '''exp : exp BIGGEST exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp11(p):
    '''exp : exp DIFF exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
  
def p_exp12(p):
    '''exp : exp POINTRANGE exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])
    
def p_exp13(p):
    '''exp : exp SMALLEQ exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp14(p):
    '''exp : exp BIGGESTEQ exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp15(p):
    '''exp : exp BIGGSMALLEQ exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])




def p_exp16(p):
    '''exp : exp DOUBLEBAR exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp17(p):
    '''exp : exp DOUBLEE exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp18(p):
    '''exp : exp EXCLAMATION exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])


  

def p_exp19(p):
    '''exp : exp SIMPLEBAR exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp20(p):
    '''exp : exp SIMPLEE exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp21(p):
    '''exp : exp CIRCUMFLEX exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp22(p):
    '''exp : exp NEGATION exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp23(p):
    '''exp : exp LSHIFT exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])

def p_exp24(p):
    '''exp : exp RSHIFT exp '''
    p[0] = sa.ExpConcrete(p[1],p[2],p[3])


def p_exp25(p):
    '''exp : call '''
    p[0] = sa.ExpConcrete(p[1])

def p_exp26(p):
    '''exp : assign '''
    p[0] = sa.ExpConcrete(p[1])

def p_exp27(p):
    '''exp : NUM '''
    p[0] = sa.ExpConcrete(p[1])

def p_exp28(p):
    '''exp : ID '''
    p[0] = sa.ExpConcrete(p[1])


  
def p_call1(p):
    '''call : ID LPAREN params RPAREN  '''
    p[0] = sa.CallConcrete(p[1], p[2], p[3], p[4])


def p_call2(p):
    '''call : ID LPAREN RPAREN  '''
    p[0] = sa.CallConcrete(p[1], p[2], p[3])


def p_params1(p):
    '''params :  exp VIRGULA params  '''
    p[0] = sa.ParamsConcrete(p[1], p[2], P[3])


def p_params2(p):
    '''params :  exp '''
    p[0] = sa.ParamsConcrete(p[1])


def p_assign(p):
    '''assign : ID EQ exp '''
    p[0] = sa.AssignConcrete(p[1], p[2], p[3])

def p_error(p):
    print("Syntax error in input!")