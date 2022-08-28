// Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MonkeyGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MonkeyGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MonkeyGrammarParser#startRule}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStartRule(MonkeyGrammarParser.StartRuleContext ctx);
	/**
	 * Visit a parse tree produced by {@link MonkeyGrammarParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(MonkeyGrammarParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link MonkeyGrammarParser#char}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChar(MonkeyGrammarParser.CharContext ctx);
}