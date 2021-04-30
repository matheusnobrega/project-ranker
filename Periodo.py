class Periodo:

    def __init__(self, nome, data_inicio, data_termino, orcamento):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.orcamento = orcamento

    def __str__(self):
        return f'O período {self.nome} tem inicio no dia {self.data_inicio} ' \
               f'e término no dia {self.data_termino}'