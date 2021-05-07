from tkinter import *
from Periodo import Periodo
from Projeto import Projeto
from Unidade import Unidade
from DAO.ProjetoDAO import ProjetoDAO
from UI.UiProjeto import UiProjeto


#def on_click():
#    print(ed.get())
#    lb["text"] = ed.get()



janela = Tk()

ui = UiProjeto(janela)
janela.mainloop()

#unidade = Unidade('Segec', 'Setor de gremiações concorrentes', 'gremiações', 54)

#projeto = Projeto('Projeto1', 'Descrição', unidade, '12/07/2021', '12/08/2021',
#                  21, 5, 5, 5, 1)
#projeto1 = Projeto('Projeto2', 'Descrição', unidade, '12/07/2021', '12/08/2021',
#                  21, 5, 4, 2, 1)
#projeto3 = Projeto('Projeto3', 'Descrição', unidade, '12/07/2021', '12/08/2021',
#                  21, 5, 4, 3, 1)

projetodao = ProjetoDAO()

#projetodao.cadastra_projeto(projeto)


#projeto.calcula_nota()
#projeto1.calcula_nota()
#projeto3.calcula_nota()


#Projeto.gera_ranking()

#periodo = Periodo('2020', '02/01/2021', '02/10/2021', 1500)
