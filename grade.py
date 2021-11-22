import tkinter as tk
from tkinter import messagebox
import pickle
import os.path

class Grade:
    def __init__(self, ano):
        self.__ano=ano
        self.__listaDisciplinas=[]
    
    def addDisciplinas(self, disciplina):
        self.__listaDisciplinas.append(disciplina)
    
    def getDisciplinas(self):
        return self.__listaDisciplinas
    
    def getAno(self):
        return self.__ano

class LimiteInsereGrade(tk.Toplevel):
    def __init__(self, controle, materias):
        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Grade")
        self.controle=controle

        self.frameAno=tk.Frame(self)
        self.frameDisciplinas=tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAno.pack()
        self.frameDisciplinas.pack()
        self.frameButton.pack()

        self.labelAno = tk.Label(self.frameAno, text="Ano")
        self.labelAno.pack(side='left')

        self.inputAno=tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side='left')

        self.labelEst = tk.Label(self.frameDisciplinas,text="Defina as Disciplinas: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameDisciplinas)
        self.listbox.pack(side="left")
        for nro in materias:
            self.listbox.insert(tk.END, nro.getCodigo())

        self.buttonSubmit2 = tk.Button(self.frameButton ,text="Inserir Disciplina")      
        self.buttonSubmit2.pack(side="left")
        self.buttonSubmit2.bind("<Button>", controle.inserirDisciplina)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Criar grade")      
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
class LimiteMostraGrade():
    def __init__(self, str):
        messagebox.showinfo("Grades: ",str)

class   CtrlGrade():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        self.listaDiscip=[]
        if not os.path.isfile('grade.pickle'):
            self.listaGrade=[]
        else:
            with open('grade.pickle', 'rb') as f:
                self.listaGrade=pickle.load(f)
    
    def salvaGrade(self):
        if len(self.listaGrade)!=0:
            with open('grade.pickle', 'wb') as f:
                pickle.dump(self.listaGrade, f)
    
    def getTodasGrades(self):
        return self.listaGrade

    def getGrade(self, ano):
        estRet=None
        for est in self.listaGrade:
            if est.getAno()==ano:
                estRet=est.getDisciplinas()
        return estRet
    
    def insereGrade(self):
        materias=self.controlePrincipal.ctrlDisciplina.getListaDisciplinas()
        self.limiteIns=LimiteInsereGrade(self, materias)
    
    def inserirDisciplina(self, event):
        codigo=self.limiteIns.listbox.get(tk.ACTIVE)
        materia=self.controlePrincipal.ctrlDisciplina.getDisciplina(codigo)
        self.listaDiscip.append(materia)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina Inserida')
        

    
    def mostraGrade(self):
        grad= "Grades\n"
        for est in self.listaGrade:
            grad+='Grade: '+str(est.getAno())+'\n'
            for i in est.getDisciplinas():
                grad+=i.getNome()+'\n'
            grad+='\n'
        self.limiteLista=LimiteMostraGrade(grad)
            
        

    def enterHandler(self, event):
        ano=self.limiteIns.inputAno.get()
        grade=Grade(ano)
        self.listaGrade.append(grade)
        for i in self.listaDiscip:
            grade.addDisciplinas(i)
        self.listaDiscip=[]
        self.limiteIns.mostraJanela("Sucesso", "Grade Inserida")
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        
    def fechaHandler(self, event):
        self.limiteIns.destroy()
