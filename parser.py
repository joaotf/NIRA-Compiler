import ply.yacc as yacc
import ply.lex as lexer
from lexer import tokens

structure = []

precedence = (
    ('left','LPAREN','RPAREN'),
    ('left','LOG','OU_LOGICO'),
    ('left','MAIOR','MENOR', 'MAIOREQUALS', 'MENOREQUALS', 'EQUALITY', 'DIFERENTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
)

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration
   '''
   pass

def p_declaration(p):
    '''declaration : var_declaration
				   | print_stmt
				   | selection_stmt
			       | iteration_stmt
	'''
    pass

def p_print_stmt(p):
	'''print_stmt   : PRINT LPAREN STRING RPAREN SEMI 
				    | PRINT LPAREN IDENTIFIER RPAREN SEMI 
				    | PRINT LPAREN NUMBER RPAREN SEMI 
				    | PRINT LPAREN boolean RPAREN SEMI 
                    | PRINT LPAREN expression RPAREN SEMI 
                    | PRINT LPAREN RPAREN SEMI 
	'''
	pass

def p_var_declaration(p):
	'''var_declaration : IDENTIFIER var_declaration
                       | IDENTIFIER 
                       | IDENTIFIER ATRIBUTION NUMBER var_declaration
                       | IDENTIFIER ATRIBUTION NUMBER
                       | IDENTIFIER ATRIBUTION boolean var_declaration
                       | IDENTIFIER ATRIBUTION boolean
                       | IDENTIFIER ATRIBUTION IDENTIFIER var_declaration
                       | IDENTIFIER ATRIBUTION IDENTIFIER 
                       | IDENTIFIER ATRIBUTION simple_expression 
	'''
	pass

def p_statement(p):
	'''statement : expression_stmt
				 | selection_stmt
				 | iteration_stmt
				 | print_stmt
	'''
	pass

def p_expression_stmt(p):
	'expression_stmt : expression'
	pass

def p_selection_stmt_1(p):
	'''selection_stmt : IF LPAREN expression RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE statement
					  | IF LPAREN expression RPAREN LBRACE expression RBRACE statement 
					  | IF LPAREN expression RPAREN LBRACE print_stmt RBRACE
					  | IF LPAREN expression RPAREN LBRACE print_stmt RBRACE ELSE LBRACE print_stmt RBRACE
	'''
	pass

def p_iteration_stmt_1(p):
	'''iteration_stmt : FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN LBRACE expression RBRACE statement 
					  | FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN LBRACE print_stmt RBRACE
	'''
	pass
def p_iteration_stmt_2(p):
	'''iteration_stmt : WHILE LPAREN expression RPAREN LBRACE expression RBRACE statement
					  | WHILE LPAREN expression RPAREN LBRACE print_stmt RBRACE
	'''
	pass

def p_iteration_stmt_3(p):
	'iteration_stmt : DO LBRACE statement SEMI RBRACE WHILE LPAREN expression RPAREN'
	pass

def p_expression(p):
	'''expression : var EQUALITY expression
				  | simple_expression
				  | var EQUALITY IDENTIFIER
			      | expression LOG expression
				  | expression OU_LOGICO expression
	'''
	pass

def p_var(p):
	'var : IDENTIFIER'
	pass

def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
	'''
	pass

def p_relop(p):
	'''relop : MENOR
			 | MENOREQUALS
			 | MAIOR
			 | MAIOREQUALS
			 | DIFERENTE
             | EQUALITY
	'''
	pass

def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | term MINUSMINUS
    				       | term PLUSPLUS
	'''
	pass

def p_addop(p):
	'''addop : PLUS
			 | MINUS
	'''
	pass

def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass

def p_mulop(p):
	'''mulop : TIMES
			 | DIVIDE
	'''
	pass

def p_factor(p):
	'''factor : LPAREN expression RPAREN
			  | var
			  | NUMBER
			  | boolean
			  | IDENTIFIER LPAREN args RPAREN
	'''
	pass

def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass


def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list(p):
	'args_list : expression'
	pass

def p_expressions_all(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term
                  | expression TIMESX term
                  | expression LOG term
                  | expression OU_LOGICO term
    '''
    if(p[2] == '+'):
        p[0] = p[1] + p[3]
    elif(p[2] == '-'):
        p[0] = p[1] - p[3]
    elif(p[2] == '*'):
        p[0] = p[1] * p[3]
    elif(p[2] == '/'):
        p[0] = p[1] / p[3]
    elif(p[2] == '**'):
        p[0] = p[1] ** p[3]
    elif(p[2] == '&&'):
        p[0] = p[1] and p[3]
    elif(p[2] == '||'):
        p[0] = p[1] or p[3]
    


def p_empty(p):
    'empty :'
    pass

    # Error rule for syntax errors
def p_error(p):
    if 1:
        if p is not None:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print("\t\tLine:  "+str(lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

    # Build the parser
parser=yacc.yacc(start='program')

