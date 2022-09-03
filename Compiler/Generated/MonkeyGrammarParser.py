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
        4,1,54,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,5,1,11,8,1,10,
        1,12,1,14,9,1,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,4,5,17,0,6,
        1,0,0,0,2,8,1,0,0,0,4,15,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,12,5,
        4,0,0,9,11,7,0,0,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,
        1,0,0,0,13,3,1,0,0,0,14,12,1,0,0,0,15,16,5,40,0,0,16,17,5,39,0,0,
        17,18,5,40,0,0,18,5,1,0,0,0,1,12
    ]

class MonkeyGrammarParser ( Parser ):

    grammarFileName = "MonkeyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'//'", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'//='", "'['", "']'", "'{'", "'}'", "'('", "')'", 
                     "'.'", "'let'", "'return'", "<INVALID>", "'\"'", "'len'", 
                     "'first'", "'last'", "'rest'", "'push'", "','", "';'", 
                     "'true'", "'false'", "'if'", "'elseif'", "'else'", 
                     "'puts'", "'fn'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "COMMENT", "WS", "LETTER", 
                      "DIGIT", "Boolean", "STRING", "EQUAL", "NOT_EQUAL", 
                      "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                      "GREATER_THAN_OR_EQUAL", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "DIVIDE_INT", "AND", "OR", "NOT", 
                      "ASSIGN", "ASSIGN_PLUS", "ASSIGN_MINUS", "ASSIGN_MULTIPLY", 
                      "ASSIGN_DIVIDE", "ASSIGN_MODULO", "ASSIGN_DIVIDE_INT", 
                      "BLOCK_OPEN", "BLOCK_CLOSE", "BRACKET_OPEN", "BRACKET_CLOSE", 
                      "PAR_OPEN", "PAR_CLOSE", "DOT", "LET", "RETURN", "CHARIN", 
                      "QUOTE", "Len", "First", "Last", "Rest", "Push", "COMMA", 
                      "SEMICOLON", "TRUE", "FALSE", "IF", "ELSEIF", "ELSE", 
                      "PUTS", "FN" ]

    RULE_startRule = 0
    RULE_identifier = 1
    RULE_char = 2

    ruleNames =  [ "startRule", "identifier", "char" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    COMMENT=2
    WS=3
    LETTER=4
    DIGIT=5
    Boolean=6
    STRING=7
    EQUAL=8
    NOT_EQUAL=9
    LESS_THAN=10
    LESS_THAN_OR_EQUAL=11
    GREATER_THAN=12
    GREATER_THAN_OR_EQUAL=13
    PLUS=14
    MINUS=15
    MULTIPLY=16
    DIVIDE=17
    MODULO=18
    DIVIDE_INT=19
    AND=20
    OR=21
    NOT=22
    ASSIGN=23
    ASSIGN_PLUS=24
    ASSIGN_MINUS=25
    ASSIGN_MULTIPLY=26
    ASSIGN_DIVIDE=27
    ASSIGN_MODULO=28
    ASSIGN_DIVIDE_INT=29
    BLOCK_OPEN=30
    BLOCK_CLOSE=31
    BRACKET_OPEN=32
    BRACKET_CLOSE=33
    PAR_OPEN=34
    PAR_CLOSE=35
    DOT=36
    LET=37
    RETURN=38
    CHARIN=39
    QUOTE=40
    Len=41
    First=42
    Last=43
    Rest=44
    Push=45
    COMMA=46
    SEMICOLON=47
    TRUE=48
    FALSE=49
    IF=50
    ELSEIF=51
    ELSE=52
    PUTS=53
    FN=54

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





