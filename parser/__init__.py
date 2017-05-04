from ply import yacc
from lexer import lex, tokens

precedence = (
    ('left', '+', '-'),
    ('left', '/', '*'),
    ('left', 'DEF')
)

def p_module(p):
    ''' program : statements
                | program statements'''
    if(len(p) > 2):
        p[0] = p[1], p[2]
    else:
        p[0] = p[1]

def p_statements(p):
    ''' statements : statement
                   | statements statement '''
    if(len(p) > 2):
        p[0] = p[1], p[2]
    else:
        p[0] = p[1]

def p_statement(p):
    ''' statement : func_def
                  | assign ';'
                  | expr ';' '''
    p[0] = p[1]

def p_func_def(p):
    ''' func_def : DEF ID '(' argument_list ')' block '''
    p[0] = ('FUNC_DEF', p[2], ('ARGS', p[4]), p[6])

def p_block_empty(p):
    ''' block : '{' '}' '''
    p[0] = ('BLOCK', ())
def p_block(p):
    ''' block : '{' statements '}' '''
    p[0] = ('BLOCK', p[2])
def p_block_return(p):
    ''' block : '{' statements RETURN expr ';' '}' '''
    p[0] = ('BLOCK', p[2] + ('RETURN', p[4]))
def p_block_immidiate_return(p):
    ''' block : '{' RETURN expr ';' '}' '''
    p[0] = ('BLOCK', ('RETURN', p[3]))

def p_argument(p):
    ''' argument      : expr
                      | default_assign '''
    p[0] = ('ARG', p[1])

def p_argument_list(p):
    ''' argument_list : argument
                      | argument ',' argument_list '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_function_argument(p):
    ''' function_argument : expr '''
    p[0] = ('ARG', p[1])

def p_function_argument_list(p):
    ''' function_argument_list : function_argument
                               | function_argument ',' function_argument_list '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_assign_with_qualifier(p):
    ''' assign : CONST ID '=' expr '''
    p[0] = ('CONST_ASSIGN', p[2], p[4])

def p_assign(p):
    ''' assign : ID '=' expr '''
    p[0] = ('ASSIGN', p[1], p[3])

def p_default_assign(p):
    ''' default_assign : ID '=' expr '''
    p[0] = ('DEFAULT_ASSIGN', p[1], p[3])

def p_expression(p):
    ''' expr : term
             | expr '+' term
             | expr '-' term '''

    if(len(p) == 4):
        if(p[2] == '+'):
            p[0] = ('ADD', p[1], p[3])
        else:
            p[0] = ('SUB', p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    ''' term : factor
             | term '*' factor
             | term '/' factor
             | term '^' factor '''
    if(len(p) == 4):
        if(p[2] == '*'):
            p[0] = ('MULT', p[1], p[3])
        elif(p[2] == '/'):
            p[0] = ('DIV', p[1], p[3])
        else:
            p[0] = ('PWR', p[1], p[3])
    else:
        p[0] = p[1]

def p_factor_constant(p):
    ''' factor : NUMBER
               | STRING
               | func_call '''
    p[0] = ('CONST', p[1])

def p_factor_variable(p):
    ''' factor : ID '''
    p[0] = ('VAR', p[1])

def p_factor_expr(p):
    ''' factor : '(' expr ')' '''
    p[0] = ('EXPR', p[2])

def p_func_call(p):
    ''' func_call : ID '(' function_argument_list ')' '''
    p[0] = ('FUNC_CALL', p[1], ('ARGS', p[3]))

yacc.yacc()
