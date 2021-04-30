from Periodo import Periodo
from Projeto import Projeto
from Unidade import Unidade

projeto = Projeto('Projeto1', 'Descrição', 'Segec', '12/07/2021', '12/08/2021',
                  21, 5, 5, 5, 5)
projeto.calcula_nota()
print(projeto)

periodo = Periodo('2020', '02/01/2021', '02/10/2021', 1500)
print(periodo)