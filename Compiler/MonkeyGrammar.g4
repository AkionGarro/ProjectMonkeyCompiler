grammar MonkeyGrammar;

//Productions
startRule: identifier;

//Comments
LINE_COMMENT : '//' .*? '\r'? '\n' -> skip ; // Match "//" stuff '\n'
COMMENT : '/*' .*? '*/' -> skip ; // Match "/*" stuff "*/"

//Caracteres ignorados
WS: (' '|'\t'|'\r'|'\n')+ -> skip;

//tokens
LETTER: [a-zA-Z_]*;
DIGIT: [0-9]*;


//Constantes booleana
Boolean: ('true' | 'false');

//Constante para cadena de caracteres
STRING : '"' .*? '"' ;

//Operadores relacionales
EQUAL: '==' ;
NOT_EQUAL: '!=' ;
LESS_THAN: '<' ;
LESS_THAN_OR_EQUAL: '<=' ;
GREATER_THAN: '>' ;
GREATER_THAN_OR_EQUAL: '>=' ;

//Operadores aritmeticos
PLUS: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DIVIDE: '/' ;
MODULO: '%' ;
DIVIDE_INT: '//' ;

//Operadores logicos
AND: '&&' ;
OR: '||' ;
NOT: '!' ;

//Operadores de asignacion
ASSIGN: '=' ;
ASSIGN_PLUS: '+=' ;
ASSIGN_MINUS: '-=' ;
ASSIGN_MULTIPLY: '*=' ;
ASSIGN_DIVIDE: '/=' ;
ASSIGN_MODULO: '%=' ;
ASSIGN_DIVIDE_INT: '//=' ;

//Brackets tokens
BLOCK_OPEN: '[';
BLOCK_CLOSE:']';
BRACKET_OPEN: '{';
BRACKET_CLOSE:'}';
PAR_OPEN: '(';
PAR_CLOSE:')';

//Otros caracteres o palabras reservadas
DOT: '.' ;
LET:'let';
RETURN:'return';
CHARIN: [a-zA-Z0-9]*;
QUOTE:'"';
Len: 'len';
First: 'first';
Last:'last';
Rest:'rest';
Push:'push';
COMMA: ',';
SEMICOLON: ';';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSEIF: 'elseif';
ELSE: 'else';
PUTS: 'puts';
FN: 'fn';


//Tokens
identifier:LETTER(LETTER|DIGIT)*;
char: QUOTE CHARIN QUOTE;


