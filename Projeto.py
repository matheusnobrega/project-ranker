class Projeto:

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

    def __str__(self):
        return f'O projeto {self.nome} tem inicio no dia {self.data_inicio} ' \
               f'e término no dia {self.data_termino} com {self.qtd_pessoas_alocadas}' \
               f' pessoas alocadas'

    def calcula_nota(self):
        nota = (self.criterio_custo + self.criterio_valor + \
               self.criterio_esforco + self.criterio_impacto)*100/20

        self.nota = nota
        print(nota)




