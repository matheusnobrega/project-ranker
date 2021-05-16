from DTO.PeriodoDTO import PeriodoDTO
from DAO.PeriodoDAO import PeriodoDAO

class Periodo:

    def salva_periodo(nome, data_inicio, data_termino, orcamento):
        periodo_dto = PeriodoDTO
        periodo_dto.nome = nome
        periodo_dto.data_inicio = data_inicio
        periodo_dto.data_termino = data_termino
        periodo_dto.orcamento = orcamento

        periodo_dao = PeriodoDAO()
        periodo_dao.salva_periodo(periodo_dto)

    def __str__(self):
        return f'O período {self.nome} tem inicio no dia {self.data_inicio} ' \
               f'e término no dia {self.data_termino}'