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
        4,1,25,24,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,
        0,21,0,6,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,7,5,1,0,0,7,8,5,23,
        0,0,8,12,5,18,0,0,9,11,3,2,1,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,
        1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,19,0,0,
        16,1,1,0,0,0,17,18,3,4,2,0,18,3,1,0,0,0,19,20,5,2,0,0,20,21,5,23,
        0,0,21,22,5,22,0,0,22,5,1,0,0,0,1,12
    ]

class MonkeyGrammarParser ( Parser ):

    grammarFileName = "MonkeyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "'println'", "'+'", 
                     "'-'", "'*'", "'/'", "'&&'", "'||'", "'!'", "'='", 
                     "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "'{'", 
                     "'}'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "VAR", "PRINTLN", "PLUS", 
                      "MINUS", "MULT", "DIV", "AND", "OR", "NOT", "ASSIGN", 
                      "GT", "LT", "GEQ", "LEQ", "EQ", "NEQ", "BRACKET_OPEN", 
                      "BRACKET_CLOSE", "PAR_OPEN", "PAR_CLOSE", "SEMICOLON", 
                      "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_var_decl = 2

    ruleNames =  [ "program", "expr", "var_decl" ]

    EOF = Token.EOF
    PROGRAM=1
    VAR=2
    PRINTLN=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    AND=8
    OR=9
    NOT=10
    ASSIGN=11
    GT=12
    LT=13
    GEQ=14
    LEQ=15
    EQ=16
    NEQ=17
    BRACKET_OPEN=18
    BRACKET_CLOSE=19
    PAR_OPEN=20
    PAR_CLOSE=21
    SEMICOLON=22
    ID=23
    NUMBER=24
    WS=25

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

        def PROGRAM(self):
            return self.getToken(MonkeyGrammarParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(MonkeyGrammarParser.ID, 0)

        def BRACKET_OPEN(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_OPEN, 0)

        def BRACKET_CLOSE(self):
            return self.getToken(MonkeyGrammarParser.BRACKET_CLOSE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MonkeyGrammarParser.ExprContext,i)


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
            self.state = 6
            self.match(MonkeyGrammarParser.PROGRAM)
            self.state = 7
            self.match(MonkeyGrammarParser.ID)
            self.state = 8
            self.match(MonkeyGrammarParser.BRACKET_OPEN)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.VAR:
                self.state = 9
                self.expr()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(MonkeyGrammarParser.BRACKET_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.Var_declContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MonkeyGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MonkeyGrammarParser.VAR, 0)

        def ID(self):
            return self.getToken(MonkeyGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MonkeyGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MonkeyGrammarParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(MonkeyGrammarParser.VAR)
            self.state = 20
            self.match(MonkeyGrammarParser.ID)
            self.state = 21
            self.match(MonkeyGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





