import sys
import os
import ply.lex as lex
import ply.yacc as yacc

import NIRA_Lexer as lexer
import NIRA_Parser as parserS
import NIRA_IDE as ide
 
def main(script):
    lexer.build()

    try:
        scriptfile = open(script, 'r+')
        scriptdata = scriptfile.read()
        lex.input(scriptdata)
        print(chr(27)+"[0;36m"+"Iniciando análise léxica"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lex.token()
            if not tok:
                break
            print("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            i += 1

        print(chr(27)+"[0;36m"+"Terminando análise léxica\n\n\n"+chr(27)+"[0m")
        
    

        print(chr(27)+"[0;36m"+"Iniciando a análise sintática"+chr(27)+"[0m")
        x = parserS.parser.parse(script, tracking=False)
        print(chr(27)+"[0;36m"+"Terminando a análise sintática"+chr(27)+"[0m")
        return x
        #else:
        #   print(chr(27)+"[0;31m"+"Passe o arquivo Python como parâmetro")
        #   print(chr(27)+"[0;36m"+"\t$ python3 main.py"+chr(27)+"[1;31m"+" <filename>.py"+chr(27)+"[0m")
    except EnvironmentError as e:
        print(e)



if __name__ == '__main__':
    ide.doidao1()
    