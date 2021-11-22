import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pickle
import os.path

class Aluno:
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome 
        self.__curso=curso

    def getNroMatric(self):
        return self.__nroMatric
    
    def setCurso(self, curso):
        self.__curso=curso
    
    def getCurso(self):
        return self.__curso
    
    def getNome(self):
        return self.__nome

class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaCurso):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Aluno")
        self.controle=controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso=tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso, text='Curso')
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")  

        self.labelCurso = tk.Label(self.frameCurso,text="Escolha o Curso: ")
        self.labelCurso.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCurso

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

class LimiteMostraAluno():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class CtrlAluno():
    def __init__(self,controlePrincipal):
        self.controlePrincipal=controlePrincipal
        if not os.path.isfile('aluno.pickle'):
            self.listaAluno=[]
        else:
            with open('aluno.pickle', 'rb') as f:
                self.listaAluno=pickle.load(f)
        #self.listaAluno=[Aluno("2020" , "João Lucas",'teste' ),Aluno("2030" , "Luis Felipe", 'teste'),Aluno("2040" , "Ana Clara", 'teste'), Aluno("2050" , "Pedro Henrique", 'teste')]

    def salvaAluno(self):
        if len(self.listaAluno)!=0:
            with open('aluno.pickle', 'wb') as f:
                pickle.dump(self.listaAluno, f)

    def getAluno(self, nroMatric):
        estRet = None
        for est in self.listaAluno:
            if est.getNroMatric()==nroMatric:
                estRet=est
        return estRet
        

    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaAluno:
            listaNro.append(est.getNroMatric())
        return listaNro

    def insereAluno(self):
        cursos=self.controlePrincipal.ctrlCurso.getListaCurso()
        certo=[]
        for i in cursos:
            certo.append(i.getNomeCurso())
        self.limiteIns = LimiteInsereAluno(self, certo) 
    
    def mostraAluno(self):
        str = 'Nro Matric. -- Nome --  Curso\n'
        for est in self.listaAluno:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '    --    '+est.getCurso()+ '\n'       
        self.limiteLista = LimiteMostraAluno(str)
    
    def enterHandler(self, event):
        nroMatric=self.limiteIns.inputNro.get()
        nome=self.limiteIns.inputNome.get()
        curso=self.limiteIns.escolhaCombo.get()
        aluno= Aluno(nroMatric, nome, curso)            
        self.listaAluno.append(aluno)

        teste=self.controlePrincipal.ctrlCurso.getCurso(curso)
        teste.addAluno(aluno)
        self.limiteIns.mostraJanela("Sucesso", "Aluno cadastrado")
        self.clearHandler(event)
        self.limiteIns.destroy()
    
    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()