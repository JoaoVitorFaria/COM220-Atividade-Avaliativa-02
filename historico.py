import tkinter as tk
from tkinter import messagebox
from aluno import Aluno
import disciplina as dcp
import aluno as aln

import pickle
import os.path
class Historico:
    def __init__(self, ano, semestre, nota, disciplina, codigo, cargaHoraria):
        
        self.__ano=ano
        self.__semestre=semestre
        self.__nota=nota
        self.__disciplina=disciplina
        self.__aluno=[]
        self.__codigo=codigo
        self.__cargaHoraria=cargaHoraria
    
    
    
    def getAluno(self):
        return self.__aluno
    
    def getCodigo(self):
        return self.__codigo

    def getDisciplina(self):
        return self.__disciplina
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getAno(self):
        return self.__ano
    
    def getSemestre(self):
        return self.__semestre
    
    def getNota(self):
        return self.__nota

class LimiteInsereHistorico(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x200')
        self.title("Histórico")
        self.controle=controle

        self.frameAluno=tk.Frame(self)
        self.frameDisciplina=tk.Frame(self)
        self.frameAno=tk.Frame(self)
        self.frameSemestre=tk.Frame(self)
        self.frameNota=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        
        self.frameAluno.pack()
        self.frameDisciplina.pack()
        self.frameAno.pack()
        self.frameSemestre.pack()
        self.frameNota.pack()
        self.frameButton.pack()

        

        self.labelAluno=tk.Label(self.frameAluno, text='Nro de Matrícula do Aluno:')
        self.labelAluno.pack(side="left")
        self.inputAluno=tk.Entry(self.frameAluno, width=20)
        self.inputAluno.pack(side='left')

        self.labelDisciplina=tk.Label(self.frameDisciplina, text='Código da Disciplina:')
        self.labelDisciplina.pack(side="left")
        self.inputDisc=tk.Entry(self.frameDisciplina, width=20)
        self.inputDisc.pack(side='left')

        self.labelAno=tk.Label(self.frameAno, text='Ano: ')
        self.labelAno.pack(side='left')
        self.inputAno=tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side='left')

        self.labelSemestre=tk.Label(self.frameSemestre, text='Semestre: ')
        self.labelSemestre.pack(side='left')
        self.inputSemestre=tk.Entry(self.frameSemestre, width=20)
        self.inputSemestre.pack(side='left')

        self.labelNota=tk.Label(self.frameNota, text='Nota: ')
        self.labelNota.pack(side='left')
        self.inputNota=tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side='left')

        self.buttonSubmit = tk.Button(self.frameButton ,text="Inserir Disciplina")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereDisciplina)

        self.buttonSubmit2 = tk.Button(self.frameButton ,text="Inserir Aluno")      
        self.buttonSubmit2.pack(side="left")
        self.buttonSubmit2.bind("<Button>", controle.insereAluno)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
class LimiteMostraHistorico():
    def __init__(self, str):
        messagebox.showinfo("Historico", str)

