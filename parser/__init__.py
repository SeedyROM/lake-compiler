from ply import yacc
from lexer import tokens, literals

precedence = (
    ('left', '+', '-'),
    ('left', '/', '*'),
    ('left', 'DEF', 'DEFP')
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
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[1], p[2]

def p_statement(p):
    ''' statement : assignment
                  | function_definition
                  | private_function_definition
                  | do_block
                  | expression '''

    p[0] = p[1]

    # TODO:
    # | flow_control
    # | struct_definition

def p_assignment_qualifier(p):
    ''' assignment_qualifier : CONST
                             | MUT '''
    p[0] = p[1]

def p_assignment(p):
    ''' assignment : ID '=' expression
                   | assignment_qualifier ID '=' expression '''
    if(len(p) == 4):
        p[0] = ('ASSIGN', p[1], p[3])
    else:
        p[0] = (p[1].upper() + '_ASSIGN', p[2], p[4])

def p_function_definition(p):
    ''' function_definition : DEF ID '(' def_argument_list ')' do_block '''
    p[0] = ('FUNC_DEF', p[2], ('ARGS', p[4]), p[6])

def p_private_function_definition(p):
    ''' private_function_definition : DEFP ID '(' def_argument_list ')' do_block '''
    p[0] = ('PRIV_FUNC_DEF', p[2], ('ARGS', p[4]), p[6])

def p_function_def_argument(p):
    ''' def_argument : ID
                     | assignment_qualifier ID
                     | assignment '''
    if(len(p) == 2):
        p[0] = ('ARG', p[1])
    else:
        p[0] = (p[1].upper() + '_ARG', p[2])

def p_function_def_argument_list_empty(p):
    ''' def_argument_list : empty '''
    p[0] = ()

def p_function_def_argument_list(p):
    ''' def_argument_list : def_argument
                          | def_argument_list ',' def_argument '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

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
    ''' constant : NUMBER
                 | STRING '''
    p[0] = ('VAL_CONST', p[1])

def p_constant_function(p):
    ''' constant : function_call '''
    p[0] = p[1]

def p_constant_id(p):
    ''' constant : ID '''
    p[0] = ('VAL_VAR', p[1])

def p_constant_expression(p):
    ''' constant : '(' expression ')' '''
    p[0] = p[2]

def p_function_call(p):
    ''' function_call : ID '(' argument_list ')' '''
    p[0] = ('FUNC_CALL', p[1], ('ARGS', p[3]))

def p_function_argument(p):
    ''' argument : expression '''
    if(len(p) == 2):
        p[0] = ('ARG', p[1])
    else:
        p[0] = (p[1].upper() + '_ARG', p[2])

def p_function_argument_list_empty(p):
    ''' argument_list : empty '''
    p[0] = ()

def p_function_argument_list(p):
    ''' argument_list : argument
                      | argument_list ',' argument '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

# TODO: For tomorrow.
# def p_flow_control(p):
#     ''' flow_control : if_statement
#                      | for_statment
#                      | while_statement '''

yacc.yacc()
