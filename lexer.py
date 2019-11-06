import ply.lex as lex
import sys

reservadas = {
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'print': 'PRINT',
        'read': 'READ',
        'for': 'FOR',
        'break': 'BREAK',
        'return': 'RETURN',
        'write' : 'WRITE',
        'true' : 'TRUE',
        'false': 'FALSE',
        'string' : 'STRING',
        'do' : 'DO', 
    }

tokens = [
        'IDENTIFIER',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'TIMESX',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'ATRIBUTION',
        'EQUALITY',
        'RBRACE',
        'LBRACE',
        'ASPAS', 
        'COMENTARIO',
        'RCOLCHETE',
        'LCOLCHETE',
        'STRINGS',
        'LOG',
        'OU_LOGICO',
        'MAIOR',
        'MENOR',
        'MAIOREQUALS',
        'MENOREQUALS',
        'DIFERENTE',
        'SEMI',
        'PLUSPLUS',
        'MINUSMINUS',
    ] + list(reservadas.values())



t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_RCOLCHETE = r'\]'
t_LCOLCHETE = r'\['
t_ATRIBUTION = r'\='
t_EQUALITY = r'(==)'
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_ASPAS = r'"'
t_COMENTARIO = r'\#.*'
t_TIMESX = r'(\*\*)'
t_LOG = r'(&&)'
t_OU_LOGICO = r'(\|\|)'
t_MAIOR = r'>'
t_MENOR = r'<'
t_DIFERENTE = r'!='
t_MAIOREQUALS = r'>='
t_MENOREQUALS = r'<='
t_MINUSMINUS = r'--'
t_PLUSPLUS = r'\+\+'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'IDENTIFIER')
    return t

def t_STRING(t):
	r'\"([^\\\n]|(\\.))*?\"'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'

t_ignore  = ' \t'
    
def t_error(t):
    print(chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)

def build(**kwargs):
    lexer = lex.lex(**kwargs)
