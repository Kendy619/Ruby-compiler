import ply.yacc as yacc
from compiler_ruby import *
from sintaxe_abstract import *


def p_starter(p):
  '''start : program'''
  p[0] = [p[1]]

def p_program1(p):
  '''program : funcdecl'''
  p[0] = p[1]

def p_program2(p):
  '''program : funcdecl program'''
  p[0] = [p[1]] + p[2]

def p_program3(p):
  '''program : class'''
  p[0] = p[1]

def p_program4(p):
  '''program : class program'''
  p[0] = [p[1]] + p[2]

def p_program5(p):
  '''program : stm'''
  p[0] = p[1]

def p_program6(p):
  '''program : stm program'''
  p[0] = [p[1]] + p[2]
  
def p_program7(p):
  '''program : call'''  
  p[0] = p[1]



def p_class_1(p): 
  '''class : CLASS ID body
  '''
  pass
  
#def p_class_1(p): 
#  '''class : CLASS ID funcdecl body
#  '''
#  pass

def p_class_2(p): 
  '''class : CLASS ID stms body
  '''
  pass

def p_class_3(p):
  '''class : CLASS ID bodyclass'''
  pass

def p_bodyclass_1(p): 
  '''bodyclass : funcdecl END
  '''
  p[0] = BodyclassConcrete(p[1], None)

def p_bodyclass_2(p): 
  '''bodyclass : attrdecl END
  '''
  p[0] = BodyclassConcrete(p[1], None)

def p_bodyclass_3(p): 
  '''bodyclass : funcdecl bodyclass END
  '''
  p[0] = BodyclassConcrete(p[1], p[2])

def p_bodyclass_4(p): 
  '''bodyclass : attrdecl bodyclass END
  '''
  p[0] = BodyclassConcrete(p[1], p[2])

def p_attdecl_1(p):
  '''attrdecl : ID EQ objdecl
  '''
   p[0] =  AttdeclConcrete(p[1], p[3])
  

def p_attdecl_2(p):
  '''attrdecl : callobj
  '''
  p[0] =  AttdeclConcrete(p[1], None)

def p_objdecl_1(p):
  '''objdecl : ID PONTO NEW LPAREN ID RPAREN
  '''
  p[0] = ObjdeclConcrete(p[1],p[5])

def p_callobj_1(p):
  '''callobj : ID PONTO ID
  '''
  p[0] = CallobjConcrete(p[1], p[3])



def p_funcdecl(p):
  '''funcdecl : signature body'''
  p[0] = FuncdeclConcrete(p[1],p[2])

def p_signature1(p):
  '''signature : DEF ID LPAREN sigParams RPAREN 
  '''
  p[0] = SignatureConcrete(p[2],p[4])

def p_signature2(p):
  '''signature : DEF ID LPAREN RPAREN
  '''
  p[0] = SignatureConcrete(p[2],None)

def p_signature3(p):
  '''signature : DEF ID'''
  p[0] = SignatureConcrete(p[2],None)

  

def p_sigParams1(p):
  '''sigParams : ID'''
  p[0] = SigparamsSingle(p[1])

def p_sigParams2(p):
  '''sigParams : ID VIRGULA sigParams'''
  p[0] = SigparamsMulti(p[1],p[3])

  
def p_body(p):
  '''body : stms END ''' 
  p[0] = BodyConcrete(p[1])

def p_stms1(p):
  '''stms : stm '''
  p[0] = StmsSingleConcrete(p[1])
  
  
def p_stms2(p):
  '''stms : stm  stms '''
  p[0] = StmsMultiConcrete(p[1],p[2])

def p_stm1(p):
  '''stm : temp''' #no lugar do temp colocar exp
  p[0] = StmConcrete(p[1])
  

def p_stm3(p):
  '''stm : exp PONTOVIRGULA'''
  p[0] = StmConcrete(p[1])
  






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
    p[0] = SIFConcrete(p[3], p[5], p[7])

def p_s1_if2_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE body 
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])

def p_s1_if3_params(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE body 
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])

def p_s1_if4_params(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE s1 
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])
  


def p_s2_if1_params(p):
    ''' s2 :  IF LPAREN exp RPAREN s1 ELSE s1
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])

def p_s2_if2_params(p):
    ''' s2 :  IF LPAREN exp RPAREN body
    '''
    p[0] = SIFConcrete(p[3], p[5], None)

def p_s2_if3_params(p):
    ''' s2 :  IF LPAREN exp RPAREN s1 ELSE s2 
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])

