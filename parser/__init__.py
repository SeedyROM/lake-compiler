from ply import yacc
from lexer import tokens, literals

precedence = (
    ('left', '+', '-'),
    ('left', '/', '*'),
    ('right', 'ID'),
    ('nonassoc', 'EQUAL', 'NOT_EQUAL', 'GREATER_THAN', 'LESS_THAN', 'EQ_GREATER_THAN', 'EQ_LESS_THAN'),
    ('right', 'DO', 'ELSE', 'ELSE_IF')
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
    ''' statement : if_statement
                  | assignment
                  | function_definition
                  | private_function_definition
                  | do_block
                  | expression
                  | return_statement '''

    p[0] = p[1]

    # TODO:
    # | flow_control
    # | struct_definition

def p_return_statement(p):
    ''' return_statement : RETURN expression '''
    p[0] = ('RETURN', p[2])

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

def p_do_block(p):
    ''' do_block : DO statements END '''
    p[0] = ('DO_BLOCK', p[2])

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
        p[0] = ('BIN_EXPR', p[2], p[1], p[3])

def p_conditional_expression(p):
    ''' expression : expression GREATER_THAN constant
                   | expression LESS_THAN constant
                   | expression EQUAL constant
                   | expression NOT_EQUAL constant
                   | expression EQ_GREATER_THAN constant
                   | expression EQ_LESS_THAN constant '''
    p[0] = ('COND_EXPR', p[2], p[1], p[3])

def p_conditional_or_and_and(p):
    ''' expression : expression AND constant
                   | expression OR  constant '''
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

#
# TODO: Will this work?
#

def p_if_statement(p):
    ''' if_statement : IF '(' expression ')' DO statements else_blocks '''
    p[0] = ('IF_STMT', p[3], p[6], p[7])

def p_else_if_blocks(p):
    ''' else_blocks : else_if_block
                    | else_block
                    | END '''
    if(p[1] != 'end'):
        p[0] = p[1]

def p_else_block(p):
    ''' else_block : ELSE DO statements '''
    p[0] = p[3]

def p_else_if_block(p):
    ''' else_if_block : ELSE_IF '(' expression ')' DO statements else_blocks '''
    p[0] = ('IF_STMT', p[3], p[6], p[7])

def p_error(p):
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input!\nParser State: {}\n{} . {}'
          .format(parser.state,
                  stack_state_str,
                  p))

parser = yacc.yacc()
