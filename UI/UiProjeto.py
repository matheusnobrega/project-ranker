from tkinter import *
from Projeto import Projeto
import os

class UiProjeto:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("800x300+100+100")

        self.frame_tela_inicial = Frame(janela)
        self.frame_tela_inicial.pack()

        self.projeto_imagem = PhotoImage(file='C:\spiral-html\imagem_projeto.png')
        self.bt = Button(self.frame_tela_inicial, image=self.projeto_imagem, command=self.cria_projeto)
        self.bt.pack(side=LEFT)

        self.projeto_unidade = PhotoImage(file='C:\spiral-html\imagem_unidade.png')
        self.bt = Button(self.frame_tela_inicial, image=self.projeto_unidade, command=self.cria_projeto)
        self.bt.pack(side=LEFT)

        self.projeto_busca = PhotoImage(file='C:\spiral-html\imagem_busca.png')
        self.bt = Button(self.frame_tela_inicial, image=self.projeto_busca, command=self.cria_projeto)
        self.bt.pack(side=LEFT)


    def cria_projeto(self):
        nova_janela = Toplevel(self.janela)
        nova_janela.geometry("600x300+100+100")
        janela_cadastro = Frame(nova_janela)
        janela_cadastro.grid()

        self.opcoes = {
            "Muito baixa(o)":1,
            "Baixa(o)":2,
            "Média(o)":3,
            "Alta(o)":4,
            "Muito alta(o)":5
        }

        label_nome_projeto = Label(janela_cadastro, text="Nome do projeto")
        label_nome_projeto.grid(row=1, column=1)
        self.nome_projeto = Entry(janela_cadastro)
        self.nome_projeto.grid(row=1, column=2)

        label_descricao_projeto = Label(janela_cadastro, text="Descrição do projeto")
        label_descricao_projeto.grid(row=2, column=1)
        self.descricao_projeto = Entry(janela_cadastro)
        self.descricao_projeto.grid(row=2, column=2)

        label_data_inicio = Label(janela_cadastro, text="Data de Início do projeto")
        label_data_inicio.grid(row=3, column=1)
        self.data_inicio = Entry(janela_cadastro)
        self.data_inicio.grid(row=3, column=2)

        label_data_termino = Label(janela_cadastro, text="Data de Término do projeto")
        label_data_termino.grid(row=4, column=1)
        self.data_termino = Entry(janela_cadastro)
        self.data_termino.grid(row=4, column=2)

        label_qtd_pessoas_alocadas = Label(janela_cadastro, text="Quantidade de pessoas alocadas")
        label_qtd_pessoas_alocadas.grid(row=5, column=1)
        self.qtd_pessoas_alocadas = Entry(janela_cadastro)
        self.qtd_pessoas_alocadas.grid(row=5, column=2)

        label_criterio_impacto = Label(janela_cadastro, text="Qual é o grau do impacto que o projeto retornará?")
        label_criterio_impacto.grid(row=6, column=1)
        self.var_criterio_impacto = StringVar(janela_cadastro)
        self.criterio_impacto = OptionMenu(janela_cadastro, self.var_criterio_impacto, *self.opcoes.keys())
        self.criterio_impacto.grid(row=6, column=2)

        label_criterio_valor = Label(janela_cadastro, text="Qual é o grau do valor que o projeto retornará?")
        label_criterio_valor.grid(row=7, column=1)
        self.var_criterio_valor = StringVar(janela_cadastro)
        self.criterio_valor = OptionMenu(janela_cadastro, self.var_criterio_valor, *self.opcoes.keys())
        self.criterio_valor.grid(row=7, column=2)

        label_criterio_custo = Label(janela_cadastro, text="Qual é o custo do projeto?")
        label_criterio_custo.grid(row=8, column=1)
        self.var_criterio_custo = StringVar(janela_cadastro)
        self.criterio_custo = OptionMenu(janela_cadastro, self.var_criterio_custo, *self.opcoes.keys())
        self.criterio_custo.grid(row=8, column=2)

        label_criterio_esforco = Label(janela_cadastro, text="Qual é o grau do esforço que o projeto requisita?")
        label_criterio_esforco.grid(row=9, column=1)
        self.var_criterio_esforco = StringVar(janela_cadastro)
        self.criterio_esforco = OptionMenu(janela_cadastro, self.var_criterio_esforco, *self.opcoes.keys())
        self.criterio_esforco.grid(row=9, column=2)

        label_situacao = Label(janela_cadastro, text="Situação")
        label_situacao.grid(row=10, column=1)
        self.situacao = Label(janela_cadastro, text="Aguardando priorização")
        self.situacao.grid(row=10, column=2)

        salva_projeto = Button(janela_cadastro, text="Salvar", command=self.salva_projeto_botao)
        salva_projeto.grid(row=11, column=1)

    def salva_projeto_botao(self):
        print(self.nome_projeto.get())
        print(self.descricao_projeto.get())
        print(self.data_inicio.get())
        print(self.data_termino.get())
        print(self.opcoes[self.var_criterio_esforco.get()])

        projeto = Projeto(self.nome_projeto.get(),
                          self.descricao_projeto.get(),
                          'Segec', # trocar para objeto de unidade
                          self.qtd_pessoas_alocadas.get(),
                          self.data_inicio.get(),
                          self.data_termino.get(),
                          self.opcoes[self.var_criterio_impacto.get()],
                          self.opcoes[self.var_criterio_valor.get()],
                          self.opcoes[self.var_criterio_custo.get()],
                          self.opcoes[self.var_criterio_esforco.get()])

        projeto.calcula_nota()