def p_s2_if4_params(p):
    ''' s2 :  IF LPAREN exp RPAREN body ELSE s2
    '''
    p[0] = SIFConcrete(p[3], p[5], p[7])



def p_s1_if1_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN s1 ELSE s1 
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])

def p_s1_if2_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body ELSE body 
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])

def p_s1_if3_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN s1 ELSE body 
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])

def p_s1_if4_params_then(p):
    ''' s1 :  IF LPAREN exp RPAREN THEN body ELSE s1 
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])
  


def p_s2_if1_params_then(p):
    ''' s2 :  IF LPAREN exp RPAREN THEN s1 ELSE s1
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])

def p_s2_if2_params_then(p):
    ''' s2 :  IF LPAREN exp RPAREN THEN body
    '''
    p[0] = SIFConcrete(p[3], p[6], None)

def p_s2_if3_params_then(p):
    ''' s2 :  IF LPAREN exp RPAREN THEN s1 ELSE s2 
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])

def p_s2_if4_params_then(p):
    ''' s2 :  IF LPAREN exp RPAREN THEN body ELSE s2
    '''
    p[0] = SIFConcrete(p[3], p[6], p[8])





def p_s1_if1_noParen(p):
    ''' s1 :  IF exp s1 ELSE s1 
    '''
    p[0] = SIFConcrete(p[2], p[3], p[5])

def p_s1_if2_noParen(p):
    ''' s1 :  IF exp body ELSE body 
    '''
    p[0] = SIFConcrete(p[2], p[3], p[5])

def p_s1_if3_noParen(p):
    ''' s1 :  IF exp s1 ELSE body 
    '''
    p[0] = SIFConcrete(p[2], p[3], p[5])

def p_s1_if4_noParen(p):
    ''' s1 :  IF exp body ELSE s1 
    '''
    p[0] = SIFConcrete(p[3], p[4], p[6])



 
def p_s2_if1_noParen(p):
    ''' s2 :  IF exp s1 ELSE s1
    '''
    p[0] = SIFConcrete(p[2], p[3], p[5])


def p_s2_if2_noParen(p):
    ''' s2 : IF exp body 
    '''
    p[0] = SIFConcrete(p[2], p[3],None)

def p_s2_if3_noParen(p):
    ''' s2 :  IF exp s1 ELSE s2
    '''
    p[0] = SIFConcrete(p[2], p[3], p[5])


def p_s2_if4_noParen(p):
    ''' s2 :  IF exp body ELSE s2
    '''
    p[0] = SIFConcrete(p[2], p[3], p[8])






def p_s1_if1_noParen_then(p):
    ''' s1 :  IF exp THEN s1 ELSE s1 
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])

def p_s1_if2_noParen_then(p):
    ''' s1 :  IF exp THEN body ELSE body 
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])

def p_s1_if3_noParen_then(p):
    ''' s1 :  IF exp THEN s1 ELSE body 
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])

def p_s1_if4_noParen_then(p):
    ''' s1 :  IF exp THEN body ELSE s1 
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])
  



def p_s2_if1_noParen_then(p):
    ''' s2 :  IF exp THEN s2  ELSE s2
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])

def p_s2_if2_noParen_then(p):
    ''' s2 :  IF exp THEN body
    '''
    p[0] = SIFConcrete(p[2], p[4], None)

