
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQUALCOMPNOTEQUALGREATER_THAN_EQUALLESS_THAN_EQUALGREATER_THANLESS_THANleftADDSUBTRACTleftEXPMULTIPLYDIVIDEADD AND BREAK CHAR CHARTYPE COMMA COMMENT CONTINUE DIVIDE ELSE EQUAL EQUALCOMP EXP FLOAT FLOATTYPE FOR GREATER_THAN GREATER_THAN_EQUAL IDENTIFIER IF INPUT INT INTTYPE LBRACE LESS_THAN LESS_THAN_EQUAL LPAREN MULTIPLY NOT NOTEQUAL OR PRINT RBRACE RETURN RPAREN SEMICOLON STRING STRINGTYPE SUBTRACT VOID WHILE\n    ka : expression SEMICOLON ka\n       | assign SEMICOLON ka\n       | print SEMICOLON ka\n       | input SEMICOLON ka\n       | if_statement ka\n       | if_else_statement ka\n       | while_statement ka\n       | for_statement ka\n       | function_statement ka\n       | comment ka\n       | empty\n    \n    legal : expression SEMICOLON legal\n       | assign SEMICOLON legal\n       | print SEMICOLON legal\n       | input SEMICOLON legal\n       | return SEMICOLON legal\n       | if_statement legal\n       | if_else_statement legal\n       | while_statement legal\n       | for_statement legal\n       | empty\n    \n    comment : COMMENT\n    \n    assign : INTTYPE IDENTIFIER EQUAL INT\n           | INTTYPE IDENTIFIER EQUAL expression\n           | FLOATTYPE IDENTIFIER EQUAL expression\n           | CHARTYPE IDENTIFIER EQUAL CHAR\n           | FLOATTYPE IDENTIFIER EQUAL FLOAT\n           | STRINGTYPE IDENTIFIER EQUAL STRING\n           | INTTYPE IDENTIFIER\n           | FLOATTYPE IDENTIFIER\n           | CHARTYPE IDENTIFIER\n           | STRINGTYPE IDENTIFIER\n    \n  print : PRINT LPAREN expression RPAREN\n  \n  input : IDENTIFIER EQUAL INPUT LPAREN RPAREN\n  \n  return : RETURN expression\n         | RETURN IDENTIFIER\n  \n    expression : expression ADD expression\n               | expression SUBTRACT expression\n               | expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression EXP expression\n               | LPAREN expression RPAREN\n    \n    expression : expression EQUALCOMP expression\n               | expression GREATER_THAN_EQUAL expression\n               | expression LESS_THAN_EQUAL expression\n               | expression GREATER_THAN expression\n               | expression LESS_THAN expression\n               | expression NOTEQUAL expression\n    \n    expression : NOT expression\n    \n    expression : expression AND expression\n               | expression OR expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : CONTINUE\n               | BREAK\n    \n    if_statement : IF LPAREN expression RPAREN LBRACE legal RBRACE\n    \n    if_else_statement : IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE LBRACE legal RBRACE\n                      | IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_else_statement\n                      | IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_statement\n    \n    while_statement : WHILE LPAREN expression RPAREN LBRACE legal RBRACE\n    \n    for_statement : FOR LPAREN assign SEMICOLON expression SEMICOLON assign RPAREN LBRACE legal RBRACE\n    \n    type_identifier : INTTYPE IDENTIFIER\n                    | CHARTYPE IDENTIFIER\n                    | FLOATTYPE IDENTIFIER\n                    | STRINGTYPE IDENTIFIER\n    \n    function_statement : type_identifier LPAREN function_input RPAREN LBRACE legal RBRACE\n                       | VOID IDENTIFIER LPAREN function_input RPAREN LBRACE legal RBRACE\n    \n    function_input : type_identifier COMMA function_input\n                   | type_identifier\n                   | empty\n    \n    expression : IDENTIFIER\n    \n    empty :\n    '
    
