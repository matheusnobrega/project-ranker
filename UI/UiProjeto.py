from tkinter import *
from Projeto import Projeto
from Periodo import Periodo
from DAO.ProjetoDAO import ProjetoDAO
import os

class UiProjeto:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("800x300+100+100")

        self.frame_tela_inicial = Frame(janela)
        self.frame_tela_inicial.grid()

        self.projeto_imagem = PhotoImage(file='C:\spiral-html\imagem_projeto.png')
        self.botao_projeto = Button(self.frame_tela_inicial, image=self.projeto_imagem, command=self.cria_projeto)
        self.botao_projeto.grid(row=1, column=1)

        self.projeto_unidade = PhotoImage(file='C:\spiral-html\imagem_unidade.png')
        self.botao_unidade = Button(self.frame_tela_inicial, image=self.projeto_unidade, command=self.cria_periodo)
        self.botao_unidade.grid(row=1, column=2)

        self.projeto_busca = PhotoImage(file='C:\spiral-html\imagem_busca.png')
        self.botao_busca = Button(self.frame_tela_inicial, image=self.projeto_busca, command=self.busca_projeto)
        self.botao_busca.grid(row=1, column=3)

        cabecalho = Label(self.frame_tela_inicial, text="Project Ranker")
        cabecalho.grid(row=2, column=1)

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

        projeto = Projeto
        projeto.salva_projeto(self.nome_projeto.get(),
                            self.descricao_projeto.get(),
                            'Segec', # trocar para objeto de unidade
                            self.qtd_pessoas_alocadas.get(),
                            self.data_inicio.get(),
                            self.data_termino.get(),
                            self.opcoes[self.var_criterio_impacto.get()],
                            self.opcoes[self.var_criterio_valor.get()],
                            self.opcoes[self.var_criterio_custo.get()],
                            self.opcoes[self.var_criterio_esforco.get()]
                            )

 #       projeto.calcula_nota()

    def busca_projeto(self):
        nova_janela = Toplevel(self.janela)
        nova_janela.geometry("1000x300+100+100")
        janela_cadastro = Frame(nova_janela)
        janela_cadastro.grid()

        projeto_dao = ProjetoDAO
        projetos = projeto_dao.busca_projeto()
        print(projetos)

        projeto_display = ''
        for projeto in projetos:
            projeto_display += str(projeto[0]) + ' ' + str(projeto[-1]) + '\n'

#        self.label_busca_projeto = Label(janela_cadastro, text=projeto_display)
#        self.label_busca_projeto.grid(row=1, column=1, columnspan=2)

        numero_linhas = len(projetos)
        numero_colunas = len(projetos[0])

        for i in range(numero_linhas):
            for j in range(numero_colunas):
                self.e = Entry(janela_cadastro, width=20, fg='black',
                               font=('Arial', 6, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, projetos[i][j])



    # Mudar para arquivo próprio
    ##################################################################################
    def cria_periodo(self):
        nova_janela = Toplevel(self.janela)
        nova_janela.geometry("600x300+100+100")
        janela_cadastro = Frame(nova_janela)
        janela_cadastro.grid()

        label_nome_periodo = Label(janela_cadastro, text="Nome do Período")
        label_nome_periodo.grid(row=1, column=1)
        self.nome_periodo = Entry(janela_cadastro)
        self.nome_periodo.grid(row=1, column=2)

        label_data_inicio = Label(janela_cadastro, text="Data de inicio")
        label_data_inicio.grid(row=2, column=1)
        self.data_inicio_periodo = Entry(janela_cadastro)
        self.data_inicio_periodo.grid(row=2, column=2)

        label_data_termino = Label(janela_cadastro, text="Data de termino")
        label_data_termino.grid(row=3, column=1)
        self.data_termino_periodo = Entry(janela_cadastro)
        self.data_termino_periodo.grid(row=3, column=2)

        label_orcamento = Label(janela_cadastro, text="Orcamento")
        label_orcamento.grid(row=4, column=1)
        self.orcamento = Entry(janela_cadastro)
        self.orcamento.grid(row=4, column=2)

        salva_periodo = Button(janela_cadastro, text="Salvar", command=self.salva_periodo_botao)
        salva_periodo.grid(row=5, column=1)

    def salva_periodo_botao(self):
        print(self.nome_periodo.get())
        print(self.data_inicio_periodo.get())
        print(self.data_termino_periodo.get())
        print(self.orcamento.get())

        periodo = Periodo
        periodo.salva_periodo(self.nome_periodo.get(),
                              self.data_inicio_periodo.get(),
                              self.data_termino_periodo.get(),
                              self.orcamento.get()
                              )



