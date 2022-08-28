# Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
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
        4,1,40,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,5,1,11,8,1,10,
        1,12,1,14,9,1,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,14,15,17,0,
        6,1,0,0,0,2,8,1,0,0,0,4,15,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,12,
        5,14,0,0,9,11,7,0,0,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,
        13,1,0,0,0,13,3,1,0,0,0,14,12,1,0,0,0,15,16,5,17,0,0,16,17,5,16,
        0,0,17,18,5,17,0,0,18,5,1,0,0,0,1,12
    ]

class MonkeyGrammarParser ( Parser ):

    grammarFileName = "MonkeyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'return'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'['", "']'", "'{'", "'}'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'\"'", 
                     "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", 
                     "'/*'", "'*/'", "<INVALID>", "'len'", "'first'", "'last'", 
                     "'rest'", "'push'", "<INVALID>", "<INVALID>", "','", 
                     "';'", "'true'", "'false'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "LET", "RETURN", "GreaterT", "LowerT", 
                      "GreaterEQ", "LowerEQ", "Equeals", "BLOCK_OPEN", "BLOCK_CLOSE", 
                      "BRACKET_OPEN", "BRACKET_CLOSE", "PAR_OPEN", "PAR_CLOSE", 
                      "LETTER", "DIGIT", "CHARIN", "QUOTE", "NotEqueals", 
                      "Sum", "Res", "Mul", "Div", "Mod", "DivEnt", "Open", 
                      "Close", "Comment", "Len", "First", "Last", "Rest", 
                      "Push", "Boolean", "WS", "COMMA", "SEMICOLON", "TRUE", 
                      "FALSE", "IF", "ELSE" ]

    RULE_startRule = 0
    RULE_identifier = 1
    RULE_char = 2

    ruleNames =  [ "startRule", "identifier", "char" ]

    EOF = Token.EOF
    LET=1
    RETURN=2
    GreaterT=3
    LowerT=4
    GreaterEQ=5
    LowerEQ=6
    Equeals=7
    BLOCK_OPEN=8
    BLOCK_CLOSE=9
    BRACKET_OPEN=10
    BRACKET_CLOSE=11
    PAR_OPEN=12
    PAR_CLOSE=13
    LETTER=14
    DIGIT=15
    CHARIN=16
    QUOTE=17
    NotEqueals=18
    Sum=19
    Res=20
    Mul=21
    Div=22
    Mod=23
    DivEnt=24
    Open=25
    Close=26
    Comment=27
    Len=28
    First=29
    Last=30
    Rest=31
    Push=32
    Boolean=33
    WS=34
    COMMA=35
    SEMICOLON=36
    TRUE=37
    FALSE=38
    IF=39
    ELSE=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MonkeyGrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MonkeyGrammarParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRule" ):
                return visitor.visitStartRule(self)
            else:
                return visitor.visitChildren(self)




    def startRule(self):

        localctx = MonkeyGrammarParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.identifier()
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
        self.enterRule(localctx, 2, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(MonkeyGrammarParser.LETTER)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MonkeyGrammarParser.LETTER or _la==MonkeyGrammarParser.DIGIT:
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==MonkeyGrammarParser.LETTER or _la==MonkeyGrammarParser.DIGIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 4, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(MonkeyGrammarParser.QUOTE)
            self.state = 16
            self.match(MonkeyGrammarParser.CHARIN)
            self.state = 17
            self.match(MonkeyGrammarParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





