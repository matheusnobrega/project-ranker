from tkinter import *
from Projeto import Projeto

class UiProjeto:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("300x300+100+100")

        self.frame_tela_inicial = Frame(janela)
        self.frame_tela_inicial.pack()

        self.ed = Entry(self.frame_tela_inicial)
        self.ed.pack(side=LEFT)

        self.bt = Button(self.frame_tela_inicial, width=20, text='ola', command=self.cria_projeto)
        self.bt.pack(side=LEFT)

        self.lb = Label(self.frame_tela_inicial, text="Label")
        self.lb.pack(side=LEFT)

       # self.bt.destroy()


    def cria_projeto(self):
        nova_janela = Toplevel(self.janela)
        nova_janela.geometry("300x300+100+100")
        janela_cadastro = Frame(nova_janela)
        janela_cadastro.pack()

        label_nome_projeto = Label(janela_cadastro, text="Nome do projeto")
        label_nome_projeto.pack(side=TOP)
        self.nome_projeto = Entry(janela_cadastro)
        self.nome_projeto.pack(side=TOP)

        label_descricao_projeto = Label(janela_cadastro, text="Descrição do projeto")
        label_descricao_projeto.pack(side=TOP)
        self.descricao_projeto = Entry(janela_cadastro)
        self.descricao_projeto.pack(side=TOP)

        label_data_inicio = Label(janela_cadastro, text="Data de Início do projeto")
        label_data_inicio.pack(side=TOP)
        self.data_inicio = Entry(janela_cadastro)
        self.data_inicio.pack(side=TOP)

        label_data_termino = Label(janela_cadastro, text="Data de Término do projeto")
        label_data_termino.pack(side=TOP)
        self.data_termino = Entry(janela_cadastro)
        self.data_termino.pack(side=TOP)

        label_qtd_pessoas_alocadas = Label(janela_cadastro, text="Quantidade de pessoas alocadas")
        label_qtd_pessoas_alocadas.pack(side=TOP)
        self.qtd_pessoas_alocadas = Entry(janela_cadastro)
        self.qtd_pessoas_alocadas.pack(side=TOP)

        label_criterio_impacto = Label(janela_cadastro, text="Qual é o grau do impacto que o projeto retornará?")
        label_criterio_impacto.pack(side=TOP)
        self.criterio_impacto = Listbox(janela_cadastro)
        self.criterio_impacto.insert(1, "Muito baixa")
        self.criterio_impacto.insert(2, "Baixa")
        self.criterio_impacto.insert(3, "Média")
        self.criterio_impacto.insert(4, "Alta")
        self.criterio_impacto.insert(5, "Muito alta")
        self.criterio_impacto.pack(side=LEFT)

        label_criterio_valor = Label(janela_cadastro, text="Qual é o grau do valor que o projeto retornará?")
        label_criterio_valor.pack(side=TOP)
        self.criterio_valor = Listbox(janela_cadastro)
        self.criterio_valor.insert(1, "Muito baixa")
        self.criterio_valor.insert(2, "Baixa")
        self.criterio_valor.insert(3, "Média")
        self.criterio_valor.insert(4, "Alta")
        self.criterio_valor.insert(5, "Muito alta")
        self.criterio_valor.pack(side=LEFT)

        label_criterio_custo = Label(janela_cadastro, text="Qual é o custo do projeto?")
        label_criterio_custo.pack(side=TOP)
        self.criterio_custo = Listbox(janela_cadastro)
        self.criterio_custo.insert(1, "Muito baixa")
        self.criterio_custo.insert(2, "Baixa")
        self.criterio_custo.insert(3, "Média")
        self.criterio_custo.insert(4, "Alta")
        self.criterio_custo.insert(5, "Muito alta")
        self.criterio_custo.pack(side=LEFT)

        label_criterio_esforco = Label(janela_cadastro, text="Qual é o grau do esforço que o projeto requisita?")
        label_criterio_esforco.pack(side=TOP)
        self.criterio_esforco = Listbox(janela_cadastro)
        self.criterio_esforco.insert(1, "Muito baixa")
        self.criterio_esforco.insert(2, "Baixa")
        self.criterio_esforco.insert(3, "Média")
        self.criterio_esforco.insert(4, "Alta")
        self.criterio_esforco.insert(5, "Muito alta")
        self.criterio_esforco.pack(side=LEFT)

        label_situacao = Label(janela_cadastro, text="Situação")
        label_situacao.pack(side=TOP)
        self.situacao = Label(janela_cadastro, text="Aguardando situação")
        self.situacao.pack(side=LEFT)

        salva_projeto = Button(janela_cadastro, text="Salvar", command=self.salva_projeto_botao)
        salva_projeto.pack(side=TOP)

    def salva_projeto_botao(self):
        print(self.nome_projeto.get())
        print(self.descricao_projeto.get())
        print(self.data_inicio.get())
        print(self.data_termino.get())
        #print(self.criterio_impacto.get())





