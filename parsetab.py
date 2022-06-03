
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BARN BEGIN BIGGEST BIGGESTEQ BIGGSMALLEQ BREAK CIRCUMFLEX CLASS CLOSEKEY COMMENT COMMENTMULTI DEF DIFF DIV DO DOUBLEBAR DOUBLEE DOUBLEEQUAL ELSE ELSIF END EQ EXCLAMATION EXPO FALSE FOR ID ID_CLASS ID_GLOBAL ID_INSTANCE IF IN LPAREN LSHIFT MINUS MODULE NAME NEGATION NEW NIL NOT NUMBER OPENKEY OR PLUS POINTRANGE PONTO PONTOVIRGULA REST RETURN RPAREN RSHIFT SELF SIMPLEBAR SIMPLEE SMALL SMALLEQ STRING SUPER THEN TIMES TRIPLEEQ TRUE VIRGULA WHILEprogram : funcdeclprogram : funcdecl programprogram : stmprogram : stm programprogram : callfuncdecl : signature bodysignature : DEF IDbody : stms END stms : stm stms : stm  stms stm : expstm : exp PONTOVIRGULAstm : s s : s1 \n          | s2  s1 : stms \n     s1 :  IF LPAREN exp RPAREN s1 ELSE s1 \n     s1 :  IF LPAREN exp RPAREN body ELSE body \n     s1 :  IF LPAREN exp RPAREN s1 ELSE body \n     s1 :  IF LPAREN exp RPAREN body ELSE s1 \n     s2 :  IF LPAREN exp RPAREN s1 ELSE s1\n     s1 :  IF LPAREN exp RPAREN body\n     s1 :  IF LPAREN exp RPAREN s1 ELSE s2 \n     s1 :  IF LPAREN exp RPAREN body ELSE s2\n     s1 :  IF LPAREN exp RPAREN THEN s1 ELSE s1 \n     s1 :  IF LPAREN exp RPAREN THEN body ELSE body \n     s1 :  IF LPAREN exp RPAREN THEN s1 ELSE body \n     s1 :  IF LPAREN exp RPAREN THEN body ELSE s1 \n     s2 :  IF LPAREN exp RPAREN THEN s1 ELSE s1\n     s1 :  IF LPAREN exp RPAREN THEN body\n     s1 :  IF LPAREN exp RPAREN THEN s1 ELSE s2 \n     s1 :  IF LPAREN exp RPAREN THEN body ELSE s2\n     s1 :  IF exp s1 ELSE s1 \n     s1 :  IF exp body ELSE body \n     s1 :  IF exp s1 ELSE body \n     s1 :  IF exp body ELSE s1 \n     s2 :  IF exp s1 ELSE s1\n     s1 :  IF exp body\n     s1 :  IF exp body ELSE s2\n     s1 :  IF exp THEN s1 ELSE s1 \n     s1 :  IF exp THEN body ELSE body \n     s1 :  IF exp THEN s1 ELSE body \n     s1 :  IF exp THEN body ELSE s1 \n     s2 :  IF exp THEN s2  ELSE s2\n     s1 :  IF exp THEN body\n     s1 :  IF exp THEN s1 ELSE s2 \n     s1 :  IF exp THEN body ELSE s2\n    stm : RETURN exp stm : RETURN exp PONTOVIRGULAexp : call exp : assign exp : NUMBER exp : STRING exp : ID exp : exp DOUBLEEQUAL exp assign : ID EQ exp call : ID LPAREN params RPAREN  call : ID LPAREN RPAREN params :  exp VIRGULA params  params :  exp '
    
