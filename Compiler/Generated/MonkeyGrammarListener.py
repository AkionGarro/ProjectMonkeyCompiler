# Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
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


    # Enter a parse tree produced by MonkeyGrammarParser#statement.
    def enterStatement(self, ctx:MonkeyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#statement.
    def exitStatement(self, ctx:MonkeyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#letStatement.
    def enterLetStatement(self, ctx:MonkeyGrammarParser.LetStatementContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#letStatement.
    def exitLetStatement(self, ctx:MonkeyGrammarParser.LetStatementContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#returnStatement.
    def enterReturnStatement(self, ctx:MonkeyGrammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#returnStatement.
    def exitReturnStatement(self, ctx:MonkeyGrammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MonkeyGrammarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MonkeyGrammarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expression.
    def enterExpression(self, ctx:MonkeyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expression.
    def exitExpression(self, ctx:MonkeyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#comparison.
    def enterComparison(self, ctx:MonkeyGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#comparison.
    def exitComparison(self, ctx:MonkeyGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#additionExpression.
    def enterAdditionExpression(self, ctx:MonkeyGrammarParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#additionExpression.
    def exitAdditionExpression(self, ctx:MonkeyGrammarParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#additionFactor.
    def enterAdditionFactor(self, ctx:MonkeyGrammarParser.AdditionFactorContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#additionFactor.
    def exitAdditionFactor(self, ctx:MonkeyGrammarParser.AdditionFactorContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:MonkeyGrammarParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:MonkeyGrammarParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#multiplicationFactor.
    def enterMultiplicationFactor(self, ctx:MonkeyGrammarParser.MultiplicationFactorContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#multiplicationFactor.
    def exitMultiplicationFactor(self, ctx:MonkeyGrammarParser.MultiplicationFactorContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#elementExpression.
    def enterElementExpression(self, ctx:MonkeyGrammarParser.ElementExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#elementExpression.
    def exitElementExpression(self, ctx:MonkeyGrammarParser.ElementExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#elementAccess.
    def enterElementAccess(self, ctx:MonkeyGrammarParser.ElementAccessContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#elementAccess.
    def exitElementAccess(self, ctx:MonkeyGrammarParser.ElementAccessContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#callExpression.
    def enterCallExpression(self, ctx:MonkeyGrammarParser.CallExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#callExpression.
    def exitCallExpression(self, ctx:MonkeyGrammarParser.CallExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExpression.
    def enterPrimitiveExpression(self, ctx:MonkeyGrammarParser.PrimitiveExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExpression.
    def exitPrimitiveExpression(self, ctx:MonkeyGrammarParser.PrimitiveExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def enterArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def exitArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:MonkeyGrammarParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:MonkeyGrammarParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#functionLiteral.
    def enterFunctionLiteral(self, ctx:MonkeyGrammarParser.FunctionLiteralContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#functionLiteral.
    def exitFunctionLiteral(self, ctx:MonkeyGrammarParser.FunctionLiteralContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#functionParameters.
    def enterFunctionParameters(self, ctx:MonkeyGrammarParser.FunctionParametersContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#functionParameters.
    def exitFunctionParameters(self, ctx:MonkeyGrammarParser.FunctionParametersContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreIdentifiers.
    def enterMoreIdentifiers(self, ctx:MonkeyGrammarParser.MoreIdentifiersContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreIdentifiers.
    def exitMoreIdentifiers(self, ctx:MonkeyGrammarParser.MoreIdentifiersContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#hashLiteral.
    def enterHashLiteral(self, ctx:MonkeyGrammarParser.HashLiteralContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#hashLiteral.
    def exitHashLiteral(self, ctx:MonkeyGrammarParser.HashLiteralContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#hashContent.
    def enterHashContent(self, ctx:MonkeyGrammarParser.HashContentContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#hashContent.
    def exitHashContent(self, ctx:MonkeyGrammarParser.HashContentContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreHashContent.
    def enterMoreHashContent(self, ctx:MonkeyGrammarParser.MoreHashContentContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreHashContent.
    def exitMoreHashContent(self, ctx:MonkeyGrammarParser.MoreHashContentContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionList.
    def enterExpressionList(self, ctx:MonkeyGrammarParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionList.
    def exitExpressionList(self, ctx:MonkeyGrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreExpressions.
    def enterMoreExpressions(self, ctx:MonkeyGrammarParser.MoreExpressionsContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreExpressions.
    def exitMoreExpressions(self, ctx:MonkeyGrammarParser.MoreExpressionsContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#printExpression.
    def enterPrintExpression(self, ctx:MonkeyGrammarParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#printExpression.
    def exitPrintExpression(self, ctx:MonkeyGrammarParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#ifExpression.
    def enterIfExpression(self, ctx:MonkeyGrammarParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#ifExpression.
    def exitIfExpression(self, ctx:MonkeyGrammarParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#blockStatement.
    def enterBlockStatement(self, ctx:MonkeyGrammarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#blockStatement.
    def exitBlockStatement(self, ctx:MonkeyGrammarParser.BlockStatementContext):
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