def p_s2_if3_noParen_then(p):
    ''' s2 :  IF exp THEN s1 ELSE s2 
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])

def p_s2_if4_noParen_then(p):
    ''' s2 :  IF exp THEN body ELSE s2
    '''
    p[0] = SIFConcrete(p[2], p[4], p[6])





def p_stm_while(p):
    '''stm : WHILE exp body'''
    p[0] = StmWhileConcrete(p[2],p[3])
  
def p_stm_while_paren(p):
    '''stm : WHILE LPAREN exp RPAREN body'''
    p[0] = StmWhileConcrete(p[3],p[5])
  
def p_stm_while_do(p):
    '''stm : WHILE exp DO body'''
    p[0] = StmWhileConcrete(p[2],p[4])

def p_stm_while_do_paren(p):
  '''stm : WHILE LPAREN exp RPAREN DO body'''
  p[0] = StmWhileConcrete(p[3],p[6])

def p_stm_for(p):
  '''stm : FOR ID IN ID body'''
  p[0] = StmForConcrete(p[2],p[4],p[5])

def p_stm_for_do(p):
  '''stm : FOR ID IN ID DO body'''
  p[0] = StmForConcrete(p[2],p[4],p[6])



  
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
    '''exp : exp1 PLUS exp 
           | exp1  
    '''
    p[0] = ExpPlusConcrete(p[1],p[3])
  
def p_exp2(p):
    '''exp1 : exp2 MINUS exp1
            | exp2
    '''
    p[0] = ExpMinusConcrete(p[1],p[3])
  
def p_exp3(p):
    '''exp2 : exp3 TIMES exp2 
            | exp3
    '''
    p[0] = ExpTimesConcrete(p[1],p[3])
  
def p_exp4(p):
    '''exp3 : exp4 DIV exp3 
            | exp4
    '''
    pass
  
def p_exp5(p):
    '''exp4 : exp5 EXPO exp4 
            | exp5
    '''
    pass




def p_exp6(p):
    '''exp5 : exp6 REST exp5 
            | exp6  
    '''
    pass

def p_exp7(p):
    '''exp6 : exp7 DOUBLEEQUAL exp6
            | exp7
    '''
    pass
  
def p_exp8(p):
    '''exp7 : exp8 TRIPLEEQ exp7
            | exp8
    '''
    pass
  
def p_exp9(p):
    '''exp8 : exp9 SMALL exp8
            | exp9  
    '''
    pass
  
def p_exp10(p):
    '''exp9 : exp10 BIGGEST exp9
            | exp10 
    '''
    pass
  
def p_exp11(p):
    '''exp10 : exp11 DIFF exp10
             | exp11
    '''
    pass
  
def p_exp12(p):
    '''exp11 : exp12 POINTRANGE exp11
             | exp12
    '''
    pass
    
def p_exp13(p):
    '''exp12 : exp13 SMALLEQ exp12
             | exp13
    '''
    pass
  
def p_exp14(p):
    '''exp13 : exp14 BIGGESTEQ exp13
             | exp14
    '''
    pass
  
def p_exp15(p):
    '''exp14 : exp15 BIGGSMALLEQ exp14
             | exp15
    '''
    pass
  
def p_exp16(p):
    '''exp15 : exp16 DOUBLEBAR exp15 
             | exp16
    '''
    pass
  
def p_exp17(p):
    '''exp16 : exp17 DOUBLEE exp16 
             | exp17
    '''
    pass
  
def p_exp18(p):
    '''exp17 : exp18 EXCLAMATION exp17 
             | exp18
    '''
    pass
  
def p_exp19(p):
    '''exp18 : exp19 SIMPLEBAR exp18
             | exp19
    '''
    pass
  
def p_exp20(p):
    '''exp19 : exp20 SIMPLEE exp19
             | exp20
    '''
    pass
  
def p_exp21(p):
    '''exp20 : exp21 CIRCUMFLEX exp20
             | exp21
    '''
    pass
  
def p_exp22(p):
    '''exp21 : exp22 NEGATION exp21
             | exp22
    '''
    pass
  
def p_exp23(p):
    '''exp22 : exp23 LSHIFT exp22
             | exp23
    '''
    pass
  
def p_exp24(p):
    '''exp23 : exp24 RSHIFT exp23
             | exp24
    '''
    pass


def p_exp24(p):
    '''exp23 : exp24 RSHIFT exp23
             | exp24
    '''
    pass

  

































def p_exp25(p):
  '''temp : call '''
  p[0] = p[1]
  


def p_exp25(p):
  '''exp24 : call ''' #onde está exp24 era exp
  pass
  
def p_exp26(p):
  '''exp24 : assign '''
  pass

def p_exp27(p):
  '''exp24 : NUMBER '''
  pass

def p_exp29(p):
  '''exp24 : STRING '''
  pass

def p_exp28(p):
  '''exp24 : ID '''
  pass
  
def p_assign(p):
  '''assign : ID EQ exp '''
  p[0] = AssignConcrete(p[1], p[3])

def p_call1(p):
  '''call : ID LPAREN params RPAREN  '''
  pass
  
def p_call2(p):
  '''call : ID LPAREN RPAREN '''
  p[0] = ExpCallConcrete(p[1])

def p_params1(p):
    '''params :  exp VIRGULA params  '''
    pass

def p_params2(p):
    '''params :  exp '''
    p[0] = ParamssingleConcrete(p[1])

def p_error(p):
  print("==============Syntax error in input!==============")