class Projeto:

    projetos = []
    def __init__(self, nome, descricao, unidade_responsavel, data_inicio,
                 data_termino, qtd_pessoas_alocadas, criterio_impacto, criterio_valor,
                 criterio_custo, criterio_esforco):
        self.nome = nome
        self.descricao = descricao
        self.unidade_responsavel = unidade_responsavel
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.qtd_pessoas_alocadas = qtd_pessoas_alocadas
        self.criterio_impacto = criterio_impacto
        self.criterio_valor = criterio_valor
        self.criterio_custo = criterio_custo
        self.criterio_esforco = criterio_esforco
        self.situacao = 'Aguardando priorização'
        self.__class__.projetos.append(self)

    def __str__(self):
        return f'O projeto {self.nome} tem inicio no dia {self.data_inicio} ' \
               f'e término no dia {self.data_termino} com {self.qtd_pessoas_alocadas}' \
               f' pessoas alocadas'

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, situacao):
        self._situacao = situacao



    def calcula_nota(self):
        nota = (self.criterio_custo + self.criterio_valor + \
               self.criterio_esforco + self.criterio_impacto)*100/20
        self.nota = nota
        #print(nota)

#    def gera_ranking(self):
#        print(self.unidade_responsavel.qtd_pessoas_alocadas)

    @classmethod
    def gera_ranking(cls):
        for p in range(len(cls.projetos)):
            atual = cls.projetos[p].nota

            while p > 0 and cls.projetos[p - 1].nota < atual:
                cls.projetos[p].nota = cls.projetos[p - 1].nota
                p -= 1

            cls.projetos[p].nota = atual

        qtd_pessoas_unidade = cls.projetos[0].unidade_responsavel.qtd_pessoas_alocadas
        for projeto in cls.projetos:
            qtd_pessoas_unidade = qtd_pessoas_unidade - projeto.qtd_pessoas_alocadas
            if qtd_pessoas_unidade >= 0:
                print("Priorizado")
                projeto.situacao = 'Priorizado'
            else:
                projeto.situacao = 'Nao priorizado'
                print("Nao priorizado")

            print(projeto.nota)





