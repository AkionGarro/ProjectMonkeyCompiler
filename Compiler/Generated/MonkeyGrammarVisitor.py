# Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MonkeyGrammarParser.

class MonkeyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MonkeyGrammarParser#startRule.
    def visitStartRule(self, ctx:MonkeyGrammarParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#identifier.
    def visitIdentifier(self, ctx:MonkeyGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#char.
    def visitChar(self, ctx:MonkeyGrammarParser.CharContext):
        return self.visitChildren(ctx)



del MonkeyGrammarParser