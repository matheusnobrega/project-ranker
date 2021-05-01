class Unidade:

    def __init__(self, sigla, nome_completo, setor, qtd_pessoas_alocadas):
        self._sigla = sigla
        self._nome_completo = nome_completo
        self._setor = setor
        self._qtd_pessoas_alocadas = qtd_pessoas_alocadas

    def __str__(self):
        return f'A unidade {self._sigla} possui {self._qtd_pessoas_alocadas} ' \
               f'pessoas alocadas'

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, sigla):
        self._sigla = sigla

    @property
    def qtd_pessoas_alocadas(self):
        return self._qtd_pessoas_alocadas