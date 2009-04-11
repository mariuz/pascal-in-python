# PROGRAM HEADING

# META

#start = 'block'

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVISION'),
    ('left', 'DIV', 'MOD'),
    ('left', 'EQ', 'NEQ', 'LTE','LT','GT','GTE'),
    ('left', 'OR', 'AND'),
)


def p_program_start(t):
	'program : header SEMICOLON block DOT'
	pass

def p_header(t):
	'header : PROGRAM IDENTIFIER'
	pass
	
def p_block(t):
	"""block : variable_declaration_part statement_part
	"""
	pass
	
	
def p_variable_declaration_part(t):
	"""variable_declaration_part : VAR variable_declaration_list
	 |
	"""
	pass

def p_variable_declaration_list(t):
	"""variable_declaration_list : variable_declaration variable_declaration_list
	 | variable_declaration
	"""
	# function and procedure missing here
	pass

def p_variable_declaration(t):
	"""variable_declaration : IDENTIFIER COLON type SEMICOLON"""
	pass
	
def p_type(t):
	""" type : TREAL 
	| TINTEGER
	| TCHAR
	| TSTRING """
	pass
	
def p_statement_part(t):
	"""statement_part : BEGIN statement_sequence END"""
	pass
	
def p_statement_sequence(t):
	"""statement_sequence : statement SEMICOLON statement_sequence
	 | statement"""
	pass
	
def p_statement(t):
	"""statement : assignment_statement
	 | statement_part
	 | if_statement
	 | while_statement
	 | repeat_statement
	 | """
	"""
	 | procedure_statement
	 | for_statement
	 |
	"""
	pass
	
	
def p_if_statement(t):
	"""if_statement : IF expression THEN statement ELSE statement
	| IF expression THEN statement
	"""
	
def p_while_statement(t):
	"""while_statement : WHILE expression DO statement"""
	
	
def p_repeat_statement(t):
	"""repeat_statement : REPEAT statement UNTIL expression"""
	
	
def p_assignment_statement(t):
	"""assignment_statement : IDENTIFIER ASSIGNMENT expression"""
	
def p_expression(t):
	"""expression : element
	 | expression sign element"""
	pass

def p_sign(t):
	"""sign : PLUS
	| MINUS
	| TIMES
	| DIVISION
	| DIV
	| MOD
	| AND
	| OR
	| EQ
	| NEQ
	| LT
	| LTE
	| GT
	| GTE
	"""
	pass


def p_element(t):
	"""element : IDENTIFIER
	| REAL
	| INTEGER
	| STRING
	| CHAR
	| LPAREN expression RPAREN
	| NOT element
	"""
	pass

def p_error(t):
	print "Syntax error in input, in line %d!" % 0