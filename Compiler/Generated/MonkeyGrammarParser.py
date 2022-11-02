# Generated from C:/Users/bryam/Desktop/compi/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,256,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,2,1,2,1,2,
        1,2,1,2,3,2,84,8,2,1,3,1,3,1,3,3,3,89,8,3,1,3,1,3,3,3,93,8,3,1,4,
        1,4,1,4,3,4,98,8,4,1,5,1,5,1,5,1,6,1,6,5,6,105,8,6,10,6,12,6,108,
        9,6,1,7,1,7,1,7,1,8,1,8,5,8,115,8,8,10,8,12,8,118,9,8,1,9,1,9,1,
        9,1,10,1,10,5,10,125,8,10,10,10,12,10,128,9,10,1,11,1,11,1,11,1,
        11,3,11,134,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,143,8,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,165,8,14,1,15,1,15,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,
        3,18,183,8,18,1,19,1,19,5,19,187,8,19,10,19,12,19,190,9,19,1,20,
        1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,5,22,203,8,22,
        10,22,12,22,206,9,22,1,23,1,23,1,23,1,23,3,23,212,8,23,1,24,1,24,
        5,24,216,8,24,10,24,12,24,219,9,24,1,25,1,25,1,25,1,25,1,25,1,26,
        1,26,1,26,1,26,1,26,1,26,3,26,232,8,26,1,27,1,27,5,27,236,8,27,10,
        27,12,27,239,9,27,1,27,1,27,1,28,1,28,5,28,245,8,28,10,28,12,28,
        248,9,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,0,0,31,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,0,6,1,0,5,10,1,0,11,12,1,0,13,14,1,0,33,37,1,0,52,53,1,
        0,45,46,257,0,65,1,0,0,0,2,76,1,0,0,0,4,78,1,0,0,0,6,92,1,0,0,0,
        8,94,1,0,0,0,10,99,1,0,0,0,12,106,1,0,0,0,14,109,1,0,0,0,16,116,
        1,0,0,0,18,119,1,0,0,0,20,126,1,0,0,0,22,129,1,0,0,0,24,135,1,0,
        0,0,26,139,1,0,0,0,28,164,1,0,0,0,30,166,1,0,0,0,32,168,1,0,0,0,
        34,172,1,0,0,0,36,182,1,0,0,0,38,188,1,0,0,0,40,191,1,0,0,0,42,196,
        1,0,0,0,44,204,1,0,0,0,46,211,1,0,0,0,48,217,1,0,0,0,50,220,1,0,
        0,0,52,225,1,0,0,0,54,233,1,0,0,0,56,242,1,0,0,0,58,249,1,0,0,0,
        60,251,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,
        0,0,0,65,66,1,0,0,0,66,1,1,0,0,0,67,65,1,0,0,0,68,69,5,38,0,0,69,
        77,3,4,2,0,70,73,5,39,0,0,71,74,3,6,3,0,72,74,1,0,0,0,73,71,1,0,
        0,0,73,72,1,0,0,0,74,77,1,0,0,0,75,77,3,8,4,0,76,68,1,0,0,0,76,70,
        1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,79,3,56,28,0,79,80,5,20,0,
        0,80,83,3,10,5,0,81,84,5,43,0,0,82,84,1,0,0,0,83,81,1,0,0,0,83,82,
        1,0,0,0,84,5,1,0,0,0,85,88,3,10,5,0,86,89,5,43,0,0,87,89,1,0,0,0,
        88,86,1,0,0,0,88,87,1,0,0,0,89,93,1,0,0,0,90,93,5,43,0,0,91,93,1,
        0,0,0,92,85,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,7,1,0,0,0,94,
        97,3,10,5,0,95,98,5,43,0,0,96,98,1,0,0,0,97,95,1,0,0,0,97,96,1,0,
        0,0,98,9,1,0,0,0,99,100,3,14,7,0,100,101,3,12,6,0,101,11,1,0,0,0,
        102,103,7,0,0,0,103,105,3,14,7,0,104,102,1,0,0,0,105,108,1,0,0,0,
        106,104,1,0,0,0,106,107,1,0,0,0,107,13,1,0,0,0,108,106,1,0,0,0,109,
        110,3,18,9,0,110,111,3,16,8,0,111,15,1,0,0,0,112,113,7,1,0,0,113,
        115,3,18,9,0,114,112,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,
        117,1,0,0,0,117,17,1,0,0,0,118,116,1,0,0,0,119,120,3,22,11,0,120,
        121,3,20,10,0,121,19,1,0,0,0,122,123,7,2,0,0,123,125,3,22,11,0,124,
        122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,
        21,1,0,0,0,128,126,1,0,0,0,129,133,3,28,14,0,130,134,3,24,12,0,131,
        134,3,26,13,0,132,134,1,0,0,0,133,130,1,0,0,0,133,131,1,0,0,0,133,
        132,1,0,0,0,134,23,1,0,0,0,135,136,5,27,0,0,136,137,3,10,5,0,137,
        138,5,28,0,0,138,25,1,0,0,0,139,142,5,31,0,0,140,143,3,46,23,0,141,
        143,1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,
        145,5,32,0,0,145,27,1,0,0,0,146,165,5,53,0,0,147,165,3,58,29,0,148,
        165,5,3,0,0,149,165,3,56,28,0,150,151,5,31,0,0,151,152,3,10,5,0,
        152,153,5,32,0,0,153,165,1,0,0,0,154,165,3,32,16,0,155,156,3,30,
        15,0,156,157,5,31,0,0,157,158,3,46,23,0,158,159,5,32,0,0,159,165,
        1,0,0,0,160,165,3,34,17,0,161,165,3,40,20,0,162,165,3,50,25,0,163,
        165,3,52,26,0,164,146,1,0,0,0,164,147,1,0,0,0,164,148,1,0,0,0,164,
        149,1,0,0,0,164,150,1,0,0,0,164,154,1,0,0,0,164,155,1,0,0,0,164,
        160,1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,
        29,1,0,0,0,166,167,7,3,0,0,167,31,1,0,0,0,168,169,5,27,0,0,169,170,
        3,46,23,0,170,171,5,28,0,0,171,33,1,0,0,0,172,173,5,51,0,0,173,174,
        5,31,0,0,174,175,3,36,18,0,175,176,5,32,0,0,176,177,3,54,27,0,177,
        35,1,0,0,0,178,179,3,56,28,0,179,180,3,38,19,0,180,183,1,0,0,0,181,
        183,1,0,0,0,182,178,1,0,0,0,182,181,1,0,0,0,183,37,1,0,0,0,184,185,
        5,42,0,0,185,187,3,56,28,0,186,184,1,0,0,0,187,190,1,0,0,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,39,1,0,0,0,190,188,1,0,0,0,191,192,5,
        29,0,0,192,193,3,42,21,0,193,194,3,44,22,0,194,195,5,30,0,0,195,
        41,1,0,0,0,196,197,3,10,5,0,197,198,5,44,0,0,198,199,3,10,5,0,199,
        43,1,0,0,0,200,201,5,42,0,0,201,203,3,42,21,0,202,200,1,0,0,0,203,
        206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,45,1,0,0,0,206,204,
        1,0,0,0,207,208,3,10,5,0,208,209,3,48,24,0,209,212,1,0,0,0,210,212,
        1,0,0,0,211,207,1,0,0,0,211,210,1,0,0,0,212,47,1,0,0,0,213,214,5,
        42,0,0,214,216,3,10,5,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,
        1,0,0,0,217,218,1,0,0,0,218,49,1,0,0,0,219,217,1,0,0,0,220,221,5,
        50,0,0,221,222,5,31,0,0,222,223,3,10,5,0,223,224,5,32,0,0,224,51,
        1,0,0,0,225,226,5,47,0,0,226,227,3,10,5,0,227,231,3,54,27,0,228,
        229,5,49,0,0,229,232,3,54,27,0,230,232,1,0,0,0,231,228,1,0,0,0,231,
        230,1,0,0,0,232,53,1,0,0,0,233,237,5,29,0,0,234,236,3,2,1,0,235,
        234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,
        240,1,0,0,0,239,237,1,0,0,0,240,241,5,30,0,0,241,55,1,0,0,0,242,
        246,5,52,0,0,243,245,7,4,0,0,244,243,1,0,0,0,245,248,1,0,0,0,246,
        244,1,0,0,0,246,247,1,0,0,0,247,57,1,0,0,0,248,246,1,0,0,0,249,250,
        7,5,0,0,250,59,1,0,0,0,251,252,5,41,0,0,252,253,5,54,0,0,253,254,
        5,41,0,0,254,61,1,0,0,0,21,65,73,76,83,88,92,97,106,116,126,133,
        142,164,182,188,204,211,217,231,237,246
    ]

