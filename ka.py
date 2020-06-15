import ply.lex as lex
import ply.yacc as yacc
import sys

#_________get code content_________#
#TODO: replace hardcoded file by using sysarguments
# fcode = open("tester.txt", "r")
# contents = fcode.read()
# fcode.close()


#_________TOKEN DEFINITIONS_________#
tokens = [
    'IDENTIFIER',
    'COMMENT',
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
    'EQUALCOMP',
    'NOTEQUAL',
    'LESS_THAN_EQUAL',
    'LESS_THAN',
    'GREATER_THAN_EQUAL',
    'GREATER_THAN',
    'NOT',
    'OR',
    'AND',
    'PRINT',
    # 'INPUT',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
    'BREAK',
    'CONTINUE',
    'RETURN'
]
t_COMMENT = r'\#.*'
t_IDENTIFIER = r'[a-zA-Z_]\w*'
t_CHAR = r'\'.\''
t_STRING = r'"(.*?)"'
# t_INPUT = r'ipasok'
t_ADD = r'\+'
t_SUBTRACT = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALCOMP = r'\=\='
t_EQUAL = r'\='
t_NOTEQUAL = r'\!\='
t_LESS_THAN_EQUAL = r'\<\='
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUAL = r'\>\='
t_GREATER_THAN = r'\>'
t_NOT = r'\!'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'

def t_RETURN(t):
    r'ibalik'
    return t

def t_BREAK(t):
    r'itigil'
    return t

def t_CONTINUE(t):
    r'ituloy'
    return t

def t_FOR(t):
    r'parasa'
    return t

def t_WHILE(t):
    r'habang'
    return t

def t_PRINT(t):
    r'ilimbag'
    return t

def t_VOID(t):
    r'kawalan'
    return t

def t_INTTYPE(t):
    r'bilang'
    return t

def t_FLOATTYPE(t):
    r'bilang'
    return t

def t_CHARTYPE(t):
    r'titik'
    return t

def t_STRINGTYPE(t):
    r'hanay'
    return t

def t_ELSE(t):
    r'kunghindi'
    return t

def t_IF(t):
    r'kung'
    return t

def t_EXP(t):
    r'eksp'
    return t

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
# lexer.input(contents)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     # print(tok)


#_________PARSER_________#
# resolve warnings
# multiple expressions, assignments, statements?
# LPAREN RPAREN if if-else? -- expressions
# add ka to loops and if-else statement
# define statement contents

precedence = (
    ('left', 'EQUALCOMP', 'NOTEQUAL', 'GREATER_THAN_EQUAL', 'LESS_THAN_EQUAL', 'GREATER_THAN', 'LESS_THAN'),
    ('left','ADD','SUBTRACT'),
    ('left','EXP', 'MULTIPLY','DIVIDE'),
  )

names = {}

def p_ka(p):
    '''
    ka : expression SEMICOLON ka
       | assign SEMICOLON ka
       | print SEMICOLON ka
       | return SEMICOLON ka
       | if_statement ka
       | if_else_statement ka
       | while_statement ka
       | for_statement ka
       | function_statement ka
       | comment ka
       | empty
    '''
    f = open("output.txt","w")
    if p[1] != None:
      print(translate(p[1]))
    f.write(translate(p[1]))
    f.close()

def p_legal(p):
    '''
    legal : expression SEMICOLON legal
       | assign SEMICOLON legal
       | print SEMICOLON legal
       | if_statement legal
       | if_else_statement legal
       | while_statement legal
       | for_statement legal
       | empty
    '''

    if len(p) == 4 and p[3] != None:
      p[0] = (p[1],) + p[3]
    elif len(p) == 4 and p[3] == None:
      p[0] = (p[1],)
    elif len(p) == 3 and p[2] != None:
      p[0] = (p[1],) + p[2]
    elif len(p) == 3 and p[2] == None:
      p[0] = (p[1],)

def p_comment(p):
    '''
    comment : COMMENT
    '''

    p[0] = p[1]

def p_assign(p):
    '''
    assign : INTTYPE IDENTIFIER EQUAL INT
           | INTTYPE IDENTIFIER EQUAL expression
           | FLOATTYPE IDENTIFIER EQUAL expression
           | CHARTYPE IDENTIFIER EQUAL CHAR
           | FLOATTYPE IDENTIFIER EQUAL FLOAT
           | STRINGTYPE IDENTIFIER EQUAL STRING
    '''

    p[0] = ('=', p[2], p[4])

def p_print(p):
  '''
  print : PRINT LPAREN expression RPAREN
  '''
  
  p[0] = (p[1], p[3])

def p_return(p):
  '''
  return : RETURN expression
         | RETURN IDENTIFIER
  '''
  
  p[0] = (p[1], p[2])

def p_expression_binary(p):
    '''
    expression : expression ADD expression
               | expression SUBTRACT expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression EXP expression
    '''

    # if p[2] == '+':
    #     p[0] = p[1] + p[3]
    # elif p[2] == '-':
    #     p[0] = p[1] - p[3]
    # elif p[2] == '*':
    #     p[0] = p[1] * p[3]
    # elif p[2] == '/':
    #     p[0] = p[1] / p[3]
    # elif p[2] == "eksp":
    #     p[0] = p[1] ** p[3]
    
    p[0] = (p[2], p[1], p[3])

