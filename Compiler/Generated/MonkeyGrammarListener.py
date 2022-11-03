# Generated from C:/Users/bryam/Desktop/compi/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyGrammarParser import MonkeyGrammarParser
else:
    from MonkeyGrammarParser import MonkeyGrammarParser

# This class defines a complete listener for a parse tree produced by MonkeyGrammarParser.
class MonkeyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MonkeyGrammarParser#programAST.
    def enterProgramAST(self, ctx:MonkeyGrammarParser.ProgramASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#programAST.
    def exitProgramAST(self, ctx:MonkeyGrammarParser.ProgramASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#statementLetAST.
    def enterStatementLetAST(self, ctx:MonkeyGrammarParser.StatementLetASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#statementLetAST.
    def exitStatementLetAST(self, ctx:MonkeyGrammarParser.StatementLetASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#statementReturnAST.
    def enterStatementReturnAST(self, ctx:MonkeyGrammarParser.StatementReturnASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#statementReturnAST.
    def exitStatementReturnAST(self, ctx:MonkeyGrammarParser.StatementReturnASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#statementExpressionAST.
    def enterStatementExpressionAST(self, ctx:MonkeyGrammarParser.StatementExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#statementExpressionAST.
    def exitStatementExpressionAST(self, ctx:MonkeyGrammarParser.StatementExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#letStatementAST.
    def enterLetStatementAST(self, ctx:MonkeyGrammarParser.LetStatementASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#letStatementAST.
    def exitLetStatementAST(self, ctx:MonkeyGrammarParser.LetStatementASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#returnStatementAST.
    def enterReturnStatementAST(self, ctx:MonkeyGrammarParser.ReturnStatementASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#returnStatementAST.
    def exitReturnStatementAST(self, ctx:MonkeyGrammarParser.ReturnStatementASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionStatementAST.
    def enterExpressionStatementAST(self, ctx:MonkeyGrammarParser.ExpressionStatementASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionStatementAST.
    def exitExpressionStatementAST(self, ctx:MonkeyGrammarParser.ExpressionStatementASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionAST.
    def enterExpressionAST(self, ctx:MonkeyGrammarParser.ExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionAST.
    def exitExpressionAST(self, ctx:MonkeyGrammarParser.ExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#comparisonAST.
    def enterComparisonAST(self, ctx:MonkeyGrammarParser.ComparisonASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#comparisonAST.
    def exitComparisonAST(self, ctx:MonkeyGrammarParser.ComparisonASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#additionExpressionAST.
    def enterAdditionExpressionAST(self, ctx:MonkeyGrammarParser.AdditionExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#additionExpressionAST.
    def exitAdditionExpressionAST(self, ctx:MonkeyGrammarParser.AdditionExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#additionFactorAST.
    def enterAdditionFactorAST(self, ctx:MonkeyGrammarParser.AdditionFactorASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#additionFactorAST.
    def exitAdditionFactorAST(self, ctx:MonkeyGrammarParser.AdditionFactorASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#multiplicationExpressionAST.
    def enterMultiplicationExpressionAST(self, ctx:MonkeyGrammarParser.MultiplicationExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#multiplicationExpressionAST.
    def exitMultiplicationExpressionAST(self, ctx:MonkeyGrammarParser.MultiplicationExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#multiplicationFactorAST.
    def enterMultiplicationFactorAST(self, ctx:MonkeyGrammarParser.MultiplicationFactorASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#multiplicationFactorAST.
    def exitMultiplicationFactorAST(self, ctx:MonkeyGrammarParser.MultiplicationFactorASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#elementExpressionAST.
    def enterElementExpressionAST(self, ctx:MonkeyGrammarParser.ElementExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#elementExpressionAST.
    def exitElementExpressionAST(self, ctx:MonkeyGrammarParser.ElementExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#elementAccessAST.
    def enterElementAccessAST(self, ctx:MonkeyGrammarParser.ElementAccessASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#elementAccessAST.
    def exitElementAccessAST(self, ctx:MonkeyGrammarParser.ElementAccessASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#callExpressionAST.
    def enterCallExpressionAST(self, ctx:MonkeyGrammarParser.CallExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#callExpressionAST.
    def exitCallExpressionAST(self, ctx:MonkeyGrammarParser.CallExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprDigitAST.
    def enterPrimitiveExprDigitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprDigitAST.
    def exitPrimitiveExprDigitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprDigitPointAST.
    def enterPrimitiveExprDigitPointAST(self, ctx:MonkeyGrammarParser.PrimitiveExprDigitPointASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprDigitPointAST.
    def exitPrimitiveExprDigitPointAST(self, ctx:MonkeyGrammarParser.PrimitiveExprDigitPointASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprBooleanAST.
    def enterPrimitiveExprBooleanAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBooleanASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprBooleanAST.
    def exitPrimitiveExprBooleanAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBooleanASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprStringAST.
    def enterPrimitiveExprStringAST(self, ctx:MonkeyGrammarParser.PrimitiveExprStringASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprStringAST.
    def exitPrimitiveExprStringAST(self, ctx:MonkeyGrammarParser.PrimitiveExprStringASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprIdAST.
    def enterPrimitiveExprIdAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIdASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprIdAST.
    def exitPrimitiveExprIdAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIdASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprBlockExprAST.
    def enterPrimitiveExprBlockExprAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprBlockExprAST.
    def exitPrimitiveExprBlockExprAST(self, ctx:MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprArrLitAST.
    def enterPrimitiveExprArrLitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprArrLitAST.
    def exitPrimitiveExprArrLitAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprArrFuncAST.
    def enterPrimitiveExprArrFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprArrFuncAST.
    def exitPrimitiveExprArrFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprFuncAST.
    def enterPrimitiveExprFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprFuncAST.
    def exitPrimitiveExprFuncAST(self, ctx:MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprHashAST.
    def enterPrimitiveExprHashAST(self, ctx:MonkeyGrammarParser.PrimitiveExprHashASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprHashAST.
    def exitPrimitiveExprHashAST(self, ctx:MonkeyGrammarParser.PrimitiveExprHashASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprPrintAST.
    def enterPrimitiveExprPrintAST(self, ctx:MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprPrintAST.
    def exitPrimitiveExprPrintAST(self, ctx:MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#primitiveExprIfAST.
    def enterPrimitiveExprIfAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIfASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#primitiveExprIfAST.
    def exitPrimitiveExprIfAST(self, ctx:MonkeyGrammarParser.PrimitiveExprIfASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def enterArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#arrayFunctions.
    def exitArrayFunctions(self, ctx:MonkeyGrammarParser.ArrayFunctionsContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#arrayLitetalAST.
    def enterArrayLitetalAST(self, ctx:MonkeyGrammarParser.ArrayLitetalASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#arrayLitetalAST.
    def exitArrayLitetalAST(self, ctx:MonkeyGrammarParser.ArrayLitetalASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#functionLiteralAST.
    def enterFunctionLiteralAST(self, ctx:MonkeyGrammarParser.FunctionLiteralASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#functionLiteralAST.
    def exitFunctionLiteralAST(self, ctx:MonkeyGrammarParser.FunctionLiteralASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#functionParametersAST.
    def enterFunctionParametersAST(self, ctx:MonkeyGrammarParser.FunctionParametersASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#functionParametersAST.
    def exitFunctionParametersAST(self, ctx:MonkeyGrammarParser.FunctionParametersASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreIdentifiersAST.
    def enterMoreIdentifiersAST(self, ctx:MonkeyGrammarParser.MoreIdentifiersASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreIdentifiersAST.
    def exitMoreIdentifiersAST(self, ctx:MonkeyGrammarParser.MoreIdentifiersASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#hashLiteralAST.
    def enterHashLiteralAST(self, ctx:MonkeyGrammarParser.HashLiteralASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#hashLiteralAST.
    def exitHashLiteralAST(self, ctx:MonkeyGrammarParser.HashLiteralASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#hashContentAST.
    def enterHashContentAST(self, ctx:MonkeyGrammarParser.HashContentASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#hashContentAST.
    def exitHashContentAST(self, ctx:MonkeyGrammarParser.HashContentASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreHashContentAST.
    def enterMoreHashContentAST(self, ctx:MonkeyGrammarParser.MoreHashContentASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreHashContentAST.
    def exitMoreHashContentAST(self, ctx:MonkeyGrammarParser.MoreHashContentASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionListAST.
    def enterExpressionListAST(self, ctx:MonkeyGrammarParser.ExpressionListASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionListAST.
    def exitExpressionListAST(self, ctx:MonkeyGrammarParser.ExpressionListASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#expressionListEmptyAST.
    def enterExpressionListEmptyAST(self, ctx:MonkeyGrammarParser.ExpressionListEmptyASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#expressionListEmptyAST.
    def exitExpressionListEmptyAST(self, ctx:MonkeyGrammarParser.ExpressionListEmptyASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#moreExpressionsAST.
    def enterMoreExpressionsAST(self, ctx:MonkeyGrammarParser.MoreExpressionsASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#moreExpressionsAST.
    def exitMoreExpressionsAST(self, ctx:MonkeyGrammarParser.MoreExpressionsASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#printExpressionAST.
    def enterPrintExpressionAST(self, ctx:MonkeyGrammarParser.PrintExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#printExpressionAST.
    def exitPrintExpressionAST(self, ctx:MonkeyGrammarParser.PrintExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#ifExpressionAST.
    def enterIfExpressionAST(self, ctx:MonkeyGrammarParser.IfExpressionASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#ifExpressionAST.
    def exitIfExpressionAST(self, ctx:MonkeyGrammarParser.IfExpressionASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#blockStatementAST.
    def enterBlockStatementAST(self, ctx:MonkeyGrammarParser.BlockStatementASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#blockStatementAST.
    def exitBlockStatementAST(self, ctx:MonkeyGrammarParser.BlockStatementASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#identifierAST.
    def enterIdentifierAST(self, ctx:MonkeyGrammarParser.IdentifierASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#identifierAST.
    def exitIdentifierAST(self, ctx:MonkeyGrammarParser.IdentifierASTContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#boolean.
    def enterBoolean(self, ctx:MonkeyGrammarParser.BooleanContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#boolean.
    def exitBoolean(self, ctx:MonkeyGrammarParser.BooleanContext):
        pass


    # Enter a parse tree produced by MonkeyGrammarParser#charAST.
    def enterCharAST(self, ctx:MonkeyGrammarParser.CharASTContext):
        pass

    # Exit a parse tree produced by MonkeyGrammarParser#charAST.
    def exitCharAST(self, ctx:MonkeyGrammarParser.CharASTContext):
        pass



del MonkeyGrammarParser