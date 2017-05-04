
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left/*leftDEFID STRING NUMBER IF WHILE RETURN CONST DEF FOR DEFSTRUCT DEFMODULE program : statements\n                | program statements statements : statement\n                   | statements statement  statement : func_def\n                  | assign ';'\n                  | expr ';'  func_def : DEF ID '(' argument_list ')' block  block : '{' '}'  block : '{' statements '}'  block : '{' statements RETURN expr ';' '}'  block : '{' RETURN expr ';' '}'  argument      : expr\n                      | default_assign  argument_list : argument\n                      | argument ',' argument_list  function_argument : expr  function_argument_list : function_argument\n                               | function_argument ',' function_argument_list  assign : CONST ID '=' expr  assign : ID '=' expr  default_assign : ID '=' expr  expr : term\n             | expr '+' term\n             | expr '-' term  term : factor\n             | term '*' factor\n             | term '/' factor\n             | term '^' factor  factor : NUMBER\n               | STRING\n               | func_call  factor : ID  factor : '(' expr ')'  func_call : ID '(' function_argument_list ')' "
    
_lr_action_items = {'=':([15,22,48,],[29,35,53,]),'(':([0,1,2,6,9,10,15,17,18,19,20,21,23,24,25,26,27,28,29,30,35,38,48,49,51,53,56,57,59,60,61,62,63,68,69,],[2,-3,2,2,-5,2,30,30,2,2,2,2,2,-7,2,-4,38,-6,2,2,2,2,30,2,2,2,-8,2,-9,2,2,-10,2,-12,-11,]),'NUMBER':([0,1,2,6,9,10,18,19,20,21,23,24,25,26,28,29,30,35,38,49,51,53,56,57,59,60,61,62,63,68,69,],[3,-3,3,3,-5,3,3,3,3,3,3,-7,3,-4,-6,3,3,3,3,3,3,3,-8,3,-9,3,3,-10,3,-12,-11,]),'CONST':([0,1,6,9,10,21,24,26,28,56,57,59,60,62,68,69,],[7,-3,7,-5,7,7,-7,-4,-6,-8,7,-9,7,-10,-12,-11,]),'$end':([1,6,9,10,21,24,26,28,56,59,62,68,69,],[-3,0,-5,-1,-2,-7,-4,-6,-8,-9,-10,-12,-11,]),'}':([1,9,24,26,28,56,57,59,60,62,66,67,68,69,],[-3,-5,-7,-4,-6,-8,59,-9,62,-10,68,69,-12,-11,]),'{':([52,],[57,]),'*':([3,4,5,11,14,15,17,31,32,33,34,36,37,48,50,],[-30,-26,18,-31,-32,-33,-33,-34,-27,-29,-28,18,18,-33,-35,]),'+':([3,4,5,8,11,14,15,16,17,31,32,33,34,36,37,39,40,43,47,48,50,58,64,65,],[-30,-26,-23,23,-31,-32,-33,23,-33,-34,-27,-29,-28,-24,-25,23,23,23,23,-33,-35,23,23,23,]),'^':([3,4,5,11,14,15,17,31,32,33,34,36,37,48,50,],[-30,-26,19,-31,-32,-33,-33,-34,-27,-29,-28,19,19,-33,-35,]),';':([3,4,5,8,11,13,14,15,17,31,32,33,34,36,37,39,43,50,64,65,],[-30,-26,-23,24,-31,28,-32,-33,-33,-34,-27,-29,-28,-24,-25,-21,-20,-35,66,67,]),'STRING':([0,1,2,6,9,10,18,19,20,21,23,24,25,26,28,29,30,35,38,49,51,53,56,57,59,60,61,62,63,68,69,],[11,-3,11,11,-5,11,11,11,11,11,11,-7,11,-4,-6,11,11,11,11,11,11,11,-8,11,-9,11,11,-10,11,-12,-11,]),',':([3,4,5,11,14,17,31,32,33,34,36,37,40,41,44,45,47,48,50,58,],[-30,-26,-23,-31,-32,-33,-34,-27,-29,-28,-24,-25,-17,49,-14,51,-13,-33,-35,-22,]),'RETURN':([1,9,24,26,28,56,57,59,60,62,68,69,],[-3,-5,-7,-4,-6,-8,61,-9,63,-10,-12,-11,]),'DEF':([0,1,6,9,10,21,24,26,28,56,57,59,60,62,68,69,],[12,-3,12,-5,12,12,-7,-4,-6,-8,12,-9,12,-10,-12,-11,]),')':([3,4,5,11,14,16,17,31,32,33,34,36,37,40,41,42,44,45,46,47,48,50,54,55,58,],[-30,-26,-23,-31,-32,31,-33,-34,-27,-29,-28,-24,-25,-17,-18,50,-14,-15,52,-13,-33,-35,-19,-16,-22,]),'-':([3,4,5,8,11,14,15,16,17,31,32,33,34,36,37,39,40,43,47,48,50,58,64,65,],[-30,-26,-23,25,-31,-32,-33,25,-33,-34,-27,-29,-28,-24,-25,25,25,25,25,-33,-35,25,25,25,]),'ID':([0,1,2,6,7,9,10,12,18,19,20,21,23,24,25,26,28,29,30,35,38,49,51,53,56,57,59,60,61,62,63,68,69,],[15,-3,17,15,22,-5,15,27,17,17,17,15,17,-7,17,-4,-6,17,17,17,48,17,48,17,-8,15,-9,15,17,-10,17,-12,-11,]),'/':([3,4,5,11,14,15,17,31,32,33,34,36,37,48,50,],[-30,-26,20,-31,-32,-33,-33,-34,-27,-29,-28,20,20,-33,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,6,10,21,57,60,],[1,1,26,26,1,26,]),'default_assign':([38,51,],[44,44,]),'block':([52,],[56,]),'func_def':([0,6,10,21,57,60,],[9,9,9,9,9,9,]),'expr':([0,2,6,10,21,29,30,35,38,49,51,53,57,60,61,63,],[8,16,8,8,8,39,40,43,47,40,47,58,8,8,64,65,]),'factor':([0,2,6,10,18,19,20,21,23,25,29,30,35,38,49,51,53,57,60,61,63,],[4,4,4,4,32,33,34,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'term':([0,2,6,10,21,23,25,29,30,35,38,49,51,53,57,60,61,63,],[5,5,5,5,5,36,37,5,5,5,5,5,5,5,5,5,5,5,]),'program':([0,],[6,]),'argument_list':([38,51,],[46,55,]),'function_argument':([30,49,],[41,41,]),'statements':([0,6,57,],[10,21,60,]),'argument':([38,51,],[45,45,]),'function_argument_list':([30,49,],[42,54,]),'assign':([0,6,10,21,57,60,],[13,13,13,13,13,13,]),'func_call':([0,2,6,10,18,19,20,21,23,25,29,30,35,38,49,51,53,57,60,61,63,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_module','__init__.py',11),
  ('program -> program statements','program',2,'p_module','__init__.py',12),
  ('statements -> statement','statements',1,'p_statements','__init__.py',19),
  ('statements -> statements statement','statements',2,'p_statements','__init__.py',20),
  ('statement -> func_def','statement',1,'p_statement','__init__.py',27),
  ('statement -> assign ;','statement',2,'p_statement','__init__.py',28),
  ('statement -> expr ;','statement',2,'p_statement','__init__.py',29),
  ('func_def -> DEF ID ( argument_list ) block','func_def',6,'p_func_def','__init__.py',33),
  ('block -> { }','block',2,'p_block_empty','__init__.py',37),
  ('block -> { statements }','block',3,'p_block','__init__.py',40),
  ('block -> { statements RETURN expr ; }','block',6,'p_block_return','__init__.py',43),
  ('block -> { RETURN expr ; }','block',5,'p_block_immidiate_return','__init__.py',46),
  ('argument -> expr','argument',1,'p_argument','__init__.py',50),
  ('argument -> default_assign','argument',1,'p_argument','__init__.py',51),
  ('argument_list -> argument','argument_list',1,'p_argument_list','__init__.py',55),
  ('argument_list -> argument , argument_list','argument_list',3,'p_argument_list','__init__.py',56),
  ('function_argument -> expr','function_argument',1,'p_function_argument','__init__.py',63),
  ('function_argument_list -> function_argument','function_argument_list',1,'p_function_argument_list','__init__.py',67),
  ('function_argument_list -> function_argument , function_argument_list','function_argument_list',3,'p_function_argument_list','__init__.py',68),
  ('assign -> CONST ID = expr','assign',4,'p_assign_with_qualifier','__init__.py',75),
  ('assign -> ID = expr','assign',3,'p_assign','__init__.py',79),
  ('default_assign -> ID = expr','default_assign',3,'p_default_assign','__init__.py',83),
  ('expr -> term','expr',1,'p_expression','__init__.py',87),
  ('expr -> expr + term','expr',3,'p_expression','__init__.py',88),
  ('expr -> expr - term','expr',3,'p_expression','__init__.py',89),
  ('term -> factor','term',1,'p_term','__init__.py',100),
  ('term -> term * factor','term',3,'p_term','__init__.py',101),
  ('term -> term / factor','term',3,'p_term','__init__.py',102),
  ('term -> term ^ factor','term',3,'p_term','__init__.py',103),
  ('factor -> NUMBER','factor',1,'p_factor_constant','__init__.py',115),
  ('factor -> STRING','factor',1,'p_factor_constant','__init__.py',116),
  ('factor -> func_call','factor',1,'p_factor_constant','__init__.py',117),
  ('factor -> ID','factor',1,'p_factor_variable','__init__.py',121),
  ('factor -> ( expr )','factor',3,'p_factor_expr','__init__.py',125),
  ('func_call -> ID ( function_argument_list )','func_call',4,'p_func_call','__init__.py',129),
]
