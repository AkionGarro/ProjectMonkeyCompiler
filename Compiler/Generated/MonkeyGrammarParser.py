# Generated from C:/Users/garroakion/Desktop/Projects2Semestre/Compiladores/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
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
        4,1,56,240,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        1,1,1,1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,3,2,79,8,2,1,3,
        1,3,1,3,3,3,84,8,3,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,6,1,6,5,
        6,96,8,6,10,6,12,6,99,9,6,1,7,1,7,1,7,1,8,1,8,5,8,106,8,8,10,8,12,
        8,109,9,8,1,9,1,9,1,9,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,
        10,1,11,1,11,1,11,1,11,3,11,125,8,11,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,154,8,14,1,15,1,
        15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,19,1,19,5,19,173,8,19,10,19,12,19,176,9,19,1,20,1,20,1,20,1,
        20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,5,22,189,8,22,10,22,12,22,
        192,9,22,1,23,1,23,1,23,1,23,3,23,198,8,23,1,24,1,24,5,24,202,8,
        24,10,24,12,24,205,9,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,26,3,26,218,8,26,1,27,1,27,5,27,222,8,27,10,27,12,27,
        225,9,27,1,27,1,27,1,28,1,28,5,28,231,8,28,10,28,12,28,234,9,28,
        1,29,1,29,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,5,1,0,6,11,
        1,0,12,13,1,0,14,15,1,0,34,38,1,0,53,54,238,0,63,1,0,0,0,2,71,1,
        0,0,0,4,73,1,0,0,0,6,80,1,0,0,0,8,85,1,0,0,0,10,90,1,0,0,0,12,97,
        1,0,0,0,14,100,1,0,0,0,16,107,1,0,0,0,18,110,1,0,0,0,20,117,1,0,
        0,0,22,120,1,0,0,0,24,126,1,0,0,0,26,130,1,0,0,0,28,153,1,0,0,0,
        30,155,1,0,0,0,32,157,1,0,0,0,34,161,1,0,0,0,36,167,1,0,0,0,38,174,
        1,0,0,0,40,177,1,0,0,0,42,182,1,0,0,0,44,190,1,0,0,0,46,197,1,0,
        0,0,48,203,1,0,0,0,50,206,1,0,0,0,52,211,1,0,0,0,54,219,1,0,0,0,
        56,228,1,0,0,0,58,235,1,0,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,1,1,0,0,0,65,63,1,0,0,0,66,
        67,5,39,0,0,67,72,3,4,2,0,68,69,5,40,0,0,69,72,3,6,3,0,70,72,3,8,
        4,0,71,66,1,0,0,0,71,68,1,0,0,0,71,70,1,0,0,0,72,3,1,0,0,0,73,74,
        3,56,28,0,74,75,5,21,0,0,75,78,3,10,5,0,76,79,5,44,0,0,77,79,1,0,
        0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,5,1,0,0,0,80,83,3,10,5,0,81,84,
        5,44,0,0,82,84,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,7,1,0,0,0,
        85,88,3,10,5,0,86,89,5,44,0,0,87,89,1,0,0,0,88,86,1,0,0,0,88,87,
        1,0,0,0,89,9,1,0,0,0,90,91,3,14,7,0,91,92,3,12,6,0,92,11,1,0,0,0,
        93,94,7,0,0,0,94,96,3,14,7,0,95,93,1,0,0,0,96,99,1,0,0,0,97,95,1,
        0,0,0,97,98,1,0,0,0,98,13,1,0,0,0,99,97,1,0,0,0,100,101,3,18,9,0,
        101,102,3,16,8,0,102,15,1,0,0,0,103,104,7,1,0,0,104,106,3,18,9,0,
        105,103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,
        108,17,1,0,0,0,109,107,1,0,0,0,110,111,3,22,11,0,111,112,3,20,10,
        0,112,19,1,0,0,0,113,114,7,2,0,0,114,116,3,22,11,0,115,113,1,0,0,
        0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,21,1,0,0,0,
        119,117,1,0,0,0,120,124,3,28,14,0,121,125,3,24,12,0,122,125,3,26,
        13,0,123,125,1,0,0,0,124,121,1,0,0,0,124,122,1,0,0,0,124,123,1,0,
        0,0,125,23,1,0,0,0,126,127,5,28,0,0,127,128,3,10,5,0,128,129,5,29,
        0,0,129,25,1,0,0,0,130,131,5,32,0,0,131,132,3,46,23,0,132,133,5,
        33,0,0,133,27,1,0,0,0,134,154,5,54,0,0,135,154,5,4,0,0,136,154,3,
        56,28,0,137,154,5,46,0,0,138,154,5,47,0,0,139,140,5,32,0,0,140,141,
        3,10,5,0,141,142,5,33,0,0,142,154,1,0,0,0,143,154,3,32,16,0,144,
        145,3,30,15,0,145,146,5,32,0,0,146,147,3,46,23,0,147,148,5,33,0,
        0,148,154,1,0,0,0,149,154,3,34,17,0,150,154,3,40,20,0,151,154,3,
        50,25,0,152,154,3,52,26,0,153,134,1,0,0,0,153,135,1,0,0,0,153,136,
        1,0,0,0,153,137,1,0,0,0,153,138,1,0,0,0,153,139,1,0,0,0,153,143,
        1,0,0,0,153,144,1,0,0,0,153,149,1,0,0,0,153,150,1,0,0,0,153,151,
        1,0,0,0,153,152,1,0,0,0,154,29,1,0,0,0,155,156,7,3,0,0,156,31,1,
        0,0,0,157,158,5,28,0,0,158,159,3,46,23,0,159,160,5,29,0,0,160,33,
        1,0,0,0,161,162,5,52,0,0,162,163,5,32,0,0,163,164,3,36,18,0,164,
        165,5,33,0,0,165,166,3,54,27,0,166,35,1,0,0,0,167,168,3,56,28,0,
        168,169,3,38,19,0,169,37,1,0,0,0,170,171,5,43,0,0,171,173,3,56,28,
        0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,
        0,175,39,1,0,0,0,176,174,1,0,0,0,177,178,5,30,0,0,178,179,3,42,21,
        0,179,180,3,44,22,0,180,181,5,31,0,0,181,41,1,0,0,0,182,183,3,10,
        5,0,183,184,5,45,0,0,184,185,3,10,5,0,185,43,1,0,0,0,186,187,5,43,
        0,0,187,189,3,42,21,0,188,186,1,0,0,0,189,192,1,0,0,0,190,188,1,
        0,0,0,190,191,1,0,0,0,191,45,1,0,0,0,192,190,1,0,0,0,193,194,3,10,
        5,0,194,195,3,48,24,0,195,198,1,0,0,0,196,198,1,0,0,0,197,193,1,
        0,0,0,197,196,1,0,0,0,198,47,1,0,0,0,199,200,5,43,0,0,200,202,3,
        10,5,0,201,199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,
        0,0,0,204,49,1,0,0,0,205,203,1,0,0,0,206,207,5,51,0,0,207,208,5,
        32,0,0,208,209,3,10,5,0,209,210,5,33,0,0,210,51,1,0,0,0,211,212,
        5,48,0,0,212,213,3,10,5,0,213,217,3,54,27,0,214,215,5,50,0,0,215,
        218,3,54,27,0,216,218,1,0,0,0,217,214,1,0,0,0,217,216,1,0,0,0,218,
        53,1,0,0,0,219,223,5,30,0,0,220,222,3,2,1,0,221,220,1,0,0,0,222,
        225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,
        223,1,0,0,0,226,227,5,31,0,0,227,55,1,0,0,0,228,232,5,53,0,0,229,
        231,7,4,0,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,
        233,1,0,0,0,233,57,1,0,0,0,234,232,1,0,0,0,235,236,5,42,0,0,236,
        237,5,55,0,0,237,238,5,42,0,0,238,59,1,0,0,0,17,63,71,78,83,88,97,
        107,117,124,153,174,190,197,203,217,223,232
    ]

