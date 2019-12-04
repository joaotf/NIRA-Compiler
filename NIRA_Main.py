import sys
import os
import ply.lex as lex
import ply.yacc as yacc

import NIRA_Lexer as lexer
import NIRA_Parser as parserS
import NIRA_IDE as ide

lextatico = []

def main(script):
    lexer.build()
    try:
        scriptfile = open(script, 'r+')
        scriptdata = scriptfile.read()
        lex.input(scriptdata)
        lextatico.append("Iniciando análise léxica")
        i = 1
        while True:
            tok = lex.token()
            if not tok:
                break
            lextatico.append(str(i)+" - "+"Line: "+str(tok.lineno)+"   "+str(tok.type)+"  --->  "+str(tok.value))
            i += 1

        lextatico.append("Terminando análise léxica                             ")
        
    

        lextatico.append("Iniciando a análise sintática")
        lextatico.append(parserS.parser.parse(scriptdata, tracking=False))
        lextatico.append("Terminando a análise sintática")
    
        return lextatico

    except EnvironmentError as e:
        print(e)


if __name__ == '__main__':
    ide.doidao1();
    if (len(sys.argv) > 1):
        script = sys.argv[1]
    print(main(script))


