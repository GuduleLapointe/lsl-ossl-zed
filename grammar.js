module.exports = grammar({
	name: "lsl",

	extras: ($) => [/\s/, $.comment],

	word: ($) => $.identifier,

	rules: {
		source_file: ($) => repeat($._statement),

		// -----------------
		// Statements
		// -----------------
		_statement: ($) =>
			choice(
				$.function_definition,
				$.state_definition,
				$.variable_declaration,
				$.if_statement,
				$.for_statement,
				$.while_statement,
				$.return_statement,
				$.expression_statement,
				$.jump_statement,
			),

		// -----------------
		// States
		// -----------------
		state_definition: ($) => seq("state", $.identifier, $.block),

		// -----------------
		// Control flow
		// -----------------
		if_statement: ($) =>
			seq(
				"if",
				"(",
				$.expression,
				")",
				$.block,
				optional(seq("else", $.block)),
			),

		for_statement: ($) =>
			seq(
				"for",
				"(",
				optional($.expression),
				";",
				optional($.expression),
				";",
				optional($.expression),
				")",
				$.block,
			),

		while_statement: ($) => seq("while", "(", $.expression, ")", $.block),

		return_statement: ($) => seq("return", optional($.expression), ";"),

		jump_statement: ($) => seq(choice("jump", "state"), $.identifier, ";"),

		// -----------------
		// Functions
		// -----------------
		function_definition: ($) =>
			seq(
				$.type,
				$.identifier,
				"(",
				optional($.parameter_list),
				")",
				$.block,
			),

		parameter_list: ($) => seq($.parameter, repeat(seq(",", $.parameter))),

		parameter: ($) => seq($.type, $.identifier),

		// -----------------
		// Variables
		// -----------------
		variable_declaration: ($) =>
			seq($.type, $.identifier, optional(seq("=", $.expression)), ";"),

		// -----------------
		// Expressions
		// -----------------
		expression_statement: ($) => seq($.expression, ";"),

		expression: ($) =>
			choice(
				$.assignment,
				$.binary_expression,
				$.cast_expression,
				$.call_expression,
				$.constant,
				$.identifier,
				$.number,
				$.string,
			),

		assignment: ($) => seq($.identifier, "=", $.expression),

		cast_expression: ($) => seq("(", $.type, ")", $.expression),

		binary_expression: ($) =>
			prec.left(
				seq(
					$.expression,
					choice(
						"+",
						"-",
						"*",
						"/",
						"%",
						"==",
						"!=",
						"<",
						">",
						"<=",
						">=",
						"&&",
						"||",
					),
					$.expression,
				),
			),

		call_expression: ($) =>
			seq(
				field("function", $.identifier),
				"(",
				optional($.argument_list),
				")",
			),

		argument_list: ($) => seq($.expression, repeat(seq(",", $.expression))),

		block: ($) => seq("{", repeat($._statement), "}"),

		// -----------------
		// Tokens
		// -----------------
		type: ($) =>
			choice(
				"integer",
				"float",
				"string",
				"key",
				"vector",
				"rotation",
				"list",
			),

		constant: ($) => choice("TRUE", "FALSE", "NULL_KEY"),

		identifier: ($) => {
			const keywords = [
				"default",
				"state",
				"if",
				"else",
				"for",
				"while",
				"return",
				"jump",
			];
			return token(
				prec(
					-1,
					new RegExp(
						`(?!${keywords.join("|")})[a-zA-Z_][a-zA-Z0-9_]*`,
					),
				),
			);
		},

		number: ($) => /\d+(\.\d+)?/,

		string: ($) => /"([^"\\]|\\.)*"/,

		comment: ($) =>
			token(
				choice(
					seq("//", /.*/),
					seq("/*", /[^*]*\*+([^/*][^*]*\*+)*/, "/"),
				),
			),
	},
});
