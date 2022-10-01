from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor


class MyVisitor(MonkeyGrammarVisitor):


    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext):
        print("In visit program")
        return self.visitChildren(ctx)

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext):
        print("Visit Let Statament")
        return self.visitChildren(ctx)

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext):
        print("Return Statament")
        return self.visitChildren(ctx)

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext):
        print("Statament Expresion")
        return self.visitChildren(ctx)

    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext):
        print("LetStatament")
        return self.visitChildren(ctx)

    def visitReturnStatementAST(self, ctx: MonkeyGrammarParser.ReturnStatementASTContext):
        print("Return Statament")
        return self.visitChildren(ctx)

    def visitExpressionStatementAST(self, ctx: MonkeyGrammarParser.ExpressionStatementASTContext):
        print("Expresion Statament")
        return self.visitChildren(ctx)

    def visitExpressionAST(self, ctx: MonkeyGrammarParser.ExpressionASTContext):
        print("Expresion ")
        return self.visitChildren(ctx)

    def visitComparisonAST(self, ctx: MonkeyGrammarParser.ComparisonASTContext):
        print("Comparison")
        return self.visitChildren(ctx)

    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext):
        print("Addition Expr")
        return self.visitChildren(ctx)

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext):
        print("Addition Factor")
        return self.visitChildren(ctx)

    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext):
        print("Mult Expr")
        return self.visitChildren(ctx)

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext):
        print("Mult Factor")
        return self.visitChildren(ctx)

    def visitElementExpressionAST(self, ctx: MonkeyGrammarParser.ElementExpressionASTContext):
        print("Element Expr")
        return self.visitChildren(ctx)

    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext):
        print("Element Access")
        return self.visitChildren(ctx)

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext):
        print("Call Expr")
        return self.visitChildren(ctx)

    def visitPrimitiveExprDigitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        print("Primitive Expr")
        return self.visitChildren(ctx)

    def visitPrimitiveExprStringAST(self, ctx: MonkeyGrammarParser.PrimitiveExprStringASTContext):
        print("Primitive String")
        return self.visitChildren(ctx)

    def visitPrimitiveExprIdAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIdASTContext):
        print("Primitive ID")
        return self.visitChildren(ctx)

    def visitPrimitiveExprTrueAST(self, ctx: MonkeyGrammarParser.PrimitiveExprTrueASTContext):
        print("Primitive True")
        return self.visitChildren(ctx)

    def visitPrimitiveExprFalseAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFalseASTContext):
        print("Primitive False")
        return self.visitChildren(ctx)

    def visitPrimitiveExprBlockExprAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        print("Primitive Block")
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        print("Expr List")
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        print("Expr Array")
        return self.visitChildren(ctx)

    def visitPrimitiveExprFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        print("Expr Func")
        return self.visitChildren(ctx)

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext):
        print("Primitive Expr Hash")
        return self.visitChildren(ctx)

    def visitPrimitiveExprPrintAST(self, ctx: MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        print("Primitive Expr Print")
        return self.visitChildren(ctx)

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext):
        print("Primitive Expr IF")
        return self.visitChildren(ctx)

    def visitArrayFunctions(self, ctx: MonkeyGrammarParser.ArrayFunctionsContext):
        print("Array Func")
        return self.visitChildren(ctx)

    def visitArrayLitetalAST(self, ctx: MonkeyGrammarParser.ArrayLitetalASTContext):
        print("Array Lits")
        return self.visitChildren(ctx)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        print("Funct Literals")
        return self.visitChildren(ctx)

    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):
        print("Func Parameters")
        return self.visitChildren(ctx)

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext):
        print("more identif")
        return self.visitChildren(ctx)

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext):
        print("Hash Literals")
        return self.visitChildren(ctx)

    def visitHashContentAST(self, ctx: MonkeyGrammarParser.HashContentASTContext):
        print("HashContent")
        return self.visitChildren(ctx)

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext):
        print("More Hash Contents")
        return self.visitChildren(ctx)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext):
        print("Expr List")
        return self.visitChildren(ctx)

    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext):
        print("Expr Empty")
        return self.visitChildren(ctx)

    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext):
        print("More expr")
        return self.visitChildren(ctx)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext):
        print("Print Expr")
        return self.visitChildren(ctx)

    def visitIfExpressionAST(self, ctx: MonkeyGrammarParser.IfExpressionASTContext):
        print("If Expr")
        return self.visitChildren(ctx)

    def visitBlockStatementAST(self, ctx: MonkeyGrammarParser.BlockStatementASTContext):
        print("BlockStatement")
        return self.visitChildren(ctx)

    def visitIdentifierAST(self, ctx: MonkeyGrammarParser.IdentifierASTContext):
        print("Identifier")
        return self.visitChildren(ctx)

    def visitCharAST(self, ctx: MonkeyGrammarParser.CharASTContext):
        print("Char")
        return self.visitChildren(ctx)
