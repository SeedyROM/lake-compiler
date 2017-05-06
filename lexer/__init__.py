from ply import lex

reserved = {
    'CONST': 'const',
    'MUT': 'mut',
    'DEF': 'def',
    'DEFP': 'defp',
    'DEFMODULE': 'defmodule',
    'DO': 'do',
    'END': 'end',
    'RETURN': 'return',
    'IF': 'if',
    'ELSE_IF': 'else if',
    'ELSE': 'else',
    # 'FOR': 'for',
    # 'WHILE': 'while',
    'AND': 'and',
    'OR': 'or',

    # 'DEFSTRUCT': 'defstruct',
}

for k, v in reserved.items():
    exec('t_{} = r\'\b{}\b\''.format(k, v))

tokens = [
    'ID',
    'STRING',
    'NUMBER',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'EQ_GREATER_THAN',
    'EQ_LESS_THAN',
] + list(reserved.keys())

literals = ['+', '-', '=', '/',
            '*', ':', '{', '}',
            '(', ')', ';', '^',
            ',', '!', '>', '<']


t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_EQ_GREATER_THAN = r'>='
t_EQ_LESS_THAN = r'<='

t_NUMBER  = r'(\-?)\d+(\.\d{1,2})?'
t_ignore  = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reserved.keys():
        t.type = t.value.upper()
    return t

def t_STRING(t):
    r'\"(\\.|[^\"])*\"|\'(\\.|[^\"])*\''
    # t.value = str(t.value)[1:-1]
    t.value = str(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += 1

def t_LBRACE(t):
    r'\{'
    t.type = '{'
    return t

def t_RBRACE(t):
    r'\}'
    t.type = '}'
    return t


# #
# # Block state
# #
# states = (
#   ('BLOCK','exclusive'),
# )
#
# def t_BLOCK(t):
#     r'\bdo\b'
#     t.lexer.code_start = t.lexer.lexpos
#     t.lexer.level = 1
#     t.lexer.begin('BLOCK')
#     print(t.lexer.level)
#
# def t_BLOCK_DO(t):
#     r'\bdo\b'
#     t.lexer.level += 1
#     print("sdadhasjkdhjkhlaskjdlsa")
#
# def t_BLOCK_END(t):
#     r'\bend\b'
#     t.lexer.level -= 1
#     print("asdjakdhjkashdjklhaskhdjkashjdklsahjkdlhsajkl")
#
#     if(t.lexer.level == 0):
#         t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
#         t.type = "BLOCK"
#         t.lexer.lineno += t.value.count('\n')
#         t.lexer.begin('INITIAL')
#         return t
#
# t_BLOCK_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()