class MonkeyGrammarParser ( Parser ):

    grammarFileName = "MonkeyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'integer'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", 
                     "'&&'", "'||'", "'!'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'//='", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "'len'", "'first'", "'last'", "'rest'", 
                     "'push'", "'let'", "'return'", "'.'", "'\"'", "','", 
                     "';'", "':'", "'true'", "'false'", "'if'", "'elseif'", 
                     "'else'", "'puts'", "'fn'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "COMMENT", "Boolean", 
                      "STRING", "INTEGER", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "DIVIDE_INT", 
                      "AND", "OR", "NOT", "ASSIGN", "ASSIGN_PLUS", "ASSIGN_MINUS", 
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
    RULE_char = 29

    ruleNames =  [ "program", "statement", "letStatement", "returnStatement", 
                   "expressionStatement", "expression", "comparison", "additionExpression", 
                   "additionFactor", "multiplicationExpression", "multiplicationFactor", 
                   "elementExpression", "elementAccess", "callExpression", 
                   "primitiveExpression", "arrayFunctions", "arrayLiteral", 
                   "functionLiteral", "functionParameters", "moreIdentifiers", 
                   "hashLiteral", "hashContent", "moreHashContent", "expressionList", 
                   "moreExpressions", "printExpression", "ifExpression", 
                   "blockStatement", "identifier", "char" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    COMMENT=2
    Boolean=3
    STRING=4
    INTEGER=5
    EQUAL=6
    NOT_EQUAL=7
    LESS_THAN=8
    LESS_THAN_OR_EQUAL=9
    GREATER_THAN=10
    GREATER_THAN_OR_EQUAL=11
    PLUS=12
    MINUS=13
    MULTIPLY=14
    DIVIDE=15
    MODULO=16
    DIVIDE_INT=17
    AND=18
    OR=19
    NOT=20
    ASSIGN=21
    ASSIGN_PLUS=22
    ASSIGN_MINUS=23
    ASSIGN_MULTIPLY=24
    ASSIGN_DIVIDE=25
    ASSIGN_MODULO=26
    ASSIGN_DIVIDE_INT=27
    BLOCK_OPEN=28
    BLOCK_CLOSE=29
    BRACKET_OPEN=30
    BRACKET_CLOSE=31
    PAR_OPEN=32
    PAR_CLOSE=33
    LEN=34
    FIRST=35
    LAST=36
    REST=37
    PUSH=38
    LET=39
    RETURN=40
    DOT=41
    QUOTE=42
    COMMA=43
    SEMICOLON=44
    COLON=45
    TRUE=46
    FALSE=47
    IF=48
    ELSEIF=49
    ELSE=50
    PUTS=51
    FN=52
    LETTER=53
    DIGIT=54
    CHARIN=55
    WS=56

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MonkeyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.STRING) | (1 << MonkeyGrammarParser.BLOCK_OPEN) | (1 << MonkeyGrammarParser.BRACKET_OPEN) | (1 << MonkeyGrammarParser.PAR_OPEN) | (1 << MonkeyGrammarParser.LEN) | (1 << MonkeyGrammarParser.FIRST) | (1 << MonkeyGrammarParser.LAST) | (1 << MonkeyGrammarParser.REST) | (1 << MonkeyGrammarParser.PUSH) | (1 << MonkeyGrammarParser.LET) | (1 << MonkeyGrammarParser.RETURN) | (1 << MonkeyGrammarParser.TRUE) | (1 << MonkeyGrammarParser.FALSE) | (1 << MonkeyGrammarParser.IF) | (1 << MonkeyGrammarParser.PUTS) | (1 << MonkeyGrammarParser.FN) | (1 << MonkeyGrammarParser.LETTER) | (1 << MonkeyGrammarParser.DIGIT))) != 0):
                self.state = 60
                self.statement()
                self.state = 65
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

        def LET(self):
            return self.getToken(MonkeyGrammarParser.LET, 0)

        def letStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.LetStatementContext,0)


        def RETURN(self):
            return self.getToken(MonkeyGrammarParser.RETURN, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ReturnStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MonkeyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(MonkeyGrammarParser.LET)
                self.state = 67
                self.letStatement()
                pass
            elif token in [MonkeyGrammarParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(MonkeyGrammarParser.RETURN)
                self.state = 69
                self.returnStatement()
                pass
            elif token in [MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
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

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(MonkeyGrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_letStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatement" ):
                listener.enterLetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatement" ):
                listener.exitLetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStatement" ):
                return visitor.visitLetStatement(self)
            else:
                return visitor.visitChildren(self)




    def letStatement(self):

        localctx = MonkeyGrammarParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.identifier()
            self.state = 74
            self.match(MonkeyGrammarParser.ASSIGN)
            self.state = 75
            self.expression()
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.SEMICOLON]:
                self.state = 76
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

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MonkeyGrammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
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


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MonkeyGrammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
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

        def additionExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.AdditionExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ComparisonContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MonkeyGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.additionExpression()
            self.state = 91
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

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = MonkeyGrammarParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.EQUAL) | (1 << MonkeyGrammarParser.NOT_EQUAL) | (1 << MonkeyGrammarParser.LESS_THAN) | (1 << MonkeyGrammarParser.LESS_THAN_OR_EQUAL) | (1 << MonkeyGrammarParser.GREATER_THAN) | (1 << MonkeyGrammarParser.GREATER_THAN_OR_EQUAL))) != 0):
                self.state = 93
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.EQUAL) | (1 << MonkeyGrammarParser.NOT_EQUAL) | (1 << MonkeyGrammarParser.LESS_THAN) | (1 << MonkeyGrammarParser.LESS_THAN_OR_EQUAL) | (1 << MonkeyGrammarParser.GREATER_THAN) | (1 << MonkeyGrammarParser.GREATER_THAN_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 94
                self.additionExpression()
                self.state = 99
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

        def multiplicationExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MultiplicationExpressionContext,0)


        def additionFactor(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.AdditionFactorContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_additionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpression" ):
                listener.enterAdditionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpression" ):
                listener.exitAdditionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionExpression" ):
                return visitor.visitAdditionExpression(self)
            else:
                return visitor.visitChildren(self)




    def additionExpression(self):

        localctx = MonkeyGrammarParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.multiplicationExpression()
            self.state = 101
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

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_additionFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionFactor" ):
                listener.enterAdditionFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionFactor" ):
                listener.exitAdditionFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionFactor" ):
                return visitor.visitAdditionFactor(self)
            else:
                return visitor.visitChildren(self)




    def additionFactor(self):

        localctx = MonkeyGrammarParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.PLUS or _la==MonkeyGrammarParser.MINUS:
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==MonkeyGrammarParser.PLUS or _la==MonkeyGrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
                self.multiplicationExpression()
                self.state = 109
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

        def elementExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ElementExpressionContext,0)


        def multiplicationFactor(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MultiplicationFactorContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_multiplicationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpression" ):
                listener.enterMultiplicationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpression" ):
                listener.exitMultiplicationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpression" ):
                return visitor.visitMultiplicationExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicationExpression(self):

        localctx = MonkeyGrammarParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplicationExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.elementExpression()
            self.state = 111
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

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_multiplicationFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationFactor" ):
                listener.enterMultiplicationFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationFactor" ):
                listener.exitMultiplicationFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationFactor" ):
                return visitor.visitMultiplicationFactor(self)
            else:
                return visitor.visitChildren(self)




    def multiplicationFactor(self):

        localctx = MonkeyGrammarParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.MULTIPLY or _la==MonkeyGrammarParser.DIVIDE:
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==MonkeyGrammarParser.MULTIPLY or _la==MonkeyGrammarParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.elementExpression()
                self.state = 119
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

        def primitiveExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.PrimitiveExpressionContext,0)


        def elementAccess(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ElementAccessContext,0)


        def callExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.CallExpressionContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_elementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementExpression" ):
                listener.enterElementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementExpression" ):
                listener.exitElementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpression" ):
                return visitor.visitElementExpression(self)
            else:
                return visitor.visitChildren(self)




    def elementExpression(self):

        localctx = MonkeyGrammarParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.primitiveExpression()
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 121
                self.elementAccess()
                pass

            elif la_ == 2:
                self.state = 122
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

        def BLOCK_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def BLOCK_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_CLOSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_elementAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAccess" ):
                listener.enterElementAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAccess" ):
                listener.exitElementAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccess" ):
                return visitor.visitElementAccess(self)
            else:
                return visitor.visitChildren(self)




    def elementAccess(self):

        localctx = MonkeyGrammarParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elementAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(MonkeyGrammarParser.BLOCK_OPEN)
            self.state = 127
            self.expression()
            self.state = 128
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

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)


        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_callExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpression" ):
                listener.enterCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpression" ):
                listener.exitCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpression" ):
                return visitor.visitCallExpression(self)
            else:
                return visitor.visitChildren(self)




    def callExpression(self):

        localctx = MonkeyGrammarParser.CallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_callExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 131
            self.expressionList()
            self.state = 132
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

        def DIGIT(self):
            return self.getToken(MonkeyGrammarParser.DIGIT, 0)

        def STRING(self):
            return self.getToken(MonkeyGrammarParser.STRING, 0)

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)


        def TRUE(self):
            return self.getToken(MonkeyGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MonkeyGrammarParser.FALSE, 0)

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ArrayLiteralContext,0)


        def arrayFunctions(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ArrayFunctionsContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)


        def functionLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.FunctionLiteralContext,0)


        def hashLiteral(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.HashLiteralContext,0)


        def printExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.PrintExpressionContext,0)


        def ifExpression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IfExpressionContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_primitiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpression" ):
                listener.enterPrimitiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpression" ):
                listener.exitPrimitiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpression" ):
                return visitor.visitPrimitiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def primitiveExpression(self):

        localctx = MonkeyGrammarParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitiveExpression)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(MonkeyGrammarParser.DIGIT)
                pass
            elif token in [MonkeyGrammarParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(MonkeyGrammarParser.STRING)
                pass
            elif token in [MonkeyGrammarParser.LETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.identifier()
                pass
            elif token in [MonkeyGrammarParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.match(MonkeyGrammarParser.TRUE)
                pass
            elif token in [MonkeyGrammarParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.match(MonkeyGrammarParser.FALSE)
                pass
            elif token in [MonkeyGrammarParser.PAR_OPEN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 139
                self.match(MonkeyGrammarParser.PAR_OPEN)
                self.state = 140
                self.expression()
                self.state = 141
                self.match(MonkeyGrammarParser.PAR_CLOSE)
                pass
            elif token in [MonkeyGrammarParser.BLOCK_OPEN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.arrayLiteral()
                pass
            elif token in [MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH]:
                self.enterOuterAlt(localctx, 8)
                self.state = 144
                self.arrayFunctions()
                self.state = 145
                self.match(MonkeyGrammarParser.PAR_OPEN)
                self.state = 146
                self.expressionList()
                self.state = 147
                self.match(MonkeyGrammarParser.PAR_CLOSE)
                pass
            elif token in [MonkeyGrammarParser.FN]:
                self.enterOuterAlt(localctx, 9)
                self.state = 149
                self.functionLiteral()
                pass
            elif token in [MonkeyGrammarParser.BRACKET_OPEN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
                self.hashLiteral()
                pass
            elif token in [MonkeyGrammarParser.PUTS]:
                self.enterOuterAlt(localctx, 11)
                self.state = 151
                self.printExpression()
                pass
            elif token in [MonkeyGrammarParser.IF]:
                self.enterOuterAlt(localctx, 12)
                self.state = 152
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
            self.state = 155
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

        def BLOCK_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_OPEN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionListContext,0)


        def BLOCK_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BLOCK_CLOSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = MonkeyGrammarParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MonkeyGrammarParser.BLOCK_OPEN)
            self.state = 158
            self.expressionList()
            self.state = 159
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


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_functionLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionLiteral" ):
                listener.enterFunctionLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionLiteral" ):
                listener.exitFunctionLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionLiteral" ):
                return visitor.visitFunctionLiteral(self)
            else:
                return visitor.visitChildren(self)




    def functionLiteral(self):

        localctx = MonkeyGrammarParser.FunctionLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MonkeyGrammarParser.FN)
            self.state = 162
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 163
            self.functionParameters()
            self.state = 164
            self.match(MonkeyGrammarParser.PAR_CLOSE)
            self.state = 165
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

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)


        def moreIdentifiers(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreIdentifiersContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_functionParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameters" ):
                listener.enterFunctionParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameters" ):
                listener.exitFunctionParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParameters" ):
                return visitor.visitFunctionParameters(self)
            else:
                return visitor.visitChildren(self)




    def functionParameters(self):

        localctx = MonkeyGrammarParser.FunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.identifier()
            self.state = 168
            self.moreIdentifiers()
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


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreIdentifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreIdentifiers" ):
                listener.enterMoreIdentifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreIdentifiers" ):
                listener.exitMoreIdentifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreIdentifiers" ):
                return visitor.visitMoreIdentifiers(self)
            else:
                return visitor.visitChildren(self)




    def moreIdentifiers(self):

        localctx = MonkeyGrammarParser.MoreIdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_moreIdentifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 170
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 171
                self.identifier()
                self.state = 176
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

        def BRACKET_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_OPEN, 0)

        def hashContent(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.HashContentContext,0)


        def moreHashContent(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreHashContentContext,0)


        def BRACKET_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_CLOSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_hashLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashLiteral" ):
                listener.enterHashLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashLiteral" ):
                listener.exitHashLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashLiteral" ):
                return visitor.visitHashLiteral(self)
            else:
                return visitor.visitChildren(self)




    def hashLiteral(self):

        localctx = MonkeyGrammarParser.HashLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_hashLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MonkeyGrammarParser.BRACKET_OPEN)
            self.state = 178
            self.hashContent()
            self.state = 179
            self.moreHashContent()
            self.state = 180
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,i)


        def COLON(self):
            return self.getToken(MonkeyGrammarParser.COLON, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_hashContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashContent" ):
                listener.enterHashContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashContent" ):
                listener.exitHashContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashContent" ):
                return visitor.visitHashContent(self)
            else:
                return visitor.visitChildren(self)




    def hashContent(self):

        localctx = MonkeyGrammarParser.HashContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_hashContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expression()
            self.state = 183
            self.match(MonkeyGrammarParser.COLON)
            self.state = 184
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


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreHashContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreHashContent" ):
                listener.enterMoreHashContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreHashContent" ):
                listener.exitMoreHashContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreHashContent" ):
                return visitor.visitMoreHashContent(self)
            else:
                return visitor.visitChildren(self)




    def moreHashContent(self):

        localctx = MonkeyGrammarParser.MoreHashContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_moreHashContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 186
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 187
                self.hashContent()
                self.state = 192
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

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def moreExpressions(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.MoreExpressionsContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MonkeyGrammarParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressionList)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.STRING, MonkeyGrammarParser.BLOCK_OPEN, MonkeyGrammarParser.BRACKET_OPEN, MonkeyGrammarParser.PAR_OPEN, MonkeyGrammarParser.LEN, MonkeyGrammarParser.FIRST, MonkeyGrammarParser.LAST, MonkeyGrammarParser.REST, MonkeyGrammarParser.PUSH, MonkeyGrammarParser.TRUE, MonkeyGrammarParser.FALSE, MonkeyGrammarParser.IF, MonkeyGrammarParser.PUTS, MonkeyGrammarParser.FN, MonkeyGrammarParser.LETTER, MonkeyGrammarParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.expression()
                self.state = 194
                self.moreExpressions()
                pass
            elif token in [MonkeyGrammarParser.BLOCK_CLOSE, MonkeyGrammarParser.PAR_CLOSE]:
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


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_moreExpressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreExpressions" ):
                listener.enterMoreExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreExpressions" ):
                listener.exitMoreExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreExpressions" ):
                return visitor.visitMoreExpressions(self)
            else:
                return visitor.visitChildren(self)




    def moreExpressions(self):

        localctx = MonkeyGrammarParser.MoreExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_moreExpressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.COMMA:
                self.state = 199
                self.match(MonkeyGrammarParser.COMMA)
                self.state = 200
                self.expression()
                self.state = 205
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

        def PUTS(self):
            return self.getToken(MonkeyGrammarParser.PUTS, 0)

        def PAR_OPEN(self):
            return self.getToken(MonkeyGrammarParser.PAR_OPEN, 0)

        def expression(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.ExpressionContext,0)


        def PAR_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.PAR_CLOSE, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_printExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpression" ):
                listener.enterPrintExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpression" ):
                listener.exitPrintExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpression" ):
                return visitor.visitPrintExpression(self)
            else:
                return visitor.visitChildren(self)




    def printExpression(self):

        localctx = MonkeyGrammarParser.PrintExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_printExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MonkeyGrammarParser.PUTS)
            self.state = 207
            self.match(MonkeyGrammarParser.PAR_OPEN)
            self.state = 208
            self.expression()
            self.state = 209
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

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_ifExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpression" ):
                listener.enterIfExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpression" ):
                listener.exitIfExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpression" ):
                return visitor.visitIfExpression(self)
            else:
                return visitor.visitChildren(self)




    def ifExpression(self):

        localctx = MonkeyGrammarParser.IfExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MonkeyGrammarParser.IF)
            self.state = 212
            self.expression()
            self.state = 213
            self.blockStatement()
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MonkeyGrammarParser.ELSE]:
                self.state = 214
                self.match(MonkeyGrammarParser.ELSE)
                self.state = 215
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

        def BRACKET_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_OPEN, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_CLOSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = MonkeyGrammarParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MonkeyGrammarParser.BRACKET_OPEN)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MonkeyGrammarParser.STRING) | (1 << MonkeyGrammarParser.BLOCK_OPEN) | (1 << MonkeyGrammarParser.BRACKET_OPEN) | (1 << MonkeyGrammarParser.PAR_OPEN) | (1 << MonkeyGrammarParser.LEN) | (1 << MonkeyGrammarParser.FIRST) | (1 << MonkeyGrammarParser.LAST) | (1 << MonkeyGrammarParser.REST) | (1 << MonkeyGrammarParser.PUSH) | (1 << MonkeyGrammarParser.LET) | (1 << MonkeyGrammarParser.RETURN) | (1 << MonkeyGrammarParser.TRUE) | (1 << MonkeyGrammarParser.FALSE) | (1 << MonkeyGrammarParser.IF) | (1 << MonkeyGrammarParser.PUTS) | (1 << MonkeyGrammarParser.FN) | (1 << MonkeyGrammarParser.LETTER) | (1 << MonkeyGrammarParser.DIGIT))) != 0):
                self.state = 220
                self.statement()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
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

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MonkeyGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MonkeyGrammarParser.LETTER)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    _la = self._input.LA(1)
                    if not(_la==MonkeyGrammarParser.LETTER or _la==MonkeyGrammarParser.DIGIT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyGrammarParser.QUOTE)
            else:
                return self.getToken(MonkeyGrammarParser.QUOTE, i)

        def CHARIN(self):
            return self.getToken(MonkeyGrammarParser.CHARIN, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)




    def char(self):

        localctx = MonkeyGrammarParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MonkeyGrammarParser.QUOTE)
            self.state = 236
            self.match(MonkeyGrammarParser.CHARIN)
            self.state = 237
            self.match(MonkeyGrammarParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





