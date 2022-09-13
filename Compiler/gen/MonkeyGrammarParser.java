// Generated from C:/Users/bryam/Desktop/ProjectMonkeyCompiler/Compiler\MonkeyGrammar.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MonkeyGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, RETURN=2, GreaterT=3, LowerT=4, GreaterEQ=5, LowerEQ=6, Equeals=7, 
		BLOCK_OPEN=8, BLOCK_CLOSE=9, BRACKET_OPEN=10, BRACKET_CLOSE=11, PAR_OPEN=12, 
		PAR_CLOSE=13, LETTER=14, DIGIT=15, CHARIN=16, QUOTE=17, NotEqueals=18, 
		Sum=19, Res=20, Mul=21, Div=22, Mod=23, DivEnt=24, Open=25, Close=26, 
		Comment=27, Len=28, First=29, Last=30, Rest=31, Push=32, Boolean=33, WS=34, 
		COMMA=35, SEMICOLON=36, TRUE=37, FALSE=38, IF=39, ELSE=40;
	public static final int
		RULE_startRule = 0, RULE_identifier = 1, RULE_char = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "identifier", "char"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'return'", "'>'", "'<'", "'>='", "'<='", "'=='", "'['", 
			"']'", "'{'", "'}'", "'('", "')'", null, null, null, "'\"'", "'!='", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'//'", "'/*'", "'*/'", null, "'len'", 
			"'first'", "'last'", "'rest'", "'push'", null, null, "','", "';'", "'true'", 
			"'false'", "'if'", "'else'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "RETURN", "GreaterT", "LowerT", "GreaterEQ", "LowerEQ", 
			"Equeals", "BLOCK_OPEN", "BLOCK_CLOSE", "BRACKET_OPEN", "BRACKET_CLOSE", 
			"PAR_OPEN", "PAR_CLOSE", "LETTER", "DIGIT", "CHARIN", "QUOTE", "NotEqueals", 
			"Sum", "Res", "Mul", "Div", "Mod", "DivEnt", "Open", "Close", "Comment", 
			"Len", "First", "Last", "Rest", "Push", "Boolean", "WS", "COMMA", "SEMICOLON", 
			"TRUE", "FALSE", "IF", "ELSE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MonkeyGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MonkeyGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartRuleContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public StartRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).enterStartRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).exitStartRule(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MonkeyGrammarVisitor ) return ((MonkeyGrammarVisitor<? extends T>)visitor).visitStartRule(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StartRuleContext startRule() throws RecognitionException {
		StartRuleContext _localctx = new StartRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_startRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public List<TerminalNode> LETTER() { return getTokens(MonkeyGrammarParser.LETTER); }
		public TerminalNode LETTER(int i) {
			return getToken(MonkeyGrammarParser.LETTER, i);
		}
		public List<TerminalNode> DIGIT() { return getTokens(MonkeyGrammarParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(MonkeyGrammarParser.DIGIT, i);
		}
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MonkeyGrammarVisitor ) return ((MonkeyGrammarVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			match(LETTER);
			setState(12);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LETTER || _la==DIGIT) {
				{
				{
				setState(9);
				_la = _input.LA(1);
				if ( !(_la==LETTER || _la==DIGIT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(14);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CharContext extends ParserRuleContext {
		public List<TerminalNode> QUOTE() { return getTokens(MonkeyGrammarParser.QUOTE); }
		public TerminalNode QUOTE(int i) {
			return getToken(MonkeyGrammarParser.QUOTE, i);
		}
		public TerminalNode CHARIN() { return getToken(MonkeyGrammarParser.CHARIN, 0); }
		public CharContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).enterChar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MonkeyGrammarListener ) ((MonkeyGrammarListener)listener).exitChar(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MonkeyGrammarVisitor ) return ((MonkeyGrammarVisitor<? extends T>)visitor).visitChar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CharContext char_() throws RecognitionException {
		CharContext _localctx = new CharContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_char);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15);
			match(QUOTE);
			setState(16);
			match(CHARIN);
			setState(17);
			match(QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001(\u0014\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0005"+
		"\u0001\u000b\b\u0001\n\u0001\f\u0001\u000e\t\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0000\u0000\u0003\u0000\u0002\u0004"+
		"\u0000\u0001\u0001\u0000\u000e\u000f\u0011\u0000\u0006\u0001\u0000\u0000"+
		"\u0000\u0002\b\u0001\u0000\u0000\u0000\u0004\u000f\u0001\u0000\u0000\u0000"+
		"\u0006\u0007\u0003\u0002\u0001\u0000\u0007\u0001\u0001\u0000\u0000\u0000"+
		"\b\f\u0005\u000e\u0000\u0000\t\u000b\u0007\u0000\u0000\u0000\n\t\u0001"+
		"\u0000\u0000\u0000\u000b\u000e\u0001\u0000\u0000\u0000\f\n\u0001\u0000"+
		"\u0000\u0000\f\r\u0001\u0000\u0000\u0000\r\u0003\u0001\u0000\u0000\u0000"+
		"\u000e\f\u0001\u0000\u0000\u0000\u000f\u0010\u0005\u0011\u0000\u0000\u0010"+
		"\u0011\u0005\u0010\u0000\u0000\u0011\u0012\u0005\u0011\u0000\u0000\u0012"+
		"\u0005\u0001\u0000\u0000\u0000\u0001\f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}