class MonkeyGrammarParser ( Parser ):

    grammarFileName = "MonkeyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'integer'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", 
                     "'&&'", "'||'", "'!'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'//='", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "'len'", "'first'", "'last'", "'rest'", 
                     "'push'", "'let'", "'return'", "'.'", "'\"'", "','", 
                     "';'", "':'", "'true'", "'false'", "'if'", "'elseif'", 
                     "'else'", "'puts'", "'fn'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "COMMENT", "STRING", 
                      "INTEGER", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "DIVIDE_INT", "AND", 
                      "OR", "NOT", "ASSIGN", "ASSIGN_PLUS", "ASSIGN_MINUS", 
                      "ASSIGN_MULTIPLY", "ASSIGN_DIVIDE", "ASSIGN_MODULO", 
                      "ASSIGN_DIVIDE_INT", "BLOCK_OPEN", "BLOCK_CLOSE", 
                      "BRACKET_OPEN", "BRACKET_CLOSE", "PAR_OPEN", "PAR_CLOSE", 
                      "LEN", "FIRST", "LAST", "REST", "PUSH", "LET", "RETURN", 
                      "DOT", "QUOTE", "COMMA", "SEMICOLON", "COLON", "TRUE", 
                      "FALSE", "IF", "ELSEIF", "ELSE", "PUTS", "FN", "LETTER", 
                      "DIGIT", "CHARIN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letStatement = 2
    RULE_returnStatement = 3
    RULE_expressionStatement = 4
    RULE_expression = 5
    RULE_comparison = 6
    RULE_additionExpression = 7
    RULE_additionFactor = 8
    RULE_multiplicationExpression = 9
    RULE_multiplicationFactor = 10
    RULE_elementExpression = 11
    RULE_elementAccess = 12
    RULE_callExpression = 13
    RULE_primitiveExpression = 14
    RULE_arrayFunctions = 15
    RULE_arrayLiteral = 16
    RULE_functionLiteral = 17
    RULE_functionParameters = 18
    RULE_moreIdentifiers = 19
    RULE_hashLiteral = 20
    RULE_hashContent = 21
    RULE_moreHashContent = 22
    RULE_expressionList = 23
    RULE_moreExpressions = 24
    RULE_printExpression = 25
    RULE_ifExpression = 26
    RULE_blockStatement = 27
    RULE_identifier = 28
    RULE_boolean = 29
    RULE_char = 30

    ruleNames =  [ "program", "statement", "letStatement", "returnStatement", 
                   "expressionStatement", "expression", "comparison", "additionExpression", 
                   "additionFactor", "multiplicationExpression", "multiplicationFactor", 
                   "elementExpression", "elementAccess", "callExpression", 
                   "primitiveExpression", "arrayFunctions", "arrayLiteral", 
                   "functionLiteral", "functionParameters", "moreIdentifiers", 
                   "hashLiteral", "hashContent", "moreHashContent", "expressionList", 
                   "moreExpressions", "printExpression", "ifExpression", 
                   "blockStatement", "identifier", "boolean", "char" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    COMMENT=2
    STRING=3
    INTEGER=4
    EQUAL=5
    NOT_EQUAL=6
    LESS_THAN=7
    LESS_THAN_OR_EQUAL=8
    GREATER_THAN=9
    GREATER_THAN_OR_EQUAL=10
    PLUS=11
    MINUS=12
    MULTIPLY=13
    DIVIDE=14
    MODULO=15
    DIVIDE_INT=16
    AND=17
    OR=18
    NOT=19
    ASSIGN=20
    ASSIGN_PLUS=21
    ASSIGN_MINUS=22
    ASSIGN_MULTIPLY=23
    ASSIGN_DIVIDE=24
    ASSIGN_MODULO=25
    ASSIGN_DIVIDE_INT=26
    BLOCK_OPEN=27
    BLOCK_CLOSE=28
    BRACKET_OPEN=29
    BRACKET_CLOSE=30
    PAR_OPEN=31
    PAR_CLOSE=32
    LEN=33
    FIRST=34
    LAST=35
    REST=36
    PUSH=37
    LET=38
    RETURN=39
    DOT=40
    QUOTE=41
    COMMA=42
    SEMICOLON=43
    COLON=44
    TRUE=45
    FALSE=46
    IF=47
    ELSEIF=48
    ELSE=49
    PUTS=50
    FN=51
    LETTER=52
    DIGIT=53
    CHARIN=54
    WS=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramASTContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramAST" ):
                listener.enterProgramAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramAST" ):
                listener.exitProgramAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramAST" ):
                return visitor.visitProgramAST(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = MonkeyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.ProgramASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.STRING) | (1 << MonkeyGrammarParser.BLOCK_OPEN) | (1 << MonkeyGrammarParser.BRACKET_OPEN) | (1 << MonkeyGrammarParser.PAR_OPEN) | (1 << MonkeyGrammarParser.LEN) | (1 << MonkeyGrammarParser.FIRST) | (1 << MonkeyGrammarParser.LAST) | (1 << MonkeyGrammarParser.REST) | (1 << MonkeyGrammarParser.PUSH) | (1 << MonkeyGrammarParser.LET) | (1 << MonkeyGrammarParser.RETURN) | (1 << MonkeyGrammarParser.TRUE) | (1 << MonkeyGrammarParser.FALSE) | (1 << MonkeyGrammarParser.IF) | (1 << MonkeyGrammarParser.PUTS) | (1 << MonkeyGrammarParser.FN) | (1 << MonkeyGrammarParser.LETTER) | (1 << MonkeyGrammarParser.DIGIT))) != 0):
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatementReturnASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MonkeyGrammarParser.RETURN, 0)
        def returnStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ReturnStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementReturnAST" ):
                listener.enterStatementReturnAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementReturnAST" ):
                listener.exitStatementReturnAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementReturnAST" ):
                return visitor.visitStatementReturnAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementLetASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(MonkeyGrammarParser.LET, 0)
        def letStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.LetStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementLetAST" ):
                listener.enterStatementLetAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementLetAST" ):
                listener.exitStatementLetAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementLetAST" ):
                return visitor.visitStatementLetAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementExpressionASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpressionAST" ):
                listener.enterStatementExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpressionAST" ):
                listener.exitStatementExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementExpressionAST" ):
                return visitor.visitStatementExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MonkeyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.LET]:
                localctx = MonkeyGrammarParser.StatementLetASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(MonkeyGrammarParser.LET)
                self.state = 69
                self.letStatement()
                pass
            elif token in [MonkeyGrammarParser.RETURN]:
                localctx = MonkeyGrammarParser.StatementReturnASTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(MonkeyGrammarParser.RETURN)
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.returnStatement()
                    pass

                elif la_ == 2:
                    pass


                pass
            elif token in [MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                localctx = MonkeyGrammarParser.StatementExpressionASTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.expressionStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_letStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LetStatementASTContext(LetStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.LetStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)

        def ASSIGN(self):
            return self.getToken(MonkeyGrammarParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatementAST" ):
                listener.enterLetStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatementAST" ):
                listener.exitLetStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStatementAST" ):
                return visitor.visitLetStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def letStatement(self):

        localctx = MonkeyGrammarParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letStatement)
        try:
            localctx = MonkeyGrammarParser.LetStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.identifier()
            self.state = 79
            self.match(MonkeyGrammarParser.ASSIGN)
            self.state = 80
            self.expression()
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.SEMICOLON]:
                self.state = 81
                self.match(MonkeyGrammarParser.SEMICOLON)
                pass
            elif token in [MonkeyGrammarParser.EOF, MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.BRACKET_CLOSE, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.LET, MonkeyGrammarParser.RETURN, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_returnStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReturnStatementASTContext(ReturnStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ReturnStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatementAST" ):
                listener.enterReturnStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatementAST" ):
                listener.exitReturnStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatementAST" ):
                return visitor.visitReturnStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def returnStatement(self):

        localctx = MonkeyGrammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_returnStatement)
        try:
            localctx = MonkeyGrammarParser.ReturnStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 85
                self.expression()
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MonkeyGrammarParser.SEMICOLON]:
                    self.state = 86
                    self.match(MonkeyGrammarParser.SEMICOLON)
                    pass
                elif token in [MonkeyGrammarParser.EOF, MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.BRACKET_CLOSE, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.LET, MonkeyGrammarParser.RETURN, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 90
                self.match(MonkeyGrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expressionStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionStatementASTContext(ExpressionStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ExpressionStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatementAST" ):
                listener.enterExpressionStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatementAST" ):
                listener.exitExpressionStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatementAST" ):
                return visitor.visitExpressionStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def expressionStatement(self):

        localctx = MonkeyGrammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionStatement)
        try:
            localctx = MonkeyGrammarParser.ExpressionStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.expression()
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.SEMICOLON]:
                self.state = 95
                self.match(MonkeyGrammarParser.SEMICOLON)
                pass
            elif token in [MonkeyGrammarParser.EOF, MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.BRACKET_CLOSE, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.LET, MonkeyGrammarParser.RETURN, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionASTContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.AdditionExpressionContext,0)

        def comparison(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAST" ):
                listener.enterExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAST" ):
                listener.exitExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAST" ):
                return visitor.visitExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = MonkeyGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            localctx = MonkeyGrammarParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.additionExpression()
            self.state = 100
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparisonASTContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.AdditionExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.AdditionExpressionContext,i)

        def LESS_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.LESS_THAN)
            else:
                return self.getToken(MonkeyGrammarParser.LESS_THAN, i)
        def GREATER_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.GREATER_THAN)
            else:
                return self.getToken(MonkeyGrammarParser.GREATER_THAN, i)
        def LESS_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.LESS_THAN_OR_EQUAL)
            else:
                return self.getToken(MonkeyGrammarParser.LESS_THAN_OR_EQUAL, i)
        def GREATER_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.GREATER_THAN_OR_EQUAL)
            else:
                return self.getToken(MonkeyGrammarParser.GREATER_THAN_OR_EQUAL, i)
        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.EQUAL)
            else:
                return self.getToken(MonkeyGrammarParser.EQUAL, i)
        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.NOT_EQUAL)
            else:
                return self.getToken(MonkeyGrammarParser.NOT_EQUAL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonAST" ):
                listener.enterComparisonAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonAST" ):
                listener.exitComparisonAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonAST" ):
                return visitor.visitComparisonAST(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self):

        localctx = MonkeyGrammarParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.EQUAL) | (1 << MonkeyGrammarParser.NOT_EQUAL) | (1 << MonkeyGrammarParser.LESS_THAN) | (1 << MonkeyGrammarParser.LESS_THAN_OR_EQUAL) | (1 << MonkeyGrammarParser.GREATER_THAN) | (1 << MonkeyGrammarParser.GREATER_THAN_OR_EQUAL))) != 0):
                self.state = 102
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.EQUAL) | (1 << MonkeyGrammarParser.NOT_EQUAL) | (1 << MonkeyGrammarParser.LESS_THAN) | (1 << MonkeyGrammarParser.LESS_THAN_OR_EQUAL) | (1 << MonkeyGrammarParser.GREATER_THAN) | (1 << MonkeyGrammarParser.GREATER_THAN_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103
                self.additionExpression()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_additionExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AdditionExpressionASTContext(AdditionExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.AdditionExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicationExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MultiplicationExpressionContext,0)

        def additionFactor(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.AdditionFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpressionAST" ):
                listener.enterAdditionExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpressionAST" ):
                listener.exitAdditionExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionExpressionAST" ):
                return visitor.visitAdditionExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def additionExpression(self):

        localctx = MonkeyGrammarParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionExpression)
        try:
            localctx = MonkeyGrammarParser.AdditionExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.multiplicationExpression()
            self.state = 110
            self.additionFactor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_additionFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AdditionFactorASTContext(AdditionFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.AdditionFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicationExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.MultiplicationExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.MultiplicationExpressionContext,i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.PLUS)
            else:
                return self.getToken(MonkeyGrammarParser.PLUS, i)
        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.MINUS)
            else:
                return self.getToken(MonkeyGrammarParser.MINUS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionFactorAST" ):
                listener.enterAdditionFactorAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionFactorAST" ):
                listener.exitAdditionFactorAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionFactorAST" ):
                return visitor.visitAdditionFactorAST(self)
            else:
                return visitor.visitChildren(self)



    def additionFactor(self):

        localctx = MonkeyGrammarParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.AdditionFactorASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.PLUS or _la==MonkeyGrammarParser.MINUS:
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==MonkeyGrammarParser.PLUS or _la==MonkeyGrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
                self.multiplicationExpression()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_multiplicationExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationExpressionASTContext(MultiplicationExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.MultiplicationExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ElementExpressionContext,0)

        def multiplicationFactor(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MultiplicationFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpressionAST" ):
                listener.enterMultiplicationExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpressionAST" ):
                listener.exitMultiplicationExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpressionAST" ):
                return visitor.visitMultiplicationExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationExpression(self):

        localctx = MonkeyGrammarParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplicationExpression)
        try:
            localctx = MonkeyGrammarParser.MultiplicationExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.elementExpression()
            self.state = 120
            self.multiplicationFactor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_multiplicationFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationFactorASTContext(MultiplicationFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.MultiplicationFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.ElementExpressionContext,i)

        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.MULTIPLY)
            else:
                return self.getToken(MonkeyGrammarParser.MULTIPLY, i)
        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.DIVIDE)
            else:
                return self.getToken(MonkeyGrammarParser.DIVIDE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationFactorAST" ):
                listener.enterMultiplicationFactorAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationFactorAST" ):
                listener.exitMultiplicationFactorAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationFactorAST" ):
                return visitor.visitMultiplicationFactorAST(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationFactor(self):

        localctx = MonkeyGrammarParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.MultiplicationFactorASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.MULTIPLY or _la==MonkeyGrammarParser.DIVIDE:
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==MonkeyGrammarParser.MULTIPLY or _la==MonkeyGrammarParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self.elementExpression()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_elementExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementExpressionASTContext(ElementExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ElementExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.PrimitiveExpressionContext,0)

        def elementAccess(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ElementAccessContext,0)

        def callExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.CallExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementExpressionAST" ):
                listener.enterElementExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementExpressionAST" ):
                listener.exitElementExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpressionAST" ):
                return visitor.visitElementExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def elementExpression(self):

        localctx = MonkeyGrammarParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementExpression)
        try:
            localctx = MonkeyGrammarParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.primitiveExpression()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 130
                self.elementAccess()
                pass

            elif la_ == 2:
                self.state = 131
                self.callExpression()
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_elementAccess

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementAccessASTContext(ElementAccessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ElementAccessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BLOCK_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_OPEN, 0)
        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def BLOCK_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAccessAST" ):
                listener.enterElementAccessAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAccessAST" ):
                listener.exitElementAccessAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccessAST" ):
                return visitor.visitElementAccessAST(self)
            else:
                return visitor.visitChildren(self)



    def elementAccess(self):

        localctx = MonkeyGrammarParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elementAccess)
        try:
            localctx = MonkeyGrammarParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MonkeyGrammarParser.BLOCK_OPEN)
            self.state = 136
            self.expression()
            self.state = 137
            self.match(MonkeyGrammarParser.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_callExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CallExpressionASTContext(CallExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.CallExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)
        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)
        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpressionAST" ):
                listener.enterCallExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpressionAST" ):
                listener.exitCallExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpressionAST" ):
                return visitor.visitCallExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def callExpression(self):

        localctx = MonkeyGrammarParser.CallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_callExpression)
        try:
            localctx = MonkeyGrammarParser.CallExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 140
                self.expressionList()
                pass

            elif la_ == 2:
                pass


            self.state = 144
            self.match(MonkeyGrammarParser.PAR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_primitiveExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimitiveExprArrFuncASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayFunctions(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ArrayFunctionsContext,0)

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)
        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)

        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprArrFuncAST" ):
                listener.enterPrimitiveExprArrFuncAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprArrFuncAST" ):
                listener.exitPrimitiveExprArrFuncAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprArrFuncAST" ):
                return visitor.visitPrimitiveExprArrFuncAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprPrintASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.PrintExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprPrintAST" ):
                listener.enterPrimitiveExprPrintAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprPrintAST" ):
                listener.exitPrimitiveExprPrintAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprPrintAST" ):
                return visitor.visitPrimitiveExprPrintAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprArrLitASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprArrLitAST" ):
                listener.enterPrimitiveExprArrLitAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprArrLitAST" ):
                listener.exitPrimitiveExprArrLitAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprArrLitAST" ):
                return visitor.visitPrimitiveExprArrLitAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprHashASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def hashLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.HashLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprHashAST" ):
                listener.enterPrimitiveExprHashAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprHashAST" ):
                listener.exitPrimitiveExprHashAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprHashAST" ):
                return visitor.visitPrimitiveExprHashAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprStringASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MonkeyGrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprStringAST" ):
                listener.enterPrimitiveExprStringAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprStringAST" ):
                listener.exitPrimitiveExprStringAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprStringAST" ):
                return visitor.visitPrimitiveExprStringAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprBooleanASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprBooleanAST" ):
                listener.enterPrimitiveExprBooleanAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprBooleanAST" ):
                listener.exitPrimitiveExprBooleanAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprBooleanAST" ):
                return visitor.visitPrimitiveExprBooleanAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprBlockExprASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)
        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprBlockExprAST" ):
                listener.enterPrimitiveExprBlockExprAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprBlockExprAST" ):
                listener.exitPrimitiveExprBlockExprAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprBlockExprAST" ):
                return visitor.visitPrimitiveExprBlockExprAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprFuncASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.FunctionLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprFuncAST" ):
                listener.enterPrimitiveExprFuncAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprFuncAST" ):
                listener.exitPrimitiveExprFuncAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprFuncAST" ):
                return visitor.visitPrimitiveExprFuncAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprDigitASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIGIT(self):
            return self.getToken(MonkeyGrammarParser.DIGIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprDigitAST" ):
                listener.enterPrimitiveExprDigitAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprDigitAST" ):
                listener.exitPrimitiveExprDigitAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprDigitAST" ):
                return visitor.visitPrimitiveExprDigitAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprIfASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IfExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprIfAST" ):
                listener.enterPrimitiveExprIfAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprIfAST" ):
                listener.exitPrimitiveExprIfAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprIfAST" ):
                return visitor.visitPrimitiveExprIfAST(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExprIdASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExprIdAST" ):
                listener.enterPrimitiveExprIdAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExprIdAST" ):
                listener.exitPrimitiveExprIdAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExprIdAST" ):
                return visitor.visitPrimitiveExprIdAST(self)
            else:
                return visitor.visitChildren(self)



    def primitiveExpression(self):

        localctx = MonkeyGrammarParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitiveExpression)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.DIGIT]:
                localctx = MonkeyGrammarParser.PrimitiveExprDigitASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MonkeyGrammarParser.DIGIT)
                pass
            elif token in [MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE]:
                localctx = MonkeyGrammarParser.PrimitiveExprBooleanASTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.boolean()
                pass
            elif token in [MonkeyGrammarParser.STRING]:
                localctx = MonkeyGrammarParser.PrimitiveExprStringASTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(MonkeyGrammarParser.STRING)
                pass
            elif token in [MonkeyGrammarParser.LETTER]:
                localctx = MonkeyGrammarParser.PrimitiveExprIdASTContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.identifier()
                pass
            elif token in [MonkeyGrammarParser.PAR_OPEN]:
                localctx = MonkeyGrammarParser.PrimitiveExprBlockExprASTContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.match(MonkeyGrammarParser.PAR_OPEN)
                self.state = 151
                self.expression()
                self.state = 152
                self.match(MonkeyGrammarParser.PAR_CLOSE)
                pass
            elif token in [MonkeyGrammarParser.BLOCK_OPEN]:
                localctx = MonkeyGrammarParser.PrimitiveExprArrLitASTContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 154
                self.arrayLiteral()
                pass
            elif token in [MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH]:
                localctx = MonkeyGrammarParser.PrimitiveExprArrFuncASTContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 155
                self.arrayFunctions()
                self.state = 156
                self.match(MonkeyGrammarParser.PAR_OPEN)
                self.state = 157
                self.expressionList()
                self.state = 158
                self.match(MonkeyGrammarParser.PAR_CLOSE)
                pass
            elif token in [MonkeyGrammarParser.FN]:
                localctx = MonkeyGrammarParser.PrimitiveExprFuncASTContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 160
                self.functionLiteral()
                pass
            elif token in [MonkeyGrammarParser.BRACKET_OPEN]:
                localctx = MonkeyGrammarParser.PrimitiveExprHashASTContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 161
                self.hashLiteral()
                pass
            elif token in [MonkeyGrammarParser.PUTS]:
                localctx = MonkeyGrammarParser.PrimitiveExprPrintASTContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 162
                self.printExpression()
                pass
            elif token in [MonkeyGrammarParser.IF]:
                localctx = MonkeyGrammarParser.PrimitiveExprIfASTContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 163
                self.ifExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayFunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEN(self):
            return self.getToken(MonkeyGrammarParser.LEN, 0)

        def FIRST(self):
            return self.getToken(MonkeyGrammarParser.FIRST, 0)

        def LAST(self):
            return self.getToken(MonkeyGrammarParser.LAST, 0)

        def REST(self):
            return self.getToken(MonkeyGrammarParser.REST, 0)

        def PUSH(self):
            return self.getToken(MonkeyGrammarParser.PUSH, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_arrayFunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayFunctions" ):
                listener.enterArrayFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayFunctions" ):
                listener.exitArrayFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayFunctions" ):
                return visitor.visitArrayFunctions(self)
            else:
                return visitor.visitChildren(self)




    def arrayFunctions(self):

        localctx = MonkeyGrammarParser.ArrayFunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayFunctions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.LEN) | (1 << MonkeyGrammarParser.FIRST) | (1 << MonkeyGrammarParser.LAST) | (1 << MonkeyGrammarParser.REST) | (1 << MonkeyGrammarParser.PUSH))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_arrayLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayLitetalASTContext(ArrayLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ArrayLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BLOCK_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_OPEN, 0)
        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)

        def BLOCK_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLitetalAST" ):
                listener.enterArrayLitetalAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLitetalAST" ):
                listener.exitArrayLitetalAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLitetalAST" ):
                return visitor.visitArrayLitetalAST(self)
            else:
                return visitor.visitChildren(self)



    def arrayLiteral(self):

        localctx = MonkeyGrammarParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayLiteral)
        try:
            localctx = MonkeyGrammarParser.ArrayLitetalASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MonkeyGrammarParser.BLOCK_OPEN)
            self.state = 169
            self.expressionList()
            self.state = 170
            self.match(MonkeyGrammarParser.BLOCK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.indice = None


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_functionLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.indice = ctx.indice



    class FunctionLiteralASTContext(FunctionLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.FunctionLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FN(self):
            return self.getToken(MonkeyGrammarParser.FN, 0)
        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)
        def functionParameters(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.FunctionParametersContext,0)

        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)
        def blockStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.BlockStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionLiteralAST" ):
                listener.enterFunctionLiteralAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionLiteralAST" ):
                listener.exitFunctionLiteralAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionLiteralAST" ):
                return visitor.visitFunctionLiteralAST(self)
            else:
                return visitor.visitChildren(self)



    def functionLiteral(self):

        localctx = MonkeyGrammarParser.FunctionLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionLiteral)
        try:
            localctx = MonkeyGrammarParser.FunctionLiteralASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MonkeyGrammarParser.FN)
            self.state = 173
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 174
            self.functionParameters()
            self.state = 175
            self.match(MonkeyGrammarParser.PAR_CLOSE)
            self.state = 176
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_functionParameters

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionParametersASTContext(FunctionParametersContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.FunctionParametersContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)

        def moreIdentifiers(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreIdentifiersContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParametersAST" ):
                listener.enterFunctionParametersAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParametersAST" ):
                listener.exitFunctionParametersAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParametersAST" ):
                return visitor.visitFunctionParametersAST(self)
            else:
                return visitor.visitChildren(self)



    def functionParameters(self):

        localctx = MonkeyGrammarParser.FunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionParameters)
        try:
            localctx = MonkeyGrammarParser.FunctionParametersASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.LETTER]:
                self.state = 178
                self.identifier()
                self.state = 179
                self.moreIdentifiers()
                pass
            elif token in [MonkeyGrammarParser.PAR_CLOSE]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreIdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreIdentifiers

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreIdentifiersASTContext(MoreIdentifiersContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.MoreIdentifiersContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.COMMA)
            else:
                return self.getToken(MonkeyGrammarParser.COMMA, i)
        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreIdentifiersAST" ):
                listener.enterMoreIdentifiersAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreIdentifiersAST" ):
                listener.exitMoreIdentifiersAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreIdentifiersAST" ):
                return visitor.visitMoreIdentifiersAST(self)
            else:
                return visitor.visitChildren(self)



    def moreIdentifiers(self):

        localctx = MonkeyGrammarParser.MoreIdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_moreIdentifiers)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.MoreIdentifiersASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 184
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 185
                self.identifier()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_hashLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HashLiteralASTContext(HashLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.HashLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRACKET_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_OPEN, 0)
        def hashContent(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.HashContentContext,0)

        def moreHashContent(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreHashContentContext,0)

        def BRACKET_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashLiteralAST" ):
                listener.enterHashLiteralAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashLiteralAST" ):
                listener.exitHashLiteralAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashLiteralAST" ):
                return visitor.visitHashLiteralAST(self)
            else:
                return visitor.visitChildren(self)



    def hashLiteral(self):

        localctx = MonkeyGrammarParser.HashLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_hashLiteral)
        try:
            localctx = MonkeyGrammarParser.HashLiteralASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MonkeyGrammarParser.BRACKET_OPEN)
            self.state = 192
            self.hashContent()
            self.state = 193
            self.moreHashContent()
            self.state = 194
            self.match(MonkeyGrammarParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_hashContent

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HashContentASTContext(HashContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.HashContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,i)

        def COLON(self):
            return self.getToken(MonkeyGrammarParser.COLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashContentAST" ):
                listener.enterHashContentAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashContentAST" ):
                listener.exitHashContentAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashContentAST" ):
                return visitor.visitHashContentAST(self)
            else:
                return visitor.visitChildren(self)



    def hashContent(self):

        localctx = MonkeyGrammarParser.HashContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_hashContent)
        try:
            localctx = MonkeyGrammarParser.HashContentASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.expression()
            self.state = 197
            self.match(MonkeyGrammarParser.COLON)
            self.state = 198
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreHashContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreHashContent

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreHashContentASTContext(MoreHashContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.MoreHashContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.COMMA)
            else:
                return self.getToken(MonkeyGrammarParser.COMMA, i)
        def hashContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.HashContentContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.HashContentContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreHashContentAST" ):
                listener.enterMoreHashContentAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreHashContentAST" ):
                listener.exitMoreHashContentAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreHashContentAST" ):
                return visitor.visitMoreHashContentAST(self)
            else:
                return visitor.visitChildren(self)



    def moreHashContent(self):

        localctx = MonkeyGrammarParser.MoreHashContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_moreHashContent)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.MoreHashContentASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 200
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 201
                self.hashContent()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expressionList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionListASTContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def moreExpressions(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreExpressionsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionListAST" ):
                listener.enterExpressionListAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionListAST" ):
                listener.exitExpressionListAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionListAST" ):
                return visitor.visitExpressionListAST(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionListEmptyASTContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionListEmptyAST" ):
                listener.enterExpressionListEmptyAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionListEmptyAST" ):
                listener.exitExpressionListEmptyAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionListEmptyAST" ):
                return visitor.visitExpressionListEmptyAST(self)
            else:
                return visitor.visitChildren(self)



    def expressionList(self):

        localctx = MonkeyGrammarParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressionList)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                localctx = MonkeyGrammarParser.ExpressionListASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.expression()
                self.state = 208
                self.moreExpressions()
                pass
            elif token in [MonkeyGrammarParser.BLOCK_CLOSE, MonkeyGrammarParser.PAR_CLOSE]:
                localctx = MonkeyGrammarParser.ExpressionListEmptyASTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreExpressions

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreExpressionsASTContext(MoreExpressionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.MoreExpressionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.COMMA)
            else:
                return self.getToken(MonkeyGrammarParser.COMMA, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreExpressionsAST" ):
                listener.enterMoreExpressionsAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreExpressionsAST" ):
                listener.exitMoreExpressionsAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreExpressionsAST" ):
                return visitor.visitMoreExpressionsAST(self)
            else:
                return visitor.visitChildren(self)



    def moreExpressions(self):

        localctx = MonkeyGrammarParser.MoreExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_moreExpressions)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.MoreExpressionsASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 213
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 214
                self.expression()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_printExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintExpressionASTContext(PrintExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.PrintExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTS(self):
            return self.getToken(MonkeyGrammarParser.PUTS, 0)
        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)
        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpressionAST" ):
                listener.enterPrintExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpressionAST" ):
                listener.exitPrintExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpressionAST" ):
                return visitor.visitPrintExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def printExpression(self):

        localctx = MonkeyGrammarParser.PrintExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_printExpression)
        try:
            localctx = MonkeyGrammarParser.PrintExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MonkeyGrammarParser.PUTS)
            self.state = 221
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 222
            self.expression()
            self.state = 223
            self.match(MonkeyGrammarParser.PAR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_ifExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfExpressionASTContext(IfExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.IfExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MonkeyGrammarParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.BlockStatementContext,i)

        def ELSE(self):
            return self.getToken(MonkeyGrammarParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpressionAST" ):
                listener.enterIfExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpressionAST" ):
                listener.exitIfExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpressionAST" ):
                return visitor.visitIfExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def ifExpression(self):

        localctx = MonkeyGrammarParser.IfExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifExpression)
        try:
            localctx = MonkeyGrammarParser.IfExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MonkeyGrammarParser.IF)
            self.state = 226
            self.expression()
            self.state = 227
            self.blockStatement()
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.ELSE]:
                self.state = 228
                self.match(MonkeyGrammarParser.ELSE)
                self.state = 229
                self.blockStatement()
                pass
            elif token in [MonkeyGrammarParser.EOF, MonkeyGrammarParser.STRING, MonkeyGrammarParser.EQUAL, MonkeyGrammarParser.NOT_EQUAL, MonkeyGrammarParser.LESS_THAN, MonkeyGrammarParser.LESS_THAN_OR_EQUAL, MonkeyGrammarParser.GREATER_THAN, MonkeyGrammarParser.GREATER_THAN_OR_EQUAL, MonkeyGrammarParser.PLUS, MonkeyGrammarParser.MINUS, MonkeyGrammarParser.MULTIPLY, MonkeyGrammarParser.DIVIDE, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BLOCK_CLOSE, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.BRACKET_CLOSE, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.PAR_CLOSE, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.LET, MonkeyGrammarParser.RETURN, MonkeyGrammarParser.COMMA, MonkeyGrammarParser.SEMICOLON, MonkeyGrammarParser.COLON, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_blockStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlockStatementASTContext(BlockStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.BlockStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRACKET_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_OPEN, 0)
        def BRACKET_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_CLOSE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatementAST" ):
                listener.enterBlockStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatementAST" ):
                listener.exitBlockStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatementAST" ):
                return visitor.visitBlockStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def blockStatement(self):

        localctx = MonkeyGrammarParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.BlockStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MonkeyGrammarParser.BRACKET_OPEN)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.STRING) | (1 << MonkeyGrammarParser.BLOCK_OPEN) | (1 << MonkeyGrammarParser.BRACKET_OPEN) | (1 << MonkeyGrammarParser.PAR_OPEN) | (1 << MonkeyGrammarParser.LEN) | (1 << MonkeyGrammarParser.FIRST) | (1 << MonkeyGrammarParser.LAST) | (1 << MonkeyGrammarParser.REST) | (1 << MonkeyGrammarParser.PUSH) | (1 << MonkeyGrammarParser.LET) | (1 << MonkeyGrammarParser.RETURN) | (1 << MonkeyGrammarParser.TRUE) | (1 << MonkeyGrammarParser.FALSE) | (1 << MonkeyGrammarParser.IF) | (1 << MonkeyGrammarParser.PUTS) | (1 << MonkeyGrammarParser.FN) | (1 << MonkeyGrammarParser.LETTER) | (1 << MonkeyGrammarParser.DIGIT))) != 0):
                self.state = 234
                self.statement()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(MonkeyGrammarParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_identifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentifierASTContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.LETTER)
            else:
                return self.getToken(MonkeyGrammarParser.LETTER, i)
        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.DIGIT)
            else:
                return self.getToken(MonkeyGrammarParser.DIGIT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierAST" ):
                listener.enterIdentifierAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierAST" ):
                listener.exitIdentifierAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierAST" ):
                return visitor.visitIdentifierAST(self)
            else:
                return visitor.visitChildren(self)



    def identifier(self):

        localctx = MonkeyGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            localctx = MonkeyGrammarParser.IdentifierASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MonkeyGrammarParser.LETTER)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 243
                    _la = self._input.LA(1)
                    if not(_la==MonkeyGrammarParser.LETTER or _la==MonkeyGrammarParser.DIGIT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MonkeyGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MonkeyGrammarParser.FALSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = MonkeyGrammarParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==MonkeyGrammarParser.TRUE or _la==MonkeyGrammarParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_char

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CharASTContext(CharContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MonkeyGrammarParser.CharContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.QUOTE)
            else:
                return self.getToken(MonkeyGrammarParser.QUOTE, i)
        def CHARIN(self):
            return self.getToken(MonkeyGrammarParser.CHARIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharAST" ):
                listener.enterCharAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharAST" ):
                listener.exitCharAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharAST" ):
                return visitor.visitCharAST(self)
            else:
                return visitor.visitChildren(self)



    def char(self):

        localctx = MonkeyGrammarParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_char)
        try:
            localctx = MonkeyGrammarParser.CharASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MonkeyGrammarParser.QUOTE)
            self.state = 252
            self.match(MonkeyGrammarParser.CHARIN)
            self.state = 253
            self.match(MonkeyGrammarParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





