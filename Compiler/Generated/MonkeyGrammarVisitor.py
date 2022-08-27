# Generated from C:/Users/garroakion/Desktop/Projects2Semestre/Compiladores/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MonkeyGrammarParser.

class MonkeyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MonkeyGrammarParser#program.
    def visitProgram(self, ctx:MonkeyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expr.
    def visitExpr(self, ctx:MonkeyGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#var_decl.
    def visitVar_decl(self, ctx:MonkeyGrammarParser.Var_declContext):
        return self.visitChildren(ctx)



del MonkeyGrammarParser