grammar MonkeyGrammar;

//Productions

//rogram:                    statement*                                              #programAST;

// create program with counter parameter
program:                      statement*                                            #programAST;


statement:                  LET letStatement                                        #statementLetAST
                            | RETURN (returnStatement| SEMICOLON | )               #statementReturnAST
                            | expressionStatement                                   #statementExpressionAST;

letStatement:               identifier ASSIGN expression ( SEMICOLON | )            #letStatementAST;

returnStatement:            expression ( SEMICOLON | )                              #returnStatementAST;

expressionStatement:        expression ( SEMICOLON | )                              #expressionStatementAST;

expression:                 additionExpression comparison                           #expressionAST;

comparison:                 ((LESS_THAN|GREATER_THAN
                            |LESS_THAN_OR_EQUAL|
                            GREATER_THAN_OR_EQUAL|
                            EQUAL|NOT_EQUAL) additionExpression)*                   #comparisonAST;

additionExpression:         multiplicationExpression additionFactor                 #additionExpressionAST;

additionFactor:             ((PLUS|MINUS) multiplicationExpression)*                #additionFactorAST;

multiplicationExpression:   elementExpression multiplicationFactor                  #multiplicationExpressionAST;

multiplicationFactor:       ((MULTIPLY|DIVIDE) elementExpression)*                  #multiplicationFactorAST;

elementExpression:          primitiveExpression (elementAccess | callExpression | ) #elementExpressionAST;

elementAccess:              BLOCK_OPEN expression BLOCK_CLOSE                       #elementAccessAST;

callExpression:             PAR_OPEN (expressionList | ) PAR_CLOSE                  #callExpressionAST;

primitiveExpression:        DIGIT                                                   #primitiveExprDigitAST
                            | boolean                                               #primitiveExprBooleanAST
                            | STRING                                                #primitiveExprStringAST
                            | identifier                                            #primitiveExprIdAST
                            | PAR_OPEN expression PAR_CLOSE                         #primitiveExprBlockExprAST
                            | arrayLiteral                                          #primitiveExprArrLitAST
                            | arrayFunctions PAR_OPEN expressionList PAR_CLOSE      #primitiveExprArrFuncAST
                            | functionLiteral                                       #primitiveExprFuncAST
                            | hashLiteral                                           #primitiveExprHashAST
                            | printExpression                                       #primitiveExprPrintAST
                            | ifExpression                                          #primitiveExprIfAST;

arrayFunctions: LEN | FIRST | LAST | REST | PUSH                                    #arrayFunctionsAST;

arrayLiteral: BLOCK_OPEN expressionList BLOCK_CLOSE                                 #arrayLitetalAST;

functionLiteral
locals [indice : int]
: FN PAR_OPEN functionParameters PAR_CLOSE blockStatement                           #functionLiteralAST;

functionParameters: ((identifier moreIdentifiers) | )                               #functionParametersAST;

moreIdentifiers: (COMMA identifier)*                                                #moreIdentifiersAST;

hashLiteral: BRACKET_OPEN hashContent moreHashContent BRACKET_CLOSE                 #hashLiteralAST;

hashContent: expression COLON expression                                            #hashContentAST;

moreHashContent: (COMMA hashContent)*                                               #moreHashContentAST;

expressionList: expression moreExpressions                                          #expressionListAST
                |                                                                   #expressionListEmptyAST;

moreExpressions: (COMMA expression)*                                                #moreExpressionsAST;

printExpression: PUTS PAR_OPEN expression PAR_CLOSE                                 #printExpressionAST;

ifExpression: IF expression blockStatement (ELSE blockStatement | )                 #ifExpressionAST;

blockStatement: BRACKET_OPEN statement* BRACKET_CLOSE                               #blockStatementAST;

identifier:LETTER(LETTER|DIGIT)*                                                    #identifierAST;

boolean: TRUE | FALSE                                                              #booleanAST;

char: QUOTE CHARIN QUOTE                                                            #charAST;

//line comment

//Comments
LINE_COMMENT : '//'.*?'\r'?'\n'->skip ; // Match "//" stuff '\n'
COMMENT : '/*'.*?'*/'->skip; // Match "/*" stuff "*/"


//Constantes booleana


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

CHARIN: [a-zA-Z0-9];

//Caracteres ignorados
WS: (' '|'\t'|'\r'|'\n')+ -> skip;