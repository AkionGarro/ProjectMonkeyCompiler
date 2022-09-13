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


    # Visit a parse tree produced by MonkeyGrammarParser#statement.
    def visitStatement(self, ctx:MonkeyGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#letStatement.
    def visitLetStatement(self, ctx:MonkeyGrammarParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#returnStatement.
    def visitReturnStatement(self, ctx:MonkeyGrammarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MonkeyGrammarParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expression.
    def visitExpression(self, ctx:MonkeyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#comparison.
    def visitComparison(self, ctx:MonkeyGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#additionExpression.
    def visitAdditionExpression(self, ctx:MonkeyGrammarParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#additionFactor.
    def visitAdditionFactor(self, ctx:MonkeyGrammarParser.AdditionFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:MonkeyGrammarParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#multiplicationFactor.
    def visitMultiplicationFactor(self, ctx:MonkeyGrammarParser.MultiplicationFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#elementExpression.
    def visitElementExpression(self, ctx:MonkeyGrammarParser.ElementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#elementAccess.
    def visitElementAccess(self, ctx:MonkeyGrammarParser.ElementAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#callExpression.
    def visitCallExpression(self, ctx:MonkeyGrammarParser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#primitiveExpression.
    def visitPrimitiveExpression(self, ctx:MonkeyGrammarParser.PrimitiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def visitArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MonkeyGrammarParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#functionLiteral.
    def visitFunctionLiteral(self, ctx:MonkeyGrammarParser.FunctionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#functionParameters.
    def visitFunctionParameters(self, ctx:MonkeyGrammarParser.FunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreIdentifiers.
    def visitMoreIdentifiers(self, ctx:MonkeyGrammarParser.MoreIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#hashLiteral.
    def visitHashLiteral(self, ctx:MonkeyGrammarParser.HashLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#hashContent.
    def visitHashContent(self, ctx:MonkeyGrammarParser.HashContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreHashContent.
    def visitMoreHashContent(self, ctx:MonkeyGrammarParser.MoreHashContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#expressionList.
    def visitExpressionList(self, ctx:MonkeyGrammarParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#moreExpressions.
    def visitMoreExpressions(self, ctx:MonkeyGrammarParser.MoreExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#printExpression.
    def visitPrintExpression(self, ctx:MonkeyGrammarParser.PrintExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#ifExpression.
    def visitIfExpression(self, ctx:MonkeyGrammarParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#blockStatement.
    def visitBlockStatement(self, ctx:MonkeyGrammarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#identifier.
    def visitIdentifier(self, ctx:MonkeyGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyGrammarParser#char.
    def visitChar(self, ctx:MonkeyGrammarParser.CharContext):
        return self.visitChildren(ctx)



del MonkeyGrammarParser