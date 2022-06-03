import ply.yacc as yacc
from compiler_ruby import *

def p_program1(p):
  '''program : funcdecl'''
  pass

def p_program2(p):
  '''program : funcdecl program'''

#def p_program3(p):
#  '''program : class'''
#  pass

#def p_program4(p):
#  '''program : class program'''
#  pass

def p_program5(p):
  '''program : stm'''
  pass

def p_program6(p):
  '''program : stm program'''
  pass
  
def p_program7(p):
  '''program : call'''  
  pass









  
#def p_class_1(p): 
#  '''class : CLASS ID  END
#  '''
#  pass



#def p_class_1(p): 
#  '''class : CLASS ID funcdecl body
#  '''
#  pass

#def p_class_2(p): 
#  '''class : CLASS ID stms body
#  '''
#  pass

#def p_bodyclass_1(p): 
#  '''bodyclass : funcdecl END
#  '''
#  pass

#def p_bodyclass_2(p): 
#  '''bodyclass : attrdecl END
#  '''
#  pass

#def p_bodyclass_3(p): 
#  '''bodyclass : funcdecl bodyclass END
#  '''
#  pass

#def p_bodyclass_4(p): 
#  '''bodyclass : attrdecl bodyclass END
#  '''
#  pass














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





def p_stm_while(p):
    '''stm : WHILE exp body'''
    pass
  
def p_stm_while_paren(p):
    '''stm : WHILE LPAREN exp RPAREN body'''
    pass
  
def p_stm_while_do(p):
    '''stm : WHILE exp DO body'''
    pass 

def p_stm_while_do_paren(p):
  '''stm : WHILE LPAREN exp RPAREN DO body'''
  pass

def p_stm_for(p):
  '''stm : FOR ID IN ID body'''
  pass

def p_stm_for_do(p):
  '''stm : FOR ID IN ID DO body'''
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

def p_stm_return(p):
  '''stm : RETURN exp '''
  pass

def p_stm_return_pontoVirgula(p):
  '''stm : RETURN exp PONTOVIRGULA'''
  pass 


def p_exp1(p):
    '''exp : exp PLUS exp '''
    pass
  
def p_exp2(p):
    '''exp : exp MINUS exp '''
    pass
  
def p_exp3(p):
    '''exp : exp TIMES exp '''
    pass
  
def p_exp4(p):
    '''exp : exp DIV exp '''
    pass
  
def p_exp5(p):
    '''exp : exp EXPO exp '''
    pass




def p_exp6(p):
    '''exp : exp REST exp '''
    pass

def p_exp7(p):
    '''exp : exp DOUBLEEQUAL exp '''
    pass
  
def p_exp8(p):
    '''exp : exp TRIPLEEQ exp '''
    pass
  
def p_exp9(p):
    '''exp : exp SMALL exp '''
    pass
  
def p_exp10(p):
    '''exp : exp BIGGEST exp '''
    pass
  
def p_exp11(p):
    '''exp : exp DIFF exp '''
    pass
  
def p_exp12(p):
    '''exp : exp POINTRANGE exp '''
    pass
    
def p_exp13(p):
    '''exp : exp SMALLEQ exp '''
    pass
  
def p_exp14(p):
    '''exp : exp BIGGESTEQ exp '''
    pass
  
def p_exp15(p):
    '''exp : exp BIGGSMALLEQ exp '''
    pass
  
def p_exp16(p):
    '''exp : exp DOUBLEBAR exp '''
    pass
  
def p_exp17(p):
    '''exp : exp DOUBLEE exp '''
    pass
  
def p_exp18(p):
    '''exp : exp EXCLAMATION exp '''
    pass
  
def p_exp19(p):
    '''exp : exp SIMPLEBAR exp '''
    pass
  
def p_exp20(p):
    '''exp : exp SIMPLEE exp '''
    pass
  
def p_exp21(p):
    '''exp : exp CIRCUMFLEX exp '''
    pass
  
def p_exp22(p):
    '''exp : exp NEGATION exp '''
    pass
  
def p_exp23(p):
    '''exp : exp LSHIFT exp '''
    pass
  
def p_exp24(p):
    '''exp : exp RSHIFT exp '''
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
  print("==============Syntax error in input!==============")