from Periodo import Periodo
from Projeto import Projeto
from Unidade import Unidade

unidade = Unidade('Segec', 'Setor de gremiações concorrentes', 'gremiações', 54)

projeto = Projeto('Projeto1', 'Descrição', unidade, '12/07/2021', '12/08/2021',
                  21, 5, 5, 5, 1)
projeto1 = Projeto('Projeto2', 'Descrição', unidade, '12/07/2021', '12/08/2021',
                  21, 5, 4, 2, 1)

projeto2 = Projeto.gera_ranking()
projeto.calcula_nota()
print(projeto)

Projeto.gera_ranking()

periodo = Periodo('2020', '02/01/2021', '02/10/2021', 1500)
print(periodo)