class Unidade:

    def __init__(self, sigla, nome_completo, setor, qtd_pessoas_alocadas):
        self.sigla = sigla
        self.nome_completo = nome_completo
        self.setor = setor
        self.qtd_pessoas_alocadas = qtd_pessoas_alocadas

    def __str__(self):
        return f'A unidade {self.sigla} possui {self.qtd_pessoas_alocadas} ' \
               f'pessoas alocadas'
