import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
import pickle
import os.path

class Curso:
    def __init__(self, nome, grade):
        self.__nome=nome
        self.__listaAluno=[]
        self.__grade=grade
    
    def addAluno(self, aluno):
        self.__listaAluno.append(aluno)

    def getGrade(self):
        return self.__grade
        
    def getListaAluno(self):
        return self.__listaAluno

    def getNomeCurso(self):
        return self.__nome

class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle, listaGrade):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Curso")
        self.controle=controle
        
        self.frameNome=tk.Frame(self)
        self.frameGrade=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameNome.pack()
        self.frameGrade.pack()
        self.frameButton.pack()

        self.labelNome=tk.Label(self.frameNome, text="Nome do Curso")
        self.labelNome.pack(side="left")
        self.inputNome=tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.labelGrade=tk.Label(self.frameGrade, text='Defina a Grade:')
        self.labelGrade.pack(side='left')
        self.escolhaCombo=tk.StringVar()
        self.combobox=ttk.Combobox(self.frameGrade, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side='left')
        self.combobox['values']=listaGrade

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraCurso():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cursos', str)

class CtrlCurso():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        #self.listaCurso=[Curso("Engenharia de Software", "2019"), 
        #Curso("Sistemas Operacionais", "2019"), Curso("Análise de Algoritmos", "2019"),
        #Curso("Prog. Orientada a objetos", "2019")
        #]
        if not os.path.isfile('curso.pickle'):
            self.listaCurso=[]
        else:
            with open('curso.pickle', 'rb') as f:
                self.listaCurso=pickle.load(f)

    
    def salvaCurso(self):
        if len(self.listaCurso)!=0:
            with open('curso.pickle', 'wb') as f:
                pickle.dump(self.listaCurso, f)
    def getListaCurso(self):
        return self.listaCurso
        
    def getCurso(self, nome):
        estRet= None
        for est in self.listaCurso:
            if est.getNomeCurso()==nome:
                estRet=est
        return estRet
    
    def insereCurso(self):
        grad=self.controlePrincipal.ctrlGrade.getTodasGrades()
        todas=[]
        for i in grad:
            todas.append(i.getAno())
        self.limiteIns = LimiteInsereCurso(self, todas)
    
    def mostraCurso(self):
        str = ''
        for est in self.listaCurso:
            str+=est.getNomeCurso()+ '\n'+"Alunos: "+'\n'
            for i in est.getListaAluno():
                str+=i.getNome()+'\n'
            str+='\n'
        self.limiteLista=LimiteMostraCurso(str)

    def enterHandler(self, event):
        nome=self.limiteIns.inputNome.get()
        grade=self.limiteIns.escolhaCombo.get()
        curso=Curso(nome, grade)
        self.listaCurso.append(curso)
        self.limiteIns.mostraJanela("Sucesso", "Curso cadastrado")
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()