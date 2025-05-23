
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftANDORleftEQEQNEQGTLTGEQLEQAND COLON COMMA DIVIDE ELSE EQEQ EQUALS FALSE FLOAT FOR GEQ GT ID IF IN LEQ LPAREN LT MINUS NEQ NEWLINE NUMBER OR PLUS PRINT RANGE RPAREN STRING TIMES TRUEprogram : statement_liststatement_list : statement\n| statement_list statementblock : statement\n| statement_liststatement : ID EQUALS expr NEWLINEstatement : PRINT LPAREN expr RPAREN NEWLINEstatement : IF expr COLON NEWLINE block ELSE COLON NEWLINE blockstatement : FOR ID IN RANGE LPAREN expr RPAREN COLON NEWLINE blockexpr : expr EQEQ expr\n| expr NEQ expr\n| expr GT expr\n| expr LT expr\n| expr GEQ expr\n| expr LEQ exprexpr : expr AND expr\n| expr OR exprexpr : expr PLUS expr\n| expr MINUS expr\n| expr TIMES expr\n| expr DIVIDE exprexpr : NUMBERexpr : FLOATexpr : IDexpr : STRINGexpr : TRUEexpr : FALSEexpr : LPAREN expr RPARENexpr : expr COMMA expr'
    
_lr_action_items = {'ID':([0,2,3,6,7,8,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,38,40,56,58,59,60,65,67,68,69,],[4,4,-2,14,19,-3,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-6,4,-7,-2,4,14,4,-8,4,-9,]),'PRINT':([0,2,3,8,38,40,56,58,59,65,67,68,69,],[5,5,-2,-3,-6,5,-7,-2,5,5,-8,5,-9,]),'IF':([0,2,3,8,38,40,56,58,59,65,67,68,69,],[6,6,-2,-3,-6,6,-7,-2,6,6,-8,6,-9,]),'FOR':([0,2,3,8,38,40,56,58,59,65,67,68,69,],[7,7,-2,-3,-6,7,-7,-2,7,7,-8,7,-9,]),'$end':([1,2,3,8,38,56,58,59,67,69,],[0,-1,-2,-3,-6,-7,-2,-5,-8,-9,]),'EQUALS':([4,],[9,]),'LPAREN':([5,6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,55,60,],[10,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,60,18,]),'NUMBER':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'FLOAT':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'STRING':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'TRUE':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'FALSE':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ELSE':([8,38,56,57,58,59,67,69,],[-3,-6,-7,61,-2,-5,-8,-9,]),'COLON':([11,12,13,14,15,16,17,41,42,43,44,45,46,47,48,49,50,51,52,53,54,61,64,],[22,-22,-23,-24,-25,-26,-27,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-29,-28,63,66,]),'EQEQ':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[23,-22,-23,-24,-25,-26,-27,23,23,23,-10,-11,-12,-13,-14,-15,23,23,23,23,23,23,23,-28,23,]),'NEQ':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[24,-22,-23,-24,-25,-26,-27,24,24,24,-10,-11,-12,-13,-14,-15,24,24,24,24,24,24,24,-28,24,]),'GT':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[25,-22,-23,-24,-25,-26,-27,25,25,25,-10,-11,-12,-13,-14,-15,25,25,25,25,25,25,25,-28,25,]),'LT':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[26,-22,-23,-24,-25,-26,-27,26,26,26,-10,-11,-12,-13,-14,-15,26,26,26,26,26,26,26,-28,26,]),'GEQ':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[27,-22,-23,-24,-25,-26,-27,27,27,27,-10,-11,-12,-13,-14,-15,27,27,27,27,27,27,27,-28,27,]),'LEQ':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[28,-22,-23,-24,-25,-26,-27,28,28,28,-10,-11,-12,-13,-14,-15,28,28,28,28,28,28,28,-28,28,]),'AND':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[29,-22,-23,-24,-25,-26,-27,29,29,29,-10,-11,-12,-13,-14,-15,-16,-17,29,29,29,29,29,-28,29,]),'OR':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[30,-22,-23,-24,-25,-26,-27,30,30,30,-10,-11,-12,-13,-14,-15,-16,-17,30,30,30,30,30,-28,30,]),'PLUS':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[31,-22,-23,-24,-25,-26,-27,31,31,31,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,31,-28,31,]),'MINUS':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[32,-22,-23,-24,-25,-26,-27,32,32,32,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,32,-28,32,]),'TIMES':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[33,-22,-23,-24,-25,-26,-27,33,33,33,-10,-11,-12,-13,-14,-15,-16,-17,33,33,-20,-21,33,-28,33,]),'DIVIDE':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[34,-22,-23,-24,-25,-26,-27,34,34,34,-10,-11,-12,-13,-14,-15,-16,-17,34,34,-20,-21,34,-28,34,]),'COMMA':([11,12,13,14,15,16,17,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[35,-22,-23,-24,-25,-26,-27,35,35,35,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,35,-28,35,]),'NEWLINE':([12,13,14,15,16,17,20,22,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,63,66,],[-22,-23,-24,-25,-26,-27,38,40,56,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-29,-28,65,68,]),'RPAREN':([12,13,14,15,16,17,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,],[-22,-23,-24,-25,-26,-27,39,54,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-29,-28,64,]),'IN':([19,],[37,]),'RANGE':([37,],[55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,40,65,68,],[2,59,59,59,]),'statement':([0,2,40,59,65,68,],[3,8,58,8,58,58,]),'expr':([6,9,10,18,23,24,25,26,27,28,29,30,31,32,33,34,35,60,],[11,20,21,36,41,42,43,44,45,46,47,48,49,50,51,52,53,62,]),'block':([40,65,68,],[57,67,69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',12),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',16),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',17),
  ('block -> statement','block',1,'p_block','parser.py',24),
  ('block -> statement_list','block',1,'p_block','parser.py',25),
  ('statement -> ID EQUALS expr NEWLINE','statement',4,'p_statement_assign','parser.py',32),
  ('statement -> PRINT LPAREN expr RPAREN NEWLINE','statement',5,'p_statement_print','parser.py',36),
  ('statement -> IF expr COLON NEWLINE block ELSE COLON NEWLINE block','statement',9,'p_statement_if','parser.py',40),
  ('statement -> FOR ID IN RANGE LPAREN expr RPAREN COLON NEWLINE block','statement',10,'p_statement_for','parser.py',44),
  ('expr -> expr EQEQ expr','expr',3,'p_expr_comparison','parser.py',49),
  ('expr -> expr NEQ expr','expr',3,'p_expr_comparison','parser.py',50),
  ('expr -> expr GT expr','expr',3,'p_expr_comparison','parser.py',51),
  ('expr -> expr LT expr','expr',3,'p_expr_comparison','parser.py',52),
  ('expr -> expr GEQ expr','expr',3,'p_expr_comparison','parser.py',53),
  ('expr -> expr LEQ expr','expr',3,'p_expr_comparison','parser.py',54),
  ('expr -> expr AND expr','expr',3,'p_expr_logical','parser.py',59),
  ('expr -> expr OR expr','expr',3,'p_expr_logical','parser.py',60),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binop','parser.py',65),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binop','parser.py',66),
  ('expr -> expr TIMES expr','expr',3,'p_expr_binop','parser.py',67),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_binop','parser.py',68),
  ('expr -> NUMBER','expr',1,'p_expr_number','parser.py',72),
  ('expr -> FLOAT','expr',1,'p_expr_float','parser.py',76),
  ('expr -> ID','expr',1,'p_expr_id','parser.py',80),
  ('expr -> STRING','expr',1,'p_expr_string','parser.py',84),
  ('expr -> TRUE','expr',1,'p_expr_true','parser.py',88),
  ('expr -> FALSE','expr',1,'p_expr_false','parser.py',92),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_parens','parser.py',97),
  ('expr -> expr COMMA expr','expr',3,'p_expr_comma','parser.py',102),
]
