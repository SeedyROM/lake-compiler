from ply import yacc
from lexer import tokens, literals

precedence = (
    ('left', '+', '-'),
    ('left', '/', '*'),
    ('left', 'DEF')
)

start = 'modules'

def p_empty(p):
    ''' empty : '''
    pass

def p_modules(p):
    ''' modules : module
                | modules module '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = ('MODULES', p[1], p[2])

def p_module(p):
    ''' module : DEFMODULE ID do_block '''
    p[0] = ('MODULE', p[2], p[3])

def p_statements(p):
    ''' statements : statement
                   | statements statement '''
    p[0] = p[1]

def p_statement(p):
    ''' statement : assignment
                  | function_definition
                  | private_function_definition
                  | do_block '''

    p[0] = p[1]

    # TODO:
    # | function_call
    # | struct_definition

def p_assignment_qualifier(p):
    ''' assignment_qualifier : CONST '''
    p[0] = p[1]

def p_assignment(p):
    ''' assignment : ID '=' expression
                   | assignment_qualifier ID '=' expression '''
    if(len(p) == 4):
        p[0] = ('ASSIGN', p[1], p[3])
    else:
        print(list(p))
        p[0] = (p[1].upper() + '_ASSIGN', p[2], p[4])

def p_function_definition(p):
    ''' function_definition : DEF ID '(' def_argument_list ')' do_block '''
    p[0] = ('FUNC_DEF', p[2], p[4], p[6])

def p_private_function_definition(p):
    ''' private_function_definition : DEFP ID '(' def_argument_list ')' do_block '''
    p[0] = ('PRIV_FUNC_DEF', p[2], p[4], p[6])

def p_function_def_argument(p):
    ''' def_argument : ID
                     | assignment '''
    p[0] = ('ARG', p[1])

def p_function_def_argument_list_empty(p):
    ''' def_argument_list : empty '''

def p_function_def_argument_list(p):
    ''' def_argument_list : def_argument
                          | def_argument_list ',' def_argument '''
    p[0] = ('ARGS', p[1])

def p_do_block_empty(p):
    ''' do_block : DO END '''

def p_do_return(p):
    ''' do_return : RETURN
                  | '' '''

def p_do_block(p):
    ''' do_block : DO statements END '''
    p[0] = ('DO_BLOCK', p[2])

def p_do_block_return(p):
    ''' do_block : DO statements do_return expression END '''
    p[0] = ('DO_BLOCK', p[2], ('RETURN', p[4]))

def p_do_block_return_immediate(p):
    ''' do_block : DO do_return expression END '''
    p[0] = ('DO_BLOCK', ('RETURN', p[3]))

def p_binary_expression(p):
    ''' expression : constant
                   | expression '+' constant
                   | expression '-' constant
                   | expression '*' constant
                   | expression '/' constant
                   | expression '^' constant
                   | expression '%' constant '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_constant(p):
    ''' constant : ID
                 | NUMBER
                 | STRING
                 | '(' expression ')' '''
    p[0] = p[1]

yacc.yacc()
