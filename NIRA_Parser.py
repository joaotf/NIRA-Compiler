import ply.yacc as yacc
import ply.lex as lexer
from NIRA_Lexer import tokens
import sys
import os

precedence = (
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LOG', 'OU_LOGICO'),
    ('left', 'MAIOR', 'MENOR', 'MAIOREQUALS',
     'MENOREQUALS', 'EQUALITY', 'DIFERENTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
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
				   | read_stmt
				   | selection_stmt
			       | iteration_stmt
				   | expression
	'''
    pass


def p_print_stmt(p):
	'''print_stmt   : PRINT LPAREN STRING RPAREN SEMI declaration
					| PRINT LPAREN STRING RPAREN SEMI
				    | PRINT LPAREN IDENTIFIER RPAREN SEMI declaration
					| PRINT LPAREN IDENTIFIER RPAREN SEMI
				    | PRINT LPAREN NUMBER RPAREN SEMI declaration
					| PRINT LPAREN NUMBER RPAREN SEMI
				    | PRINT LPAREN boolean RPAREN SEMI declaration
					| PRINT LPAREN boolean RPAREN SEMI
                    | PRINT LPAREN expression RPAREN SEMI declaration
					| PRINT LPAREN expression RPAREN SEMI
                    | PRINT LPAREN RPAREN SEMI declaration
					| PRINT LPAREN RPAREN SEMI
	'''
	pass


def p_var_declaration(p):
	'''var_declaration : IDENTIFIER var_declaration
                       | IDENTIFIER
                       | IDENTIFIER ATRIBUTION NUMBER var_declaration
                       | IDENTIFIER ATRIBUTION NUMBER SEMI
                       | IDENTIFIER ATRIBUTION boolean var_declaration
                       | IDENTIFIER ATRIBUTION boolean SEMI
                       | IDENTIFIER ATRIBUTION IDENTIFIER var_declaration
                       | IDENTIFIER ATRIBUTION IDENTIFIER SEMI
                       | IDENTIFIER ATRIBUTION simple_expression SEMI
	'''
	pass


def p_statement(p):
	'''statement : expression_stmt
				 | selection_stmt
				 | iteration_stmt
				 | print_stmt
				 | read_stmt
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
					  | FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN LBRACE statement RBRACE
	'''
	pass


def p_iteration_stmt_2(p):
	'''iteration_stmt : WHILE LPAREN expression RPAREN LBRACE expression RBRACE statement
					  | WHILE LPAREN expression RPAREN LBRACE print_stmt RBRACE
	'''
	pass


def p_iteration_stmt_3(p):
	'''iteration_stmt : DO LBRACE statement SEMI RBRACE WHILE LPAREN expression RPAREN SEMI
					  | DO LBRACE print_stmt RBRACE WHILE LPAREN expression RPAREN SEMI
	'''
	pass


def p_read_stmt(p):
	'''
		read_stmt : READ LPAREN STRING RPAREN SEMI declaration
				  | READ LPAREN STRING RPAREN SEMI
			      | IDENTIFIER READ LPAREN STRING RPAREN SEMI
				  | IDENTIFIER READ LPAREN RPAREN SEMI
	'''
	pass


def p_expression(p):
	'''expression : IDENTIFIER EQUALITY expression
				  | simple_expression
				  | IDENTIFIER EQUALITY IDENTIFIER
			      | expression LOG expression
				  | expression OU_LOGICO expression
	'''
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
			  | IDENTIFIER
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


def p_number(p):
	'''NUMBER : INTEGER
			  | FLOAT
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

    return p[0]


def p_empty(p):
    'empty :'
    pass

def p_error(p):
	if True:
		if p is not None:
			print(chr(27)+"[1;31m"+"  ERROR: Syntax error - Unexpected token"+chr(27)+"[0m")
			print("\t\tLine: "+str((p.lexer.lineno))+"\t=> "+str(p.value))
		else:
			print(chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
			print("\t\tLine:  "+str(lexer.lexer.lineno))
	else:
		raise Exception('syntax','error')

parser = yacc.yacc(start='program')
