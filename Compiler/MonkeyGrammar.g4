
grammar MonkeyGrammar;


program: PROGRAM ID BRACKET_OPEN expr* BRACKET_CLOSE;

expr: var_decl;

var_decl: VAR ID SEMICOLON;


PROGRAM: 'program';
VAR: 'var';
PRINTLN: 'println';

PLUS:'+';
MINUS:'-';
MULT:'*';
DIV: '/';

AND: '&&';
OR: '||';
NOT:'!';
ASSIGN:'=';

GT: '>';
LT: '<';
GEQ:'>=';
LEQ:'<=';
EQ:'==';
NEQ:'!=';


BRACKET_OPEN: '{';
BRACKET_CLOSE:'}';
PAR_OPEN: '(';
PAR_CLOSE:')';

SEMICOLON:';';

ID: [a-zA-Z][a-zA-Z0-9]*;

NUMBER: [0-9]*;

WS: [ \t\n\r]+ ->skip;