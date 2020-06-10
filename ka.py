import ply.lex as lex
import ply.yacc as yacc
import sys

#_________get code content_________#
#TODO: replace hardcoded file by using sysarguments
fcode = open("tester.txt", "r")
contents = fcode.read()
fcode.close()


#_________TOKEN DEFINITIONS_________#
tokens = [
    'IDENTIFIER',
    'INT',
    'CHAR',
    'FLOAT',
    'STRING',
    'VOID',
    'INTTYPE',
    'CHARTYPE',
    'FLOATTYPE',
    'STRINGTYPE',
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'EXP',
    'EQUAL',
]
t_IDENTIFIER = r'[a-zA-Z_]\w*'
t_CHAR = r'\'.\''
t_STRING = r'"(.*?)"'
t_VOID = r'kawalan'
t_INTTYPE = r'bilang'
t_CHARTYPE = r'titik'
t_FLOATTYPE = r'lutang'
t_STRINGTYPE = r'hanay'
t_ADD = r'\+'
t_SUBTRACT = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EXP = r'eksp'
t_EQUAL = r'\='
def t_FLOAT(t):
    r'[-+]?\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'[-+]?\d+'
    t.value = int(t.value)
    return t
def t_newlinte(t):  # track line number
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    error_string = t.value + "\n" # make sure there's a new line
    error_string = error_string.split('\n', 1)[0] # get the line where the error is
    print("Illegal character '" + error_string + "'")
    print("\tLine:" + str(t.lexer.lineno) + ", Position: " + str(find_column(contents, t)))
    t.lexer.skip(1)
t_ignore = r' '


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return token.lexpos - line_start + 1

#_________BUILD LEXER_________#
lexer = lex.lex()
lexer.input(contents)
while True:
    tok = lexer.token()
    if not tok:
        break
    # print(tok)
