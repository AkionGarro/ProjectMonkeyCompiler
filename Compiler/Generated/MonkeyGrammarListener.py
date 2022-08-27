# Generated from C:/Users/garroakion/Desktop/Projects2Semestre/Compiladores/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete listener for a parse tree produced by MonkeyGrammarParser.
class MonkeyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MonkeyGrammarParser#program.
    def enterProgram(self, ctx:MonkeyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#program.
    def exitProgram(self, ctx:MonkeyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expr.
    def enterExpr(self, ctx:MonkeyGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expr.
    def exitExpr(self, ctx:MonkeyGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#var_decl.
    def enterVar_decl(self, ctx:MonkeyGrammarParser.Var_declContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#var_decl.
    def exitVar_decl(self, ctx:MonkeyGrammarParser.Var_declContext):
        pass



del MonkeyGrammarParser