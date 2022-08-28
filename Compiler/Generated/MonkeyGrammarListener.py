# Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete listener for a parse tree produced by MonkeyGrammarParser.
class MonkeyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MonkeyGrammarParser#startRule.
    def enterStartRule(self, ctx:MonkeyGrammarParser.StartRuleContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#startRule.
    def exitStartRule(self, ctx:MonkeyGrammarParser.StartRuleContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#identifier.
    def enterIdentifier(self, ctx:MonkeyGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#identifier.
    def exitIdentifier(self, ctx:MonkeyGrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#char.
    def enterChar(self, ctx:MonkeyGrammarParser.CharContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#char.
    def exitChar(self, ctx:MonkeyGrammarParser.CharContext):
        pass



del MonkeyGrammarParser