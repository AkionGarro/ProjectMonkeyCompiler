grammar MonkeyGrammar;


//Comments

//Productions
startRule: identifier;

//Tokens
identifier:LETTER(LETTER|DIGIT)*;
char: QUOTE CHARIN QUOTE;
LET:'let';
RETURN:'return';


//Comparison tokens
GreaterT: '>';
LowerT: '<';
GreaterEQ:'>=';
LowerEQ:'<=';
Equeals:'==';


//Brackets tokens
BLOCK_OPEN: '[';
BLOCK_CLOSE:']';
BRACKET_OPEN: '{';
BRACKET_CLOSE:'}';
PAR_OPEN: '(';
PAR_CLOSE:')';


LETTER: [a-zA-Z_]*;
DIGIT: [0-9]*;
CHARIN: [a-zA-Z0-9]*;

QUOTE:'"';

NotEqueals:'!=';

//------------------------------------

//Comparison tokens
Sum: '+';
Res: '-';
Mul:'*';
Div:'/';
Mod:'%';
DivEnt:'//';

//comentario largo
Open: '/*';
Close: '*/';

Comment: Open [identifier] Close-> skip;

//arrayFunctions
Len: 'len';
First: 'first';
Last:'last';
Rest:'rest';
Push:'push';

//boolean
Boolean: (TRUE | FALSE);
WS: (' '|'\t'|'\r'|'\n')+ -> skip;

COMMA: ',';
SEMICOLON: ';';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';