_lr_action_items = {'LPAREN':([0,6,7,8,9,10,11,13,14,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,67,86,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,176,177,178,179,180,181,185,186,188,190,],[13,13,13,13,13,13,13,13,13,62,63,64,65,66,-22,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-62,-64,-63,-65,13,13,13,106,107,13,13,13,13,13,13,13,13,13,13,13,13,13,-56,13,13,13,13,-60,-66,-67,181,13,-58,-59,13,13,-57,-61,13,-56,]),'NOT':([0,6,7,8,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[14,14,14,14,14,14,14,14,14,-22,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-56,14,14,14,14,-60,-66,-67,14,-58,-59,14,14,-57,-61,14,-56,]),'INT':([0,6,7,8,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[15,15,15,15,15,15,15,15,15,-22,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,108,15,15,15,15,15,15,15,15,15,15,15,15,-56,15,15,15,15,-60,-66,-67,15,-58,-59,15,15,-57,-61,15,-56,]),'FLOAT':([0,6,7,8,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[16,16,16,16,16,16,16,16,16,-22,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,111,16,16,16,16,16,16,16,16,16,16,16,-56,16,16,16,16,-60,-66,-67,16,-58,-59,16,16,-57,-61,16,-56,]),'CONTINUE':([0,6,7,8,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[17,17,17,17,17,17,17,17,17,-22,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-56,17,17,17,17,-60,-66,-67,17,-58,-59,17,17,-57,-61,17,-56,]),'BREAK':([0,6,7,8,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[18,18,18,18,18,18,18,18,18,-22,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-56,18,18,18,18,-60,-66,-67,18,-58,-59,18,18,-57,-61,18,-56,]),'IDENTIFIER':([0,6,7,8,9,10,11,13,14,20,21,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,95,96,97,98,102,103,104,105,117,130,131,134,138,139,144,145,147,151,152,153,156,157,158,159,164,166,175,177,178,179,180,181,185,186,188,190,],[19,19,19,19,19,19,19,55,55,58,59,60,61,67,-22,19,55,55,55,55,55,55,55,55,55,55,55,55,55,19,19,19,55,55,55,55,55,118,119,120,121,124,125,126,127,55,19,19,19,19,19,19,19,163,19,19,-56,19,19,19,19,-60,-66,-67,19,-58,-59,19,55,-57,-61,19,-56,]),'INTTYPE':([0,6,7,8,9,10,11,30,31,45,46,47,65,66,106,122,130,131,134,138,139,144,145,149,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[20,20,20,20,20,20,20,-22,20,20,20,20,95,102,102,102,95,95,95,95,95,95,95,95,95,95,-56,95,95,95,95,-60,-66,-67,95,-58,-59,95,-57,-61,95,-56,]),'FLOATTYPE':([0,6,7,8,9,10,11,30,31,45,46,47,65,66,106,122,130,131,134,138,139,144,145,149,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[21,21,21,21,21,21,21,-22,21,21,21,21,96,104,104,104,96,96,96,96,96,96,96,96,96,96,-56,96,96,96,96,-60,-66,-67,96,-58,-59,96,-57,-61,96,-56,]),'CHARTYPE':([0,6,7,8,9,10,11,30,31,45,46,47,65,66,106,122,130,131,134,138,139,144,145,149,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[22,22,22,22,22,22,22,-22,22,22,22,22,97,103,103,103,97,97,97,97,97,97,97,97,97,97,-56,97,97,97,97,-60,-66,-67,97,-58,-59,97,-57,-61,97,-56,]),'STRINGTYPE':([0,6,7,8,9,10,11,30,31,45,46,47,65,66,106,122,130,131,134,138,139,144,145,149,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[23,23,23,23,23,23,23,-22,23,23,23,23,98,105,105,105,98,98,98,98,98,98,98,98,98,98,-56,98,98,98,98,-60,-66,-67,98,-58,-59,98,-57,-61,98,-56,]),'PRINT':([0,6,7,8,9,10,11,30,31,45,46,47,130,131,134,138,139,144,145,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[24,24,24,24,24,24,24,-22,24,24,24,24,24,24,24,24,24,24,24,24,24,-56,24,24,24,24,-60,-66,-67,24,-58,-59,24,-57,-61,24,-56,]),'IF':([0,6,7,8,9,10,11,30,31,45,46,47,130,131,134,138,139,144,145,151,152,153,156,157,158,159,164,166,169,175,177,178,179,180,185,186,188,190,],[25,25,25,25,25,25,25,-22,25,25,25,25,25,25,25,25,25,25,25,25,25,-56,25,25,25,25,-60,-66,176,-67,25,-58,-59,25,-57,-61,25,-56,]),'WHILE':([0,6,7,8,9,10,11,30,31,45,46,47,130,131,134,138,139,144,145,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[26,26,26,26,26,26,26,-22,26,26,26,26,26,26,26,26,26,26,26,26,26,-56,26,26,26,26,-60,-66,-67,26,-58,-59,26,-57,-61,26,-56,]),'FOR':([0,6,7,8,9,10,11,30,31,45,46,47,130,131,134,138,139,144,145,151,152,153,156,157,158,159,164,166,175,177,178,179,180,185,186,188,190,],[27,27,27,27,27,27,27,-22,27,27,27,27,27,27,27,27,27,27,27,27,27,-56,27,27,27,27,-60,-66,-67,27,-58,-59,27,-57,-61,27,-56,]),'VOID':([0,6,7,8,9,10,11,30,31,45,46,47,153,164,166,175,178,179,185,186,190,],[29,29,29,29,29,29,29,-22,29,29,29,29,-56,-60,-66,-67,-58,-59,-57,-61,-56,]),'COMMENT':([0,6,7,8,9,10,11,30,31,45,46,47,153,164,166,175,178,179,185,186,190,],[30,30,30,30,30,30,30,-22,30,30,30,30,-56,-60,-66,-67,-58,-59,-57,-61,-56,]),'$end':([0,1,6,7,8,9,10,11,12,30,31,45,46,47,48,49,50,51,52,53,68,82,83,84,153,164,166,175,178,179,185,186,190,],[-72,0,-72,-72,-72,-72,-72,-72,-11,-22,-72,-72,-72,-72,-5,-6,-7,-8,-9,-10,-1,-2,-3,-4,-56,-60,-66,-67,-58,-59,-57,-61,-56,]),'SEMICOLON':([2,3,4,5,15,16,17,18,19,55,56,58,59,60,61,69,70,71,72,73,74,75,76,77,78,79,80,81,85,94,108,109,110,111,112,113,114,118,119,120,121,129,132,136,140,141,142,143,162,163,],[31,45,46,47,-52,-53,-54,-55,-71,-71,-49,-29,-30,-31,-32,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,-50,-51,-42,117,-23,-24,-25,-27,-26,-28,-33,-29,-30,-31,-32,-34,149,152,156,157,158,159,-35,-36,]),'ADD':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[32,-52,-53,-54,-55,-71,32,-71,32,-37,-38,-39,-40,-41,32,32,32,32,32,32,32,32,-42,32,32,32,-52,32,32,-53,32,32,32,-71,32,]),'SUBTRACT':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[33,-52,-53,-54,-55,-71,33,-71,33,-37,-38,-39,-40,-41,33,33,33,33,33,33,33,33,-42,33,33,33,-52,33,33,-53,33,33,33,-71,33,]),'MULTIPLY':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[34,-52,-53,-54,-55,-71,34,-71,34,34,34,-39,-40,-41,34,34,34,34,34,34,34,34,-42,34,34,34,-52,34,34,-53,34,34,34,-71,34,]),'DIVIDE':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[35,-52,-53,-54,-55,-71,35,-71,35,35,35,-39,-40,-41,35,35,35,35,35,35,35,35,-42,35,35,35,-52,35,35,-53,35,35,35,-71,35,]),'EXP':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[36,-52,-53,-54,-55,-71,36,-71,36,36,36,-39,-40,-41,36,36,36,36,36,36,36,36,-42,36,36,36,-52,36,36,-53,36,36,36,-71,36,]),'EQUALCOMP':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[37,-52,-53,-54,-55,-71,37,-71,37,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,37,37,-42,37,37,37,-52,37,37,-53,37,37,37,-71,37,]),'GREATER_THAN_EQUAL':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[38,-52,-53,-54,-55,-71,38,-71,38,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,38,38,-42,38,38,38,-52,38,38,-53,38,38,38,-71,38,]),'LESS_THAN_EQUAL':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[39,-52,-53,-54,-55,-71,39,-71,39,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,39,39,-42,39,39,39,-52,39,39,-53,39,39,39,-71,39,]),'GREATER_THAN':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[40,-52,-53,-54,-55,-71,40,-71,40,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,40,40,-42,40,40,40,-52,40,40,-53,40,40,40,-71,40,]),'LESS_THAN':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[41,-52,-53,-54,-55,-71,41,-71,41,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,41,41,-42,41,41,41,-52,41,41,-53,41,41,41,-71,41,]),'NOTEQUAL':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[42,-52,-53,-54,-55,-71,42,-71,42,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,42,42,-42,42,42,42,-52,42,42,-53,42,42,42,-71,42,]),'AND':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[43,-52,-53,-54,-55,-71,43,-71,43,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,43,43,-42,43,43,43,-52,43,43,-53,43,43,43,-71,43,]),'OR':([2,15,16,17,18,19,54,55,56,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,108,109,110,111,132,136,162,163,184,],[44,-52,-53,-54,-55,-71,44,-71,44,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,44,44,-42,44,44,44,-52,44,44,-53,44,44,44,-71,44,]),'RPAREN':([15,16,17,18,54,55,56,66,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,92,93,99,100,101,106,107,108,109,110,111,112,113,118,119,120,121,122,124,125,126,127,128,133,165,184,],[-52,-53,-54,-55,85,-71,-49,-72,-37,-38,-39,-40,-41,-43,-44,-45,-46,-47,-48,-50,-51,-42,114,115,116,-69,123,-70,-72,129,-23,-24,-25,-27,-26,-28,-29,-30,-31,-32,-72,-62,-63,-64,-65,135,-68,174,187,]),'EQUAL':([19,58,59,60,61,118,119,120,121,],[57,87,88,89,90,87,88,89,90,]),'INPUT':([57,],[86,]),'CHAR':([89,],[112,]),'STRING':([90,],[113,]),'COMMA':([99,124,125,126,127,],[122,-62,-63,-64,-65,]),'LBRACE':([115,116,123,135,169,174,187,],[130,131,134,151,177,180,188,]),'RETURN':([130,131,134,138,139,144,145,151,152,153,156,157,158,159,164,177,178,179,180,185,186,188,190,],[147,147,147,147,147,147,147,147,147,-56,147,147,147,147,-60,147,-58,-59,147,-57,-61,147,-56,]),'RBRACE':([130,131,134,137,138,139,144,145,146,148,150,151,152,153,154,155,156,157,158,159,160,161,164,167,168,170,171,172,173,177,178,179,180,182,183,185,186,188,189,190,],[-72,-72,-72,153,-72,-72,-72,-72,-21,164,166,-72,-72,-56,-18,-17,-72,-72,-72,-72,-19,-20,-60,175,-12,-13,-14,-15,-16,-72,-58,-59,-72,185,186,-57,-61,-72,190,-56,]),'ELSE':([153,190,],[169,169,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ka':([0,6,7,8,9,10,11,31,45,46,47,],[1,48,49,50,51,52,53,68,82,83,84,]),'expression':([0,6,7,8,9,10,11,13,14,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,87,88,117,130,131,134,138,139,144,145,147,151,152,156,157,158,159,177,180,181,188,],[2,2,2,2,2,2,2,54,56,2,69,70,71,72,73,74,75,76,77,78,79,80,81,2,2,2,91,92,93,109,110,132,136,136,136,136,136,136,136,162,136,136,136,136,136,136,136,136,184,136,]),'assign':([0,6,7,8,9,10,11,31,45,46,47,65,130,131,134,138,139,144,145,149,151,152,156,157,158,159,177,180,188,],[3,3,3,3,3,3,3,3,3,3,3,94,140,140,140,140,140,140,140,165,140,140,140,140,140,140,140,140,140,]),'print':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[4,4,4,4,4,4,4,4,4,4,4,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,141,]),'input':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[5,5,5,5,5,5,5,5,5,5,5,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,]),'if_statement':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,169,177,180,188,],[6,6,6,6,6,6,6,6,6,6,6,139,139,139,139,139,139,139,139,139,139,139,139,139,179,139,139,139,]),'if_else_statement':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,169,177,180,188,],[7,7,7,7,7,7,7,7,7,7,7,138,138,138,138,138,138,138,138,138,138,138,138,138,178,138,138,138,]),'while_statement':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[8,8,8,8,8,8,8,8,8,8,8,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,]),'for_statement':([0,6,7,8,9,10,11,31,45,46,47,130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[9,9,9,9,9,9,9,9,9,9,9,145,145,145,145,145,145,145,145,145,145,145,145,145,145,145,145,]),'function_statement':([0,6,7,8,9,10,11,31,45,46,47,],[10,10,10,10,10,10,10,10,10,10,10,]),'comment':([0,6,7,8,9,10,11,31,45,46,47,],[11,11,11,11,11,11,11,11,11,11,11,]),'empty':([0,6,7,8,9,10,11,31,45,46,47,66,106,122,130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[12,12,12,12,12,12,12,12,12,12,12,101,101,101,146,146,146,146,146,146,146,146,146,146,146,146,146,146,146,146,]),'type_identifier':([0,6,7,8,9,10,11,31,45,46,47,66,106,122,],[28,28,28,28,28,28,28,28,28,28,28,99,99,99,]),'function_input':([66,106,122,],[100,128,133,]),'legal':([130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[137,148,150,154,155,160,161,167,168,170,171,172,173,182,183,189,]),'return':([130,131,134,138,139,144,145,151,152,156,157,158,159,177,180,188,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ka","S'",1,None,None,None),
  ('ka -> expression SEMICOLON ka','ka',3,'p_ka','ka.py',192),
  ('ka -> assign SEMICOLON ka','ka',3,'p_ka','ka.py',193),
  ('ka -> print SEMICOLON ka','ka',3,'p_ka','ka.py',194),
  ('ka -> input SEMICOLON ka','ka',3,'p_ka','ka.py',195),
  ('ka -> if_statement ka','ka',2,'p_ka','ka.py',196),
  ('ka -> if_else_statement ka','ka',2,'p_ka','ka.py',197),
  ('ka -> while_statement ka','ka',2,'p_ka','ka.py',198),
  ('ka -> for_statement ka','ka',2,'p_ka','ka.py',199),
  ('ka -> function_statement ka','ka',2,'p_ka','ka.py',200),
  ('ka -> comment ka','ka',2,'p_ka','ka.py',201),
  ('ka -> empty','ka',1,'p_ka','ka.py',202),
  ('legal -> expression SEMICOLON legal','legal',3,'p_legal','ka.py',212),
  ('legal -> assign SEMICOLON legal','legal',3,'p_legal','ka.py',213),
  ('legal -> print SEMICOLON legal','legal',3,'p_legal','ka.py',214),
  ('legal -> input SEMICOLON legal','legal',3,'p_legal','ka.py',215),
  ('legal -> return SEMICOLON legal','legal',3,'p_legal','ka.py',216),
  ('legal -> if_statement legal','legal',2,'p_legal','ka.py',217),
  ('legal -> if_else_statement legal','legal',2,'p_legal','ka.py',218),
  ('legal -> while_statement legal','legal',2,'p_legal','ka.py',219),
  ('legal -> for_statement legal','legal',2,'p_legal','ka.py',220),
  ('legal -> empty','legal',1,'p_legal','ka.py',221),
  ('comment -> COMMENT','comment',1,'p_comment','ka.py',235),
  ('assign -> INTTYPE IDENTIFIER EQUAL INT','assign',4,'p_assign','ka.py',242),
  ('assign -> INTTYPE IDENTIFIER EQUAL expression','assign',4,'p_assign','ka.py',243),
  ('assign -> FLOATTYPE IDENTIFIER EQUAL expression','assign',4,'p_assign','ka.py',244),
  ('assign -> CHARTYPE IDENTIFIER EQUAL CHAR','assign',4,'p_assign','ka.py',245),
  ('assign -> FLOATTYPE IDENTIFIER EQUAL FLOAT','assign',4,'p_assign','ka.py',246),
  ('assign -> STRINGTYPE IDENTIFIER EQUAL STRING','assign',4,'p_assign','ka.py',247),
  ('assign -> INTTYPE IDENTIFIER','assign',2,'p_assign','ka.py',248),
  ('assign -> FLOATTYPE IDENTIFIER','assign',2,'p_assign','ka.py',249),
  ('assign -> CHARTYPE IDENTIFIER','assign',2,'p_assign','ka.py',250),
  ('assign -> STRINGTYPE IDENTIFIER','assign',2,'p_assign','ka.py',251),
  ('print -> PRINT LPAREN expression RPAREN','print',4,'p_print','ka.py',261),
  ('input -> IDENTIFIER EQUAL INPUT LPAREN RPAREN','input',5,'p_input','ka.py',268),
  ('return -> RETURN expression','return',2,'p_return','ka.py',275),
  ('return -> RETURN IDENTIFIER','return',2,'p_return','ka.py',276),
  ('expression -> expression ADD expression','expression',3,'p_expression_binary','ka.py',283),
  ('expression -> expression SUBTRACT expression','expression',3,'p_expression_binary','ka.py',284),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binary','ka.py',285),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binary','ka.py',286),
  ('expression -> expression EXP expression','expression',3,'p_expression_binary','ka.py',287),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_binary','ka.py',288),
  ('expression -> expression EQUALCOMP expression','expression',3,'p_expression_binary_compare','ka.py',308),
  ('expression -> expression GREATER_THAN_EQUAL expression','expression',3,'p_expression_binary_compare','ka.py',309),
  ('expression -> expression LESS_THAN_EQUAL expression','expression',3,'p_expression_binary_compare','ka.py',310),
  ('expression -> expression GREATER_THAN expression','expression',3,'p_expression_binary_compare','ka.py',311),
  ('expression -> expression LESS_THAN expression','expression',3,'p_expression_binary_compare','ka.py',312),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binary_compare','ka.py',313),
  ('expression -> NOT expression','expression',2,'p_expression_unary','ka.py',333),
  ('expression -> expression AND expression','expression',3,'p_expression_and_or','ka.py',341),
  ('expression -> expression OR expression','expression',3,'p_expression_and_or','ka.py',342),
  ('expression -> INT','expression',1,'p_int_float','ka.py',353),
  ('expression -> FLOAT','expression',1,'p_int_float','ka.py',354),
  ('expression -> CONTINUE','expression',1,'p_continue_break','ka.py',361),
  ('expression -> BREAK','expression',1,'p_continue_break','ka.py',362),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE legal RBRACE','if_statement',7,'p_expression_if','ka.py',369),
  ('if_else_statement -> IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE LBRACE legal RBRACE','if_else_statement',11,'p_expression_if_else','ka.py',376),
  ('if_else_statement -> IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_else_statement','if_else_statement',9,'p_expression_if_else','ka.py',377),
  ('if_else_statement -> IF LPAREN expression RPAREN LBRACE legal RBRACE ELSE if_statement','if_else_statement',9,'p_expression_if_else','ka.py',378),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE legal RBRACE','while_statement',7,'p_while_statement','ka.py',393),
  ('for_statement -> FOR LPAREN assign SEMICOLON expression SEMICOLON assign RPAREN LBRACE legal RBRACE','for_statement',11,'p_for_statement','ka.py',400),
  ('type_identifier -> INTTYPE IDENTIFIER','type_identifier',2,'p_types','ka.py',407),
  ('type_identifier -> CHARTYPE IDENTIFIER','type_identifier',2,'p_types','ka.py',408),
  ('type_identifier -> FLOATTYPE IDENTIFIER','type_identifier',2,'p_types','ka.py',409),
  ('type_identifier -> STRINGTYPE IDENTIFIER','type_identifier',2,'p_types','ka.py',410),
  ('function_statement -> type_identifier LPAREN function_input RPAREN LBRACE legal RBRACE','function_statement',7,'p_function','ka.py',417),
  ('function_statement -> VOID IDENTIFIER LPAREN function_input RPAREN LBRACE legal RBRACE','function_statement',8,'p_function','ka.py',418),
  ('function_input -> type_identifier COMMA function_input','function_input',3,'p_function_input','ka.py',428),
  ('function_input -> type_identifier','function_input',1,'p_function_input','ka.py',429),
  ('function_input -> empty','function_input',1,'p_function_input','ka.py',430),
  ('expression -> IDENTIFIER','expression',1,'p_expression_var','ka.py',440),
  ('empty -> <empty>','empty',0,'p_empty','ka.py',447),
]
