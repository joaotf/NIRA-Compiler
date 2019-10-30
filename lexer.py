import ply.lex as lex

reservadas = {
        'if':'IF',
        'else':'ELSE',
        'while':'WHILE',
        'for':'FOR',
        'print':'PRINT',
        'read':'READ'
}

class Lexer(object):
    
    tokens = [
        'IDENTIFIER',
        'RESERVED',
        'NUMBER',
        'PLUS',
        'MINUS',
        'ASCII2A',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'ATRIBUTION',
        'EQUALITY',
        'RKEY',
        'LKEY',
        'ASPAS',
        'COMENTARIO',
        'RCOLCHETE',
        'LCOLCHETE'
    ]+list(reservadas.values())

    # Regular expression rules for simple tokens

    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_ASCII2A   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_RCOLCHETE = r'\]'
    t_LCOLCHETE = r'\['
    t_ATRIBUTION = r'\='
    t_EQUALITY = r'(==)'
    t_RKEY = r'\}'
    t_LKEY = r'\{'
    t_ASPAS = r'"'
    t_COMENTARIO = r'\#.*'

    # A regular expression rule with some action code
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t
    
    def t_IDENTIFIER(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reservadas.get(t.value,'IDENTIFIER')
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_COMMENT(self,t):
        r'\#.*'
        pass
    
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'
    
    # Error handling rule
    def t_error(self,t):
        r'\W+'
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    

    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)
if __name__ == '__main__':
    with open("command.txt",mode='r+') as file:
        textao = file.read()

    m = Lexer()
    m.build()
    m.test(textao)
