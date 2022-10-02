from Generated.MonkeyGrammarParser import MonkeyGrammarParser
from Generated.MonkeyGrammarVisitor import MonkeyGrammarVisitor
from REPL import REPL
from antlr4.CommonTokenFactory import CommonToken


class MyVisitor(MonkeyGrammarVisitor):
    replVisitor = REPL()

    def visitProgramAST(self, ctx: MonkeyGrammarParser.ProgramASTContext):
        return self.visitChildren(ctx)

    def visitStatementLetAST(self, ctx: MonkeyGrammarParser.StatementLetASTContext):
        return self.visitChildren(ctx)

    def visitStatementReturnAST(self, ctx: MonkeyGrammarParser.StatementReturnASTContext):
        return self.visitChildren(ctx)

    def visitStatementExpressionAST(self, ctx: MonkeyGrammarParser.StatementExpressionASTContext):
        return self.visitChildren(ctx)

    def visitLetStatementAST(self, ctx: MonkeyGrammarParser.LetStatementASTContext):
        self.visit(ctx.expression())
        self.replVisitor.data.add(ctx.identifier().start.text, self.replVisitor.stack.pop())

    def visitReturnStatementAST(self, ctx: MonkeyGrammarParser.ReturnStatementASTContext):
        return self.visitChildren(ctx)

    def visitExpressionStatementAST(self, ctx: MonkeyGrammarParser.ExpressionStatementASTContext):
        return self.visitChildren(ctx)

    def visitExpressionAST(self, ctx: MonkeyGrammarParser.ExpressionASTContext):
        return self.visitChildren(ctx)

    def visitComparisonAST(self, ctx: MonkeyGrammarParser.ComparisonASTContext):
        return self.visitChildren(ctx)

    def visitAdditionExpressionAST(self, ctx: MonkeyGrammarParser.AdditionExpressionASTContext):
        return self.visitChildren(ctx)

    def visitAdditionFactorAST(self, ctx: MonkeyGrammarParser.AdditionFactorASTContext):
        for i in range(0,len(ctx.multiplicationExpression())):
            self.visit(ctx.multiplicationExpression(i))
            op2 = (int)(self.replVisitor.stack.pop())
            op1 = (int)(self.replVisitor.stack.pop())
            self.replVisitor.stack.append(op1+op2)


    def visitMultiplicationExpressionAST(self, ctx: MonkeyGrammarParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)

    def visitMultiplicationFactorAST(self, ctx: MonkeyGrammarParser.MultiplicationFactorASTContext):
        return self.visitChildren(ctx)

    def visitElementExpressionAST(self, ctx: MonkeyGrammarParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)

    def visitElementAccessAST(self, ctx: MonkeyGrammarParser.ElementAccessASTContext):
        return self.visitChildren(ctx)

    def visitCallExpressionAST(self, ctx: MonkeyGrammarParser.CallExpressionASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprDigitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprDigitASTContext):
        self.replVisitor.stack.append((int)(ctx.DIGIT().symbol.text))
        return self.visitChildren(ctx)

    def visitPrimitiveExprStringAST(self, ctx: MonkeyGrammarParser.PrimitiveExprStringASTContext):
        self.replVisitor.stack.append(ctx.STRING().symbol.text)
        return self.visitChildren(ctx)

    def visitPrimitiveExprIdAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIdASTContext):
        object = self.replVisitor.data.get(ctx.identifier().start.text)
        if(object!=None):
            self.replVisitor.stack.append(object)
        else:
            print("El identificador no existe")

        return self.visitChildren(ctx)

    def visitPrimitiveExprTrueAST(self, ctx: MonkeyGrammarParser.PrimitiveExprTrueASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprFalseAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFalseASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprBlockExprAST(self, ctx: MonkeyGrammarParser.PrimitiveExprBlockExprASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrLitAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrLitASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprArrFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprArrFuncASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprFuncAST(self, ctx: MonkeyGrammarParser.PrimitiveExprFuncASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprHashAST(self, ctx: MonkeyGrammarParser.PrimitiveExprHashASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprPrintAST(self, ctx: MonkeyGrammarParser.PrimitiveExprPrintASTContext):
        return self.visitChildren(ctx)

    def visitPrimitiveExprIfAST(self, ctx: MonkeyGrammarParser.PrimitiveExprIfASTContext):
        return self.visitChildren(ctx)

    def visitArrayFunctions(self, ctx: MonkeyGrammarParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)

    def visitArrayLitetalAST(self, ctx: MonkeyGrammarParser.ArrayLitetalASTContext):
        return self.visitChildren(ctx)

    def visitFunctionLiteralAST(self, ctx: MonkeyGrammarParser.FunctionLiteralASTContext):
        return self.visitChildren(ctx)

    def visitFunctionParametersAST(self, ctx: MonkeyGrammarParser.FunctionParametersASTContext):
        return self.visitChildren(ctx)

    def visitMoreIdentifiersAST(self, ctx: MonkeyGrammarParser.MoreIdentifiersASTContext):
        return self.visitChildren(ctx)

    def visitHashLiteralAST(self, ctx: MonkeyGrammarParser.HashLiteralASTContext):
        return self.visitChildren(ctx)

    def visitHashContentAST(self, ctx: MonkeyGrammarParser.HashContentASTContext):
        return self.visitChildren(ctx)

    def visitMoreHashContentAST(self, ctx: MonkeyGrammarParser.MoreHashContentASTContext):
        return self.visitChildren(ctx)

    def visitExpressionListAST(self, ctx: MonkeyGrammarParser.ExpressionListASTContext):
        return self.visitChildren(ctx)

    def visitExpressionListEmptyAST(self, ctx: MonkeyGrammarParser.ExpressionListEmptyASTContext):
        return self.visitChildren(ctx)

    def visitMoreExpressionsAST(self, ctx: MonkeyGrammarParser.MoreExpressionsASTContext):
        return self.visitChildren(ctx)

    def visitPrintExpressionAST(self, ctx: MonkeyGrammarParser.PrintExpressionASTContext):
        try:

            self.visit(ctx.expression())
            print(self.replVisitor.stack.pop())
        except:
            print("Error")
        return self.visitChildren(ctx)

    def visitIfExpressionAST(self, ctx: MonkeyGrammarParser.IfExpressionASTContext):
        return self.visitChildren(ctx)

    def visitBlockStatementAST(self, ctx: MonkeyGrammarParser.BlockStatementASTContext):
        return self.visitChildren(ctx)

    def visitIdentifierAST(self, ctx: MonkeyGrammarParser.IdentifierASTContext):
        return self.visitChildren(ctx)

    def visitCharAST(self, ctx: MonkeyGrammarParser.CharASTContext):
        return self.visitChildren(ctx)
