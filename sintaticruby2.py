import ply.yacc as yacc
from compiler_ruby import *

def p_program1(p):
  '''program : funcdecl'''
  pass

def p_program2(p):
  '''program : funcdecl program'''

def p_program5(p):
  '''program : stm'''
  pass

def p_program6(p):
  '''program : stm program'''
  pass
  
def p_program7(p):
  '''program : call'''  
  pass

def p_funcdecl(p):
  '''funcdecl : signature body'''
  pass
  
def p_signature3(p):
  '''signature : DEF ID'''
  pass
  
def p_body(p):
  '''body : stms END '''
  pass

def p_stms1(p):
  '''stms : stm '''
  pass
  
def p_stms2(p):
  '''stms : stm  stms '''
  pass

def p_stm1(p):
  '''stm : exp'''
  pass

def p_stm3(p):
  '''stm : exp PONTOVIRGULA'''
  pass






def p_if(p):
    '''stm : s'''
    pass
  
def p_s(p):
    ''' s : s1 
          | s2 '''
    pass

def p_s1_if0(p):
    ''' s1 : stms 
    '''
    pass


def p_s1_if1_params(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE s1 
    '''
    pass

def p_s1_if2_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE body 
    '''
    pass

def p_s1_if3_params(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE body 
    '''
    pass

def p_s1_if4_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE s1 
    '''
    pass
  


def p_s2_if1_params(p):
    ''' s2 :  IF LPAREN exp RPAREN s1 ELSE s1
    '''
    pass

def p_s2_if2_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body
    '''
    pass

def p_s2_if3_params(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE s2 
    '''
    pass

def p_s2_if4_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE s2
    '''
    pass


def p_s1_if1_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN s1 ELSE s1 
    '''
    pass

def p_s1_if2_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body ELSE body 
    '''
    pass

def p_s1_if3_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN s1 ELSE body 
    '''
    pass

def p_s1_if4_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body ELSE s1 
    '''
    pass
  

def p_s2_if1_params_then(p):
    ''' s2 :  IF LPAREN exp RPAREN THEN s1 ELSE s1
    '''
    pass

def p_s2_if2_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body
    '''
    pass

def p_s2_if3_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN s1 ELSE s2 
    '''
    pass

def p_s2_if4_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body ELSE s2
    '''
    pass


def p_s1_if1_noParen(p):
    ''' s1 :  IF exp s1 ELSE s1 
    '''
    pass

def p_s1_if2_noParen(p):
    ''' s1 :  IF exp body ELSE body 
    '''
    pass

def p_s1_if3_noParen(p):
    ''' s1 :  IF exp s1 ELSE body 
    '''
    pass

def p_s1_if4_noParen(p):
    ''' s1 :  IF exp body ELSE s1 
    '''
    pass

def p_s2_if1_noParen(p):
    ''' s2 :  IF exp s1 ELSE s1
    '''
    pass

def p_s2_if2_noParen(p):
    ''' s1 :  IF exp body
    '''
    pass

def p_s2_if4_noParen(p):
    ''' s1 :  IF exp body ELSE s2
    '''
    pass



def p_s1_if1_noParen_then(p):
    ''' s1 :  IF exp THEN s1 ELSE s1 
    '''
    pass

def p_s1_if2_noParen_then(p):
    ''' s1 :  IF exp THEN body ELSE body 
    '''
    pass

def p_s1_if3_noParen_then(p):
    ''' s1 :  IF exp THEN s1 ELSE body 
    '''
    pass

def p_s1_if4_noParen_then(p):
    ''' s1 :  IF exp THEN body ELSE s1 
    '''
    pass
  



def p_s2_if1_noParen_then(p):
    ''' s2 :  IF exp THEN s2  ELSE s2
    '''
    pass

def p_s2_if2_noParen_then(p):
    ''' s1 :  IF exp THEN body
    '''
    pass

def p_s2_if3_noParen_then(p):
    ''' s1 :  IF exp THEN s1 ELSE s2 
    '''
    pass

def p_s2_if4_noParen_then(p):
    ''' s1 :  IF exp THEN body ELSE s2
    '''
    pass






  
  

  
#def p_stm8(p):
#  '''stm : IF exp body'''
#  pass
  
#def p_stm9(p):
#  '''stm : IF exp THEN body'''
#  pass

#def p_stm10(p):
#  '''stm : IF LPAREN exp RPAREN body'''
#  pass

#def p_stm11(p):
##  '''stm :  IF LPAREN exp RPAREN THEN body'''
#  #pass

def p_stm12(p):
  '''stm : RETURN exp '''
  pass

def p_stm13(p):
  '''stm : RETURN exp PONTOVIRGULA'''
  pass 

def p_exp25(p):
  '''exp : call '''
  pass
  
def p_exp26(p):
  '''exp : assign '''
  pass

def p_exp27(p):
  '''exp : NUMBER '''
  pass

def p_exp29(p):
  '''exp : STRING '''
  pass

def p_exp28(p):
  '''exp : ID '''
  pass
  
def p_exp7(p):
    '''exp : exp DOUBLEEQUAL exp '''
    pass


def p_assign(p):
  '''assign : ID EQ exp '''
  pass

def p_call1(p):
  '''call : ID LPAREN params RPAREN  '''
  pass
  
def p_call2(p):
  '''call : ID LPAREN RPAREN '''
  pass

def p_params1(p):
    '''params :  exp VIRGULA params  '''
    pass

def p_params2(p):
    '''params :  exp '''
    pass

def p_error(p):
  print("Syntax error in input!")