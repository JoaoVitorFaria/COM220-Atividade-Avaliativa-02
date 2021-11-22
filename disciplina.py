import tkinter as tk 
from tkinter import messagebox
import pickle
import os.path

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria=cargaHoraria
        self.__listaDisciplinas=[]

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameCargaHoraria = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHoraria.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCarga = tk.Label(self.frameCargaHoraria, text="Carga Horária:")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")  
        self.labelCarga.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")  
        self.inputCarga = tk.Entry(self.frameCargaHoraria, width=20)
        self.inputCarga.pack(side="left")            
      
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

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)


class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        #self.listaDisciplinas=[ Disciplina("COM220", "Orientada a objetos", 64), Disciplina('COM222', 'Programação Web',48),Disciplina('COM111', 'Estruturas de Dados', 96)]
        if not os.path.isfile('disciplina.pickle'):
            self.listaDisciplinas=[]
        else:
            with open('disciplina.pickle', 'rb') as f:
                self.listaDisciplinas=pickle.load(f)

    def salvaDisciplina(self):
        if len(self.listaDisciplinas)!=0:
            with open('disciplina.pickle', 'wb') as f:
                pickle.dump(self.listaDisciplinas, f)

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getDisciplina(self, codDisc):
        discRet= None
        for disc in self.listaDisciplinas:
            if disc.getCodigo()==codDisc:
                discRet=disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def insereDisciplina(self):
        self.limiteIns=LimiteInsereDisciplinas(self)  

    def mostraDisciplina(self):
        discip = 'Código -- Nome -- Carga Horaria\n'
        for disc in self.listaDisciplinas:
            discip+= str(disc.getCodigo())+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteLista=LimiteMostraDisciplinas(discip)
    
    def enterHandler(self, event):
        codigo=self.limiteIns.inputCodigo.get()
        nome=self.limiteIns.inputNome.get()
        carga=self.limiteIns.inputCarga.get()
        discip=Disciplina(codigo, nome, carga)
        self.listaDisciplinas.append(discip)
        self.limiteIns.mostraJanela("Sucesso", "Disciplina Cadastrada")
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCarga.delete(0, len(self.limiteIns.inputCarga.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

            