_lr_action_items = {'RETURN':([0,2,3,4,5,6,7,9,11,12,13,14,15,16,20,21,22,23,24,25,26,28,31,33,34,35,36,38,40,42,43,44,45,46,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,77,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,95,97,98,100,101,102,103,104,105,106,107,],[8,8,8,-50,8,-11,-13,-54,-51,-52,-53,-14,-15,-16,-10,-6,-16,8,-50,-54,-12,-48,-7,8,-8,-55,-49,-58,-56,-14,-38,8,-16,-57,8,8,8,-14,-45,-15,-14,-22,8,-14,-35,-34,-14,-15,8,8,8,8,-14,-30,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,8,8,8,-14,-27,-15,-26,-14,-15,-14,8,8,-14,8,-14,8,-14,-14,8,-14,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,97,98,100,101,102,103,104,105,106,107,],[9,9,9,-50,25,-11,-13,25,-54,31,-51,-52,-53,-14,-15,-16,25,-10,-6,-16,25,-50,-54,-12,25,-48,25,25,-7,25,25,-8,-55,-49,-58,-56,-14,-38,25,-16,-57,25,25,25,25,-14,-45,-15,-14,-22,25,-14,-35,-34,-14,-15,25,25,25,25,-14,-30,-14,-42,-15,-41,-14,-15,25,-44,-14,-19,-15,-18,-14,-15,25,25,25,25,-14,-27,-15,-26,-14,-15,-14,25,25,-14,25,-14,25,-14,-14,25,-14,]),'DEF':([0,2,3,4,6,7,9,11,12,13,14,15,16,20,21,22,23,24,25,26,28,34,35,36,38,40,43,45,46,52,56,58,59,60,61,62,69,70,71,72,73,74,75,77,78,79,80,81,82,83,88,89,90,91,92,93,102,105,107,],[10,10,10,-50,-11,-13,-54,-51,-52,-53,-14,-15,-16,-10,-6,-16,-9,-50,-54,-12,-48,-8,-55,-49,-58,-56,-38,-16,-57,-45,-22,-14,-35,-34,-14,-15,-30,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,-14,-27,-15,-26,-14,-15,-14,-14,-14,]),'NUMBER':([0,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,97,98,100,101,102,103,104,105,106,107,],[12,12,12,-50,12,-11,-13,12,-54,-51,-52,-53,-14,-15,-16,12,-10,-6,-16,12,-50,-54,-12,12,-48,12,12,-7,12,12,-8,-55,-49,-58,-56,-14,-38,12,-16,-57,12,12,12,12,-14,-45,-15,-14,-22,12,-14,-35,-34,-14,-15,12,12,12,12,-14,-30,-14,-42,-15,-41,-14,-15,12,-44,-14,-19,-15,-18,-14,-15,12,12,12,12,-14,-27,-15,-26,-14,-15,-14,12,12,-14,12,-14,12,-14,-14,12,-14,]),'STRING':([0,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,97,98,100,101,102,103,104,105,106,107,],[13,13,13,-50,13,-11,-13,13,-54,-51,-52,-53,-14,-15,-16,13,-10,-6,-16,13,-50,-54,-12,13,-48,13,13,-7,13,13,-8,-55,-49,-58,-56,-14,-38,13,-16,-57,13,13,13,13,-14,-45,-15,-14,-22,13,-14,-35,-34,-14,-15,13,13,13,13,-14,-30,-14,-42,-15,-41,-14,-15,13,-44,-14,-19,-15,-18,-14,-15,13,13,13,13,-14,-27,-15,-26,-14,-15,-14,13,13,-14,13,-14,13,-14,-14,13,-14,]),'IF':([0,2,3,4,5,6,7,9,11,12,13,14,15,16,20,21,22,23,24,25,26,28,31,33,34,35,36,38,40,42,43,44,45,46,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,95,96,97,98,100,101,102,103,104,105,106,107,],[17,17,17,-50,17,-11,-13,-54,-51,-52,-53,-14,-15,-16,-10,-6,-16,17,-50,-54,-12,-48,-7,17,-8,-55,-49,-58,-56,-14,-38,17,-16,-57,17,17,17,-14,-45,-15,-14,-22,17,-14,-35,-34,-14,-15,17,17,76,17,17,-14,-30,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,17,17,17,-14,-27,-15,-26,-14,-15,-14,76,17,17,-14,17,-14,17,-14,-14,17,-14,]),'$end':([1,2,3,4,6,7,9,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,28,34,35,36,38,40,43,45,46,52,56,58,59,60,61,62,69,70,71,72,73,74,75,77,78,79,80,81,82,83,88,89,90,91,92,93,102,105,107,],[0,-1,-3,-5,-11,-13,-54,-51,-52,-53,-14,-15,-16,-2,-4,-10,-6,-16,-9,-50,-54,-12,-48,-8,-55,-49,-58,-56,-38,-16,-57,-45,-22,-14,-35,-34,-14,-15,-30,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,-14,-27,-15,-26,-14,-15,-14,-14,-14,]),'PONTOVIRGULA':([4,6,9,11,12,13,24,25,28,35,38,40,46,],[-50,26,-54,-51,-52,-53,-50,-54,36,-55,-58,-56,-57,]),'DOUBLEEQUAL':([4,6,9,11,12,13,24,25,28,33,35,38,39,40,41,46,87,94,],[-50,27,-54,-51,-52,-53,-50,-54,27,27,27,-58,27,27,27,-57,27,27,]),'END':([6,7,11,12,13,14,15,16,20,22,23,24,25,26,28,34,35,36,38,40,42,43,45,46,51,52,53,55,56,58,59,60,61,62,68,69,70,71,72,73,74,75,77,78,79,80,81,82,83,88,89,90,91,92,93,102,105,107,],[-11,-13,-51,-52,-53,-14,-15,-16,-10,34,-9,-50,-54,-12,-48,-8,-55,-49,-58,-56,-14,-38,34,-57,-14,-45,-15,-14,-22,-14,-35,-34,-14,-15,-14,-30,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,-14,-27,-15,-26,-14,-15,-14,-14,-14,]),'ELSE':([6,7,11,12,13,14,15,16,20,22,23,24,25,26,28,34,35,36,38,40,42,43,45,46,51,52,53,55,56,58,59,60,61,62,68,69,70,71,72,73,74,75,77,78,79,80,81,82,83,88,89,90,91,92,93,95,99,100,102,104,105,107,],[-11,-13,-51,-52,-53,-14,-15,-16,-10,-16,-9,-50,-54,-12,-48,-8,-55,-49,-58,-56,49,50,-16,-57,63,64,65,66,67,-14,-35,-34,-14,-15,84,85,-14,-42,-15,-41,-14,-15,-44,-14,-19,-15,-18,-14,-15,-14,-27,-15,-26,-14,-15,98,65,103,-14,106,-14,-14,]),'LPAREN':([9,17,25,76,],[29,32,29,86,]),'EQ':([9,25,],[30,30,]),'THEN':([11,12,13,24,25,33,35,38,40,46,48,87,97,],[-51,-52,-53,-50,-54,44,-55,-58,-56,-57,57,96,101,]),'VIRGULA':([11,12,13,24,25,35,38,39,40,46,],[-51,-52,-53,-50,-54,-55,-58,47,-56,-57,]),'RPAREN':([11,12,13,24,25,29,35,37,38,39,40,41,46,54,94,],[-51,-52,-53,-50,-54,38,-55,46,-58,-60,-56,48,-57,-59,97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,18,19,]),'funcdecl':([0,2,3,],[2,2,2,]),'stm':([0,2,3,5,23,33,44,48,49,50,57,63,64,66,67,84,85,87,97,98,101,103,106,],[3,3,3,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'call':([0,2,3,5,8,17,23,27,29,30,32,33,44,47,48,49,50,57,63,64,66,67,76,84,85,86,87,97,98,101,103,106,],[4,4,4,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'signature':([0,2,3,],[5,5,5,]),'exp':([0,2,3,5,8,17,23,27,29,30,32,33,44,47,48,49,50,57,63,64,66,67,76,84,85,86,87,97,98,101,103,106,],[6,6,6,6,28,33,6,35,39,40,41,6,6,39,6,6,6,6,6,6,6,6,87,6,6,94,6,6,6,6,6,6,]),'s':([0,2,3,5,23,33,44,48,49,50,57,63,64,66,67,84,85,87,97,98,101,103,106,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'assign':([0,2,3,5,8,17,23,27,29,30,32,33,44,47,48,49,50,57,63,64,66,67,76,84,85,86,87,97,98,101,103,106,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'s1':([0,2,3,5,23,33,44,48,49,50,57,63,64,66,67,84,85,87,97,98,101,103,106,],[14,14,14,14,14,42,51,55,58,61,68,70,74,78,82,88,92,95,100,102,104,105,107,]),'s2':([0,2,3,5,23,33,44,48,49,50,57,63,64,65,66,67,84,85,87,96,97,98,101,103,106,],[15,15,15,15,15,15,53,15,15,62,15,72,75,77,80,83,90,93,15,99,15,15,15,15,15,]),'stms':([0,2,3,5,23,33,44,48,49,50,57,63,64,66,67,84,85,87,97,98,101,103,106,],[16,16,20,22,20,45,45,45,45,22,45,45,22,45,22,45,22,16,16,16,16,16,16,]),'body':([5,33,44,48,49,50,57,63,64,66,67,84,85,],[21,43,52,56,59,60,69,71,73,79,81,89,91,]),'params':([29,47,],[37,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> funcdecl','program',1,'p_program1','sintaticruby2.py',5),
  ('program -> funcdecl program','program',2,'p_program2','sintaticruby2.py',9),
  ('program -> stm','program',1,'p_program5','sintaticruby2.py',12),
  ('program -> stm program','program',2,'p_program6','sintaticruby2.py',16),
  ('program -> call','program',1,'p_program7','sintaticruby2.py',20),
  ('funcdecl -> signature body','funcdecl',2,'p_funcdecl','sintaticruby2.py',24),
  ('signature -> DEF ID','signature',2,'p_signature3','sintaticruby2.py',28),
  ('body -> stms END','body',2,'p_body','sintaticruby2.py',32),
  ('stms -> stm','stms',1,'p_stms1','sintaticruby2.py',36),
  ('stms -> stm stms','stms',2,'p_stms2','sintaticruby2.py',40),
  ('stm -> exp','stm',1,'p_stm1','sintaticruby2.py',44),
  ('stm -> exp PONTOVIRGULA','stm',2,'p_stm3','sintaticruby2.py',48),
  ('stm -> s','stm',1,'p_if','sintaticruby2.py',57),
  ('s -> s1','s',1,'p_s','sintaticruby2.py',61),
  ('s -> s2','s',1,'p_s','sintaticruby2.py',62),
  ('s1 -> stms','s1',1,'p_s1_if0','sintaticruby2.py',66),
  ('s1 -> IF LPAREN exp RPAREN s1 ELSE s1','s1',7,'p_s1_if1_params','sintaticruby2.py',72),
  ('s1 -> IF LPAREN exp RPAREN body ELSE body','s1',7,'p_s1_if2_params','sintaticruby2.py',77),
  ('s1 -> IF LPAREN exp RPAREN s1 ELSE body','s1',7,'p_s1_if3_params','sintaticruby2.py',82),
  ('s1 -> IF LPAREN exp RPAREN body ELSE s1','s1',7,'p_s1_if4_params','sintaticruby2.py',87),
  ('s2 -> IF LPAREN exp RPAREN s1 ELSE s1','s2',7,'p_s2_if1_params','sintaticruby2.py',94),
  ('s1 -> IF LPAREN exp RPAREN body','s1',5,'p_s2_if2_params','sintaticruby2.py',99),
  ('s1 -> IF LPAREN exp RPAREN s1 ELSE s2','s1',7,'p_s2_if3_params','sintaticruby2.py',104),
  ('s1 -> IF LPAREN exp RPAREN body ELSE s2','s1',7,'p_s2_if4_params','sintaticruby2.py',109),
  ('s1 -> IF LPAREN exp RPAREN THEN s1 ELSE s1','s1',8,'p_s1_if1_params_then','sintaticruby2.py',121),
  ('s1 -> IF LPAREN exp RPAREN THEN body ELSE body','s1',8,'p_s1_if2_params_then','sintaticruby2.py',126),
  ('s1 -> IF LPAREN exp RPAREN THEN s1 ELSE body','s1',8,'p_s1_if3_params_then','sintaticruby2.py',131),
  ('s1 -> IF LPAREN exp RPAREN THEN body ELSE s1','s1',8,'p_s1_if4_params_then','sintaticruby2.py',136),
  ('s2 -> IF LPAREN exp RPAREN THEN s1 ELSE s1','s2',8,'p_s2_if1_params_then','sintaticruby2.py',142),
  ('s1 -> IF LPAREN exp RPAREN THEN body','s1',6,'p_s2_if2_params_then','sintaticruby2.py',147),
  ('s1 -> IF LPAREN exp RPAREN THEN s1 ELSE s2','s1',8,'p_s2_if3_params_then','sintaticruby2.py',152),
  ('s1 -> IF LPAREN exp RPAREN THEN body ELSE s2','s1',8,'p_s2_if4_params_then','sintaticruby2.py',157),
  ('s1 -> IF exp s1 ELSE s1','s1',5,'p_s1_if1_noParen','sintaticruby2.py',200),
  ('s1 -> IF exp body ELSE body','s1',5,'p_s1_if2_noParen','sintaticruby2.py',205),
  ('s1 -> IF exp s1 ELSE body','s1',5,'p_s1_if3_noParen','sintaticruby2.py',210),
  ('s1 -> IF exp body ELSE s1','s1',5,'p_s1_if4_noParen','sintaticruby2.py',215),
  ('s2 -> IF exp s1 ELSE s1','s2',5,'p_s2_if1_noParen','sintaticruby2.py',220),
  ('s1 -> IF exp body','s1',3,'p_s2_if2_noParen','sintaticruby2.py',225),
  ('s1 -> IF exp body ELSE s2','s1',5,'p_s2_if4_noParen','sintaticruby2.py',230),
  ('s1 -> IF exp THEN s1 ELSE s1','s1',6,'p_s1_if1_noParen_then','sintaticruby2.py',237),
  ('s1 -> IF exp THEN body ELSE body','s1',6,'p_s1_if2_noParen_then','sintaticruby2.py',242),
  ('s1 -> IF exp THEN s1 ELSE body','s1',6,'p_s1_if3_noParen_then','sintaticruby2.py',247),
  ('s1 -> IF exp THEN body ELSE s1','s1',6,'p_s1_if4_noParen_then','sintaticruby2.py',252),
  ('s2 -> IF exp THEN s2 ELSE s2','s2',6,'p_s2_if1_noParen_then','sintaticruby2.py',260),
  ('s1 -> IF exp THEN body','s1',4,'p_s2_if2_noParen_then','sintaticruby2.py',265),
  ('s1 -> IF exp THEN s1 ELSE s2','s1',6,'p_s2_if3_noParen_then','sintaticruby2.py',270),
  ('s1 -> IF exp THEN body ELSE s2','s1',6,'p_s2_if4_noParen_then','sintaticruby2.py',275),
  ('stm -> RETURN exp','stm',2,'p_stm12','sintaticruby2.py',305),
  ('stm -> RETURN exp PONTOVIRGULA','stm',3,'p_stm13','sintaticruby2.py',309),
  ('exp -> call','exp',1,'p_exp25','sintaticruby2.py',313),
  ('exp -> assign','exp',1,'p_exp26','sintaticruby2.py',317),
  ('exp -> NUMBER','exp',1,'p_exp27','sintaticruby2.py',321),
  ('exp -> STRING','exp',1,'p_exp29','sintaticruby2.py',325),
  ('exp -> ID','exp',1,'p_exp28','sintaticruby2.py',329),
  ('exp -> exp DOUBLEEQUAL exp','exp',3,'p_exp7','sintaticruby2.py',333),
  ('assign -> ID EQ exp','assign',3,'p_assign','sintaticruby2.py',338),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call1','sintaticruby2.py',342),
  ('call -> ID LPAREN RPAREN','call',3,'p_call2','sintaticruby2.py',346),
  ('params -> exp VIRGULA params','params',3,'p_params1','sintaticruby2.py',350),
  ('params -> exp','params',1,'p_params2','sintaticruby2.py',354),
]
