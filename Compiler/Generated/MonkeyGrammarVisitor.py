# Generated from C:/Users/garroakion/Desktop/Projects2Semestre/Compiladores/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MonkeyGrammarParser.

class MonkeyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MonkeyGrammarParser#programAST.
    def visitProgramAST(self, ctx:MonkeyGrammarParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#statementLetAST.
    def visitStatementLetAST(self, ctx:MonkeyGrammarParser.StatementLetASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#statementReturnAST.
    def visitStatementReturnAST(self, ctx:MonkeyGrammarParser.StatementReturnASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#statementExpressionAST.
    def visitStatementExpressionAST(self, ctx:MonkeyGrammarParser.StatementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#letStatementAST.
    def visitLetStatementAST(self, ctx:MonkeyGrammarParser.LetStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#returnStatementAST.
    def visitReturnStatementAST(self, ctx:MonkeyGrammarParser.ReturnStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionStatementAST.
    def visitExpressionStatementAST(self, ctx:MonkeyGrammarParser.ExpressionStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionAST.
    def visitExpressionAST(self, ctx:MonkeyGrammarParser.ExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#comparisonAST.
    def visitComparisonAST(self, ctx:MonkeyGrammarParser.ComparisonASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#additionExpressionAST.
    def visitAdditionExpressionAST(self, ctx:MonkeyGrammarParser.AdditionExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#additionFactorAST.
    def visitAdditionFactorAST(self, ctx:MonkeyGrammarParser.AdditionFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:MonkeyGrammarParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#multiplicationFactorAST.
    def visitMultiplicationFactorAST(self, ctx:MonkeyGrammarParser.MultiplicationFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:MonkeyGrammarParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:MonkeyGrammarParser.ElementAccessASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#callExpressionAST.
    def visitCallExpressionAST(self, ctx:MonkeyGrammarParser.CallExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprDigitAST.
    def visitPrimitiveExprDigitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprStringAST.
    def visitPrimitiveExprStringAST(self, ctx:MonkeyGrammarParser.PrimitiveExprStringASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprIdAST.
    def visitPrimitiveExprIdAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIdASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprTrueAST.
    def visitPrimitiveExprTrueAST(self, ctx:MonkeyGrammarParser.PrimitiveExprTrueASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprFalseAST.
    def visitPrimitiveExprFalseAST(self, ctx:MonkeyGrammarParser.PrimitiveExprFalseASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprBlockExprAST.
    def visitPrimitiveExprBlockExprAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprArrLitAST.
    def visitPrimitiveExprArrLitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprArrFuncAST.
    def visitPrimitiveExprArrFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprFuncAST.
    def visitPrimitiveExprFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprHashAST.
    def visitPrimitiveExprHashAST(self, ctx:MonkeyGrammarParser.PrimitiveExprHashASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprPrintAST.
    def visitPrimitiveExprPrintAST(self, ctx:MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExprIfAST.
    def visitPrimitiveExprIfAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIfASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def visitArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#arrayLitetalAS.
    def visitArrayLitetalAS(self, ctx:MonkeyGrammarParser.ArrayLitetalASContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#functionLiteralAST.
    def visitFunctionLiteralAST(self, ctx:MonkeyGrammarParser.FunctionLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#functionParametersAST.
    def visitFunctionParametersAST(self, ctx:MonkeyGrammarParser.FunctionParametersASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreIdentifiersAST.
    def visitMoreIdentifiersAST(self, ctx:MonkeyGrammarParser.MoreIdentifiersASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#hashLiteralAST.
    def visitHashLiteralAST(self, ctx:MonkeyGrammarParser.HashLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#hashContentAST.
    def visitHashContentAST(self, ctx:MonkeyGrammarParser.HashContentASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreHashContentAST.
    def visitMoreHashContentAST(self, ctx:MonkeyGrammarParser.MoreHashContentASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionListAST.
    def visitExpressionListAST(self, ctx:MonkeyGrammarParser.ExpressionListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionListEmptyAST.
    def visitExpressionListEmptyAST(self, ctx:MonkeyGrammarParser.ExpressionListEmptyASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreExpressionsAST.
    def visitMoreExpressionsAST(self, ctx:MonkeyGrammarParser.MoreExpressionsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#printExpressionAST.
    def visitPrintExpressionAST(self, ctx:MonkeyGrammarParser.PrintExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#ifExpressionAST.
    def visitIfExpressionAST(self, ctx:MonkeyGrammarParser.IfExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#blockStatementAST.
    def visitBlockStatementAST(self, ctx:MonkeyGrammarParser.BlockStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#identifierAST.
    def visitIdentifierAST(self, ctx:MonkeyGrammarParser.IdentifierASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#charAST.
    def visitCharAST(self, ctx:MonkeyGrammarParser.CharASTContext):
        return self.visitChildren(ctx)



del MonkeyGrammarParser