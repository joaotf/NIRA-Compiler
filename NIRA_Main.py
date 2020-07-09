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
            lextatico.append("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"   "+str(tok.type)+"  --->  "+str(tok.value))
            i += 1

        lextatico.append("Terminando análise léxica\n")

        lextatico.append("\nIniciando a análise sintática")
        parserS.y.parse(scriptdata, tracking=False)
        if(len(parserS.errors) == 0):
            lextatico.append("\tNão há erros sintáticos no código!");            
        else:
            lextatico.append(parserS.errors);
        lextatico.append("Terminando a análise sintática")

        with open("result.txt","w+") as file:
            for x in range(len(lextatico)):
                file.writelines(lextatico[x]);
                file.writelines("\n");
                
        file.close()
        
    except EnvironmentError as e:
        print(e)


if __name__ == '__main__':
    #ide.doidao1();
    if (len(sys.argv) > 1):
        script = sys.argv[1]
    print(main(script))


