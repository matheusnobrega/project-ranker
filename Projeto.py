from DTO.ProjetoDTO import ProjetoDTO
from DAO.ProjetoDAO import ProjetoDAO

class Projeto:

    projetos = []
    def salva_projeto(nome, descricao, unidade_responsavel, data_inicio,
                    data_termino, qtd_pessoas_alocadas, criterio_impacto, criterio_valor,
                    criterio_custo, criterio_esforco):
        projeto_dto = ProjetoDTO
        projeto_dto.nome = nome
        projeto_dto.descricao = descricao
        projeto_dto.unidade_responsavel = unidade_responsavel
        projeto_dto.data_inicio = data_inicio
        projeto_dto.data_termino = data_termino
        projeto_dto.qtd_pessoas_alocadas = qtd_pessoas_alocadas
        projeto_dto.criterio_impacto = criterio_impacto
        projeto_dto.criterio_valor = criterio_valor
        projeto_dto.criterio_custo = criterio_custo
        projeto_dto.criterio_esforco = criterio_esforco
        projeto_dto.situacao = 'Aguardando priorização'
        projeto_dto.nota = (criterio_esforco + criterio_impacto +
                            criterio_valor + criterio_custo)*100/20
#        self.__class__.projetos.append(self)

        projeto_dao = ProjetoDAO()
        projeto_dao.salva_projeto(projeto_dto)

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
        self.nota = (self.criterio_custo + self.criterio_valor + \
               self.criterio_esforco + self.criterio_impacto)*100/20


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