class limiteConsultaHistorico(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x200')
        self.title("Histórico")
        self.controle=controle

        self.frameAluno=tk.Frame(self)
        self.frameButton=tk.Frame(self)

        self.frameAluno.pack()
        self.frameButton.pack()

        self.labelAluno=tk.Label(self.frameAluno, text='Nro de Matrícula do Aluno:')
        self.labelAluno.pack(side="left")
        self.inputAluno=tk.Entry(self.frameAluno, width=20)
        self.inputAluno.pack(side='left')

        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar Histórico")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandlerHistorico)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerConsulta) 

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlHistorico():
    def __init__(self,controlePrincipal):
        self.controlePrincipal=controlePrincipal
        if not os.path.isfile('historico.pickle'):
            self.historicos={}
        else:
            with open('historico.pickle', 'rb') as f:
                self.historicos=pickle.load(f)

    def salvaHistorico(self):
        if len(self.historicos)!=0:
            with open('historico.pickle', 'wb') as f:
                pickle.dump(self.historicos, f)
    
    def insereHistorico(self):
        self.disciplinas=[]
        self.limiteIns=LimiteInsereHistorico(self)

    def consultaHistorico(self):
        self.limiteCons=limiteConsultaHistorico(self)

    def mostraHistorico(self):
        hist="Historicos\n"
        for est in self.historicos:
            hist+="Aluno: "+est.getNome()+"--"+est.getNroMatric()+'\n'
            hist+="Disciplina      Ano      Semestre      Nota\n"
            for procura in self.historicos[est]:
                hist+=procura.getDisciplina()+"      "+str(procura.getAno())+"      "+str(procura.getSemestre())+"      "+str(procura.getNota())+'\n'
        self.limiteLista=LimiteMostraHistorico(hist)

    def consultaHandlerHistorico(self, event):
        matricula=self.limiteCons.inputAluno.get()
        texto=''
        for est in self.historicos:
            if est.getNroMatric()==matricula:
                texto+="Nome: "+est.getNome()+"\nMatricula: "+est.getNroMatric()+"\n"
                for i in range(1,9):
                    texto+= str(i) + " Semestre\n"
                    texto+='Codigo         Disciplina         Status\n'
                    for procura in self.historicos[est]:
                        if int(procura.getSemestre())==i:
                            texto+=str(procura.getCodigo())+"         "+procura.getDisciplina()
                            if int(procura.getNota()) >= 6:
                                texto+="         Aprovado\n"
                            else:
                                texto+="         Reprovado"
                        else:
                            texto+= "---------         ---------         ---------\n"
                mat=est.getNroMatric()
                estudante=self.controlePrincipal.ctrlAluno.getAluno(mat)
                nomeCurso=estudante.getCurso()
                curso=self.controlePrincipal.ctrlCurso.getCurso(nomeCurso)
                grade=curso.getGrade()
                obrigatorias=self.controlePrincipal.ctrlGrade.getGrade(grade)
                totalOptativa=0
                totalObriga=0
                for procura in self.historicos[est]:
                    for i in obrigatorias:
                        if procura.getCodigo()==i.getCodigo():
                            totalObriga+=int(procura.getCargaHoraria())
                        else:
                            totalOptativa+=int(procura.getCargaHoraria())
                        
                texto+="Total Obrigatorias: "+ str(totalObriga)+'\n'
                texto+="Total Optativas: "+str(totalOptativa)+'\n'                  
                                
                                       
        self.limiteLista=LimiteMostraHistorico(texto)

                

    def insereDisciplina(self, event):
        ano=self.limiteIns.inputAno.get()
        nota=self.limiteIns.inputNota.get()
        semestre=self.limiteIns.inputSemestre.get()
        codDis=self.limiteIns.inputDisc.get()
        disc=self.controlePrincipal.ctrlDisciplina.getDisciplina(codDis)
        hist=Historico( ano, semestre, nota, disc.getNome(), disc.getCodigo(), disc.getCargaHoraria())
        
        self.disciplinas.append(hist)
        self.limiteIns.mostraJanela("Sucesso", "Disciplina Inserida no Histórico")
        self.clearHandler(event)

    def insereAluno(self, event):
        nroMat=self.limiteIns.inputAluno.get()
        aluno=self.controlePrincipal.ctrlAluno.getAluno(nroMat)
        self.historicos[aluno]=self.disciplinas
        self.limiteIns.mostraJanela("Sucesso", "Aluno inserido no histórico")

    def clearHandler(self, event):
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputDisc.delete(0, len(self.limiteIns.inputDisc.get()))
        self.limiteIns.inputNota.delete(0, len(self.limiteIns.inputNota.get()))
        self.limiteIns.inputSemestre.delete(0, len(self.limiteIns.inputSemestre.get()))
        
    def clearHandlerConsulta(self, event):
        self.limiteCons.inputAluno.delete(0, len(self.limiteCons.inputAluno.get()))
        
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def fechaHandlerConsulta(self, event):
        self.limiteCons.destroy()
