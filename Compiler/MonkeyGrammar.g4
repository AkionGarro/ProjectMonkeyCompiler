grammar MonkeyGrammar;

//Productions

program:                    statement*;

statement:                  LET letStatement | RETURN returnStatement | expressionStatement;

letStatement:               identifier ASSIGN expression ( SEMICOLON | );

returnStatement:            expression ( SEMICOLON | );

expressionStatement:        expression ( SEMICOLON | );

expression:                 additionExpression comparison;

comparison:                 ((LESS_THAN|GREATER_THAN|LESS_THAN_OR_EQUAL|GREATER_THAN_OR_EQUAL|EQUAL|NOT_EQUAL) additionExpression)*;

additionExpression:         multiplicationExpression additionFactor;

additionFactor:             ((PLUS|MINUS) multiplicationExpression)*;

multiplicationExpression:   elementExpression multiplicationFactor;

multiplicationFactor:       ((MULTIPLY|DIVIDE) elementExpression)*;

elementExpression:          primitiveExpression (elementAccess | callExpression | );

elementAccess:              BLOCK_OPEN expression BLOCK_CLOSE;

callExpression:             PAR_OPEN expressionList PAR_CLOSE;

primitiveExpression:        DIGIT | STRING | identifier | TRUE | FALSE | PAR_OPEN expression PAR_CLOSE | arrayLiteral
                            | arrayFunctions PAR_OPEN expressionList PAR_CLOSE | functionLiteral | hashLiteral
                            | printExpression | ifExpression;

arrayFunctions: LEN | FIRST | LAST | REST | PUSH;

arrayLiteral: BLOCK_OPEN expressionList BLOCK_CLOSE;

functionLiteral: FN PAR_OPEN functionParameters PAR_CLOSE blockStatement;

functionParameters: identifier moreIdentifiers;

moreIdentifiers: (COMMA identifier)*;

hashLiteral: BRACKET_OPEN hashContent moreHashContent BRACKET_CLOSE;

hashContent: expression COLON expression;

moreHashContent: (COMMA hashContent)*;

expressionList: expression moreExpressions | ;

moreExpressions: (COMMA expression)*;

printExpression: PUTS PAR_OPEN expression PAR_CLOSE;

ifExpression: IF expression blockStatement (ELSE blockStatement | );

blockStatement: BRACKET_OPEN statement* BRACKET_CLOSE;

identifier:LETTER(LETTER|DIGIT)*;

char: QUOTE CHARIN QUOTE;

//line comment

//Comments
LINE_COMMENT : '//'.*?'\r'?'\n'->skip ; // Match "//" stuff '\n'
COMMENT : '/*'.*?'*/'->skip; // Match "/*" stuff "*/"


//Constantes booleana
Boolean: ('true' | 'false');

//Constante para cadena de caracteres
STRING : '"' .*? '"' ;
INTEGER: 'integer';

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
DIVIDE_INT: '//' ; //19

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


//Arrays Functions
LEN: 'len';
FIRST: 'first';
LAST:'last';
REST:'rest';
PUSH:'push';

//Otros caracteres o palabras reservadas
LET:'let';
RETURN:'return';
DOT: '.' ;
QUOTE:'"';
COMMA: ',';
SEMICOLON: ';';
COLON:':';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSEIF: 'elseif';
ELSE: 'else';
PUTS: 'puts';
FN: 'fn';


//tokens
LETTER: [a-zA-Z_]*;

DIGIT: [0-9]*;

CHARIN: [a-zA-Z0-9]*;

//Caracteres ignorados
WS: (' '|'\t'|'\r'|'\n')+ -> skip;