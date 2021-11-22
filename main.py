import tkinter as tk
from tkinter import messagebox
import aluno as aln 
import curso as crs 
import grade as grd 
import disciplina as dcp 
import historico as htr 

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x450')
        self.menubar =tk.Menu(self.root) 

        self.alunoMenu=tk.Menu(self.menubar)
        self.cursoMenu=tk.Menu(self.menubar)
        self.gradeMenu=tk.Menu(self.menubar)
        self.disciplinaMenu=tk.Menu(self.menubar)
        self.historicoMenu=tk.Menu(self.menubar)
        self.sairMenu=tk.Menu(self.menubar)

        self.alunoMenu.add_command(label='Insere', \
                    command=self.controle.insereAluno)
        self.alunoMenu.add_command(label='Lista',\
                    command=self.controle.mostraAluno)
        self.menubar.add_cascade(label="Aluno",\
                    menu=self.alunoMenu)

        self.cursoMenu.add_command(label='Insere', \
                    command=self.controle.insereCurso)
        self.cursoMenu.add_command(label='Lista',\
                    command=self.controle.mostraCurso)
        self.menubar.add_cascade(label="Curso",\
                    menu=self.cursoMenu)

        self.gradeMenu.add_command(label='Insere', \
                    command=self.controle.insereGrade)
        self.gradeMenu.add_command(label='Lista',\
                    command=self.controle.mostraGrade)
        self.menubar.add_cascade(label="Grade",\
                    menu=self.gradeMenu)
        
        self.disciplinaMenu.add_command(label='Insere', \
                    command=self.controle.insereDisciplina)
        self.disciplinaMenu.add_command(label='Lista',\
                    command=self.controle.mostraDisciplina)
        self.menubar.add_cascade(label="Disciplina",\
                    menu=self.disciplinaMenu)
        
        self.historicoMenu.add_command(label='Insere', \
                    command=self.controle.insereHistorico)
        self.historicoMenu.add_command(label='Lista',\
                    command=self.controle.mostraHistorico)
        self.historicoMenu.add_command(label='Consulta', \
                    command=self.controle.consultaHistorico)
        self.menubar.add_cascade(label="Histórico",\
                    menu=self.historicoMenu)
        
        self.sairMenu.add_command(label='Salvar',\
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label='Sair',\
                    menu=self.sairMenu)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno=aln.CtrlAluno(self)
        self.ctrlCurso=crs.CtrlCurso(self)
        self.ctrlGrade=grd.CtrlGrade(self)
        self.ctrlDisciplina=dcp.CtrlDisciplina(self)
        self.ctrlHistorico=htr.CtrlHistorico(self)

        self.limite= LimitePrincipal(self.root, self)

        self.root.title("SIGAA 2.0")
        self.root.mainloop()
    
    def insereAluno(self):
        self.ctrlAluno.insereAluno()
    
    def mostraAluno(self):
        self.ctrlAluno.mostraAluno()
    
    def insereCurso(self):
        self.ctrlCurso.insereCurso()
    
    def mostraCurso(self):
        self.ctrlCurso.mostraCurso()

    def insereDisciplina(self):
        self.ctrlDisciplina.insereDisciplina()
    
    def mostraDisciplina(self):
        self.ctrlDisciplina.mostraDisciplina()
    
    def insereGrade(self):
        self.ctrlGrade.insereGrade()
    
    def mostraGrade(self):
        self.ctrlGrade.mostraGrade()
    
    def insereHistorico(self):
        self.ctrlHistorico.insereHistorico()
    
    def mostraHistorico(self):
        self.ctrlHistorico.mostraHistorico()
    
    def consultaHistorico(self):
        self.ctrlHistorico.consultaHistorico()

    def salvaDados(self):
        self.ctrlGrade.salvaGrade()
        self.ctrlAluno.salvaAluno()
        self.ctrlCurso.salvaCurso()
        self.ctrlDisciplina.salvaDisciplina()
        self.ctrlHistorico.salvaHistorico()
        self.root.destroy()
if __name__=='__main__':
    c=ControlePrincipal()
