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
        'INTEGER',
        'FLOAT',
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
        'COMMENT',
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
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'


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
    print(f"Illegal chacacter {t.value[0]} at line {t.lineno}")
    t.lexer.skip(1)


def build(**kwargs):
    lexer = lex.lex(**kwargs)
