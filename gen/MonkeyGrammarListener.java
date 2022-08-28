// Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MonkeyGrammarParser}.
 */
public interface MonkeyGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MonkeyGrammarParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(MonkeyGrammarParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link MonkeyGrammarParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(MonkeyGrammarParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link MonkeyGrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(MonkeyGrammarParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link MonkeyGrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(MonkeyGrammarParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link MonkeyGrammarParser#char}.
	 * @param ctx the parse tree
	 */
	void enterChar(MonkeyGrammarParser.CharContext ctx);
	/**
	 * Exit a parse tree produced by {@link MonkeyGrammarParser#char}.
	 * @param ctx the parse tree
	 */
	void exitChar(MonkeyGrammarParser.CharContext ctx);
}