def p_expression_binary_compare(p):
    '''
    expression : expression EQUALCOMP expression
               | expression GREATER_THAN_EQUAL expression
               | expression LESS_THAN_EQUAL expression
               | expression GREATER_THAN expression
               | expression LESS_THAN expression
               | expression NOTEQUAL expression
    '''

    # if p[2] == "==":
    #   p[0] = p[1] == p[3]
    # elif p[2] == ">=":
    #   p[0] = p[1] >= p[3]
    # elif p[2] == "<=":
    #   p[0] = p[1] <= p[3]
    # elif p[2] == ">":
    #   p[0] = p[1] > p[3]
    # elif p[2] == "<":
    #   p[0] = p[1] < p[3]
    # elif p[2] == "!=":
    #   p[0] = p[1] != p[3]

    p[0] = (p[2], p[1], p[3])

def p_expression_unary(p):
    '''
    expression : NOT expression
    '''

    # p[0] = not (p[2])
    p[0] = (p[1], [2])

def p_expression_and_or(p):
    '''
    expression : expression AND expression
               | expression OR expression
    '''

    # if p[2] == "&&":
    #   p[0] = p[1] and p[3]
    # elif p[2] == "||":
    #   p[0] = p[1] or p[3]
    p[0] = (p[2], p[1], p[3])

def p_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''

    p[0] = p[1]

def p_continue_break(p):
    '''
    expression : CONTINUE
               | BREAK
    '''

    p[0] = p[1]

def p_expression_if(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE legal RBRACE
    '''

    p[0] = (p[1], p[2], p[3], p[4], p[5]) + p[6] + (p[7],)

def p_expression_if_else(p):
    '''
    if_else_statement : IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE LBRACE legal RBRACE
                      | IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_else_statement
                      | IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_statement
    '''

    # if p[3] and p[2] == '(':
    #   p[0] = p[6]
    # else:
    #   p[0] = p[10]

    if len(p) == 12:
      p[0] = (p[1], p[2], p[3], p[4], p[5]) + p[6] + (p[7], p[8], p[9]) + p[10] + (p[11],)
    else:
      p[0] = (p[1], p[2], p[3], p[4], p[5]) + p[6] +(p[7], p[8]) + p[9]

def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACE legal RBRACE
    '''

    p[0] = (p[1], p[2], p[3], p[4], p[5]) + p[6] + (p[7],)

def p_for_statement(p):
    '''
    for_statement : FOR LPAREN assign SEMICOLON expression SEMICOLON assign RPAREN LBRACE legal RBRACE
    '''

    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]) + p[10] + (p[11],)

def p_types(p):
    '''
    type_identifier : INTTYPE IDENTIFIER
                    | CHARTYPE IDENTIFIER
                    | FLOATTYPE IDENTIFIER
                    | STRINGTYPE IDENTIFIER
    '''

    p[0] = p[1], p[2]

def p_function(p):
    '''
    function_statement : type_identifier LPAREN function_input RPAREN LBRACE legal RBRACE
                       | VOID IDENTIFIER LPAREN function_input RPAREN LBRACE legal RBRACE
    '''

    if len(p) == 8:
      p[0] = p[1] + (p[2],) + p[3] + (p[4], p[5]) + p[6] + (p[7],)
    else:
      p[0] = (p[1], p[2], p[3]) + p[4] + (p[5], p[6]) + p[7] + (p[8],)

def p_function_input(p):
    '''
    function_input : type_identifier COMMA function_input
                   | type_identifier
    '''

    if len(p) > 2:
      p[0] = (p[1],) + (p[2],) + p[3]
    else:
      p[0] = (p[1],)

def p_expression_var(p):
    '''
    expression : IDENTIFIER
    '''

    p[0] = ("var", p[1])

def p_empty(p):
    '''
    empty :
    '''

    p[0] = None

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

#____________TRANSLATE___________#
def translate(p):
    #f = open("output.txt","w")
    #missing p_legal

    if type(p) == tuple:
        #for_if_statement_and_its_constituents
        if len(p) == 11:
            pstring = ''
            if p[0] == 'kung':
                pstring += 'if' + p[1] + translate(p[2]) + p[3] + p[4] + '\n' + translate(p[5]) + '\n' + p[6] + 'else' + p[8] + translate(p[9]) + p[10]
            if p[0] == 'parasa':
                pstring += 'for' + p[1] + translate(p[2]) + p[3] + translate(p[4]) + p[5] + translate(p[6]) + p[7] + p[8] + translate(p[9]) + p[10]
            return(pstring)
        #if_else
        elif len(p) == 9:
            if p[0] == 'kung':
                pstring = 'if' + p[1] + translate(p[2]) + p[3] + p[4] + '\n' + translate(p[5]) + '\n' + p[6] + 'else ' + translate(p[8]) 
                return(pstring)        
        #while_if_statement
        elif len(p) == 7:
            pstring = ''
            if p[0] == 'kung':
                pstring += 'if ' 
            if p[0] == 'habang':
                pstring += 'while '
            pstring += p[1] + translate(p[2]) + p[3] + p[4] + '\n' + translate(p[5]) + '\n' + p[6]
            return(pstring)
        # expressions and other stuff
        elif len(p) == 3:
            #eksp
            if p[0] == 'eksp':
                return (p[1] + '**' + p[2])
            #function_input
            elif p[1] == ',':
                return (translate(p[0]) + p[1] + translate(p[2]))
            else:
                return (str(p[1]) + str(p[0]) + str(p[2]))
        # return
        elif len(p) == 2:
            if p[0] == 'ilimbag':
               return ('printf(' + translate(p[1]) + ')')
            elif p[0] == 'ibalik':
                return('return ' + translate(p[1]))
            else:
                return(str(p[0]) + translate(p[1]))                
    else:
        if(type(p) == string):
            if p == 'ituloy':
                p = 'continue'
            if p == 'itigil':
                p = 'break'
        return str(p)
    #return p

while True: 
    try:
        s = input('ka> ')
    except EOFError:
        break
    print(parser.parse(s))