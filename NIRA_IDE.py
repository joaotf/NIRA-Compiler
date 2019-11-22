import tkinter as tk
from tkinter import *
import re
import os
from tkinter.messagebox import *
from tkinter.filedialog import *
from tksheet import Sheet
from tkinter import ttk

import NIRA_Lexer as lexical
import NIRA_Main as Main


class Notepad:
    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisCompilerButton = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Untitled")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)

        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label="Novo",
                                        command=self.__newFile)

        self.__thisFileMenu.add_command(label="Abrir",
                                        command=self.__openFile)

        self.__thisFileMenu.add_command(label="Salvar",
                                        command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Compilar",
                                       command=self.__compilar)
        self.__thisFileMenu.add_command(label="Tokens",
                                        command=self.__open_windows)

        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Fechar",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Arquivo",
                                       menu=self.__thisFileMenu)

       
        self.__thisEditMenu.add_command(label="Cortar",
                                        command=self.__cut)

        self.__thisEditMenu.add_command(label="Copiar",
                                        command=self.__copy)

        self.__thisEditMenu.add_command(label="Colar",
                                        command=self.__paste)

        self.__thisMenuBar.add_cascade(label="Editar",
                                       menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="Ajuda",
        command=self.__ajuda)
        self.__thisMenuBar.add_cascade(label="Ajuda",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()
        exit()
    def __ajuda(self):
        root = Tk();
        root.geometry('250x300')
        
        text = Text(root)
        text.insert(INSERT,"Eu também preciso de ajuda!")
        text.pack()

    def __compilar(self):
        content = ""
        content2 = ""
        linhao = 0
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
        y = os.path.basename(self.__file)
       
        with open(y,'r+', encoding="utf8") as file:
            for linha in file:
                linhao += 1
            content = file.readlines()
        
        x = Main.main(y)
        
        
        content2 = str(x).replace(",","\n").replace("[","").replace("]","").replace("'","").replace('"',"").replace("\\","/")
    
        with open("result.txt",'w+', encoding="utf8") as file1:
            file1.writelines("")
            content = file1.writelines(content2)

        self.__root.title(y)

        file = open("result.txt", "r+", encoding="utf8")
        
        root = Tk();
        root.geometry('500x600')
        
        text = Text(root,height=30,width=40)

        text.insert(INSERT,file.read())
        text.pack()

        file.close()





    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r", encoding="utf8")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __open_windows(self):
        root = Tk();
        root.geometry("700x500")
        root.title("Tokens");

        treeview = ttk.Treeview(root)
        treeview.pack(fill="x");
        
        style = ttk.Style(root)
        style.configure("Treeview", rowheight=50)
        treeview.configure(style="Treeview")


        treeview.insert('',0,'1',text="Token (Palavra Reservada)")

        treeview.insert('',1,'2',text="Token (Identificador)")
        
        treeview.insert('',2,'3',text="Token (Double)")
        
        treeview.insert('',3,'4',text="Token (Inteiro)")

        treeview.insert('',4,'5',text="Token (Atribuição)")

        treeview.insert('',5,'6',text="Token (Agrupadores)")
        
        treeview.insert('',6,'7',text="Token (Comparador)")
        
        treeview.insert('',7,"8",text="Token (Comentário)")

        for i in lexical.reservadas:
            treeview.insert("1","end",text="PR : "+i)

        treeview.insert("2","end",text="Qualquer palavra que não contenha : @!#$%¨¨&*()")
       
        treeview.insert("5","end",text="=")

        treeview.insert("8","end",text="Comentário : #")
    
    def __saveFile(self):

        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                file = open(self.__file, "w", encoding="utf8")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        self.__root.mainloop()



def doidao1():
    notepad = Notepad(width=800, height=600)
    notepad.run()


