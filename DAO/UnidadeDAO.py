import sqlite3

class UnidadeDAO():


    def salva_unidade(self, periodo):
        database = sqlite3.connect('C:\spiral-html\ProjectRankerDB.db')
        cursor = database.cursor()

        cursor.execute("""
                        INSERT INTO unidade VALUES (?,?,?,?)
                        """ , ( periodo.sigla,
                                periodo.nome_completo,
                                periodo.setor,
                                periodo.qtd_pessoas_alocadas)
                       )

        database.commit()
        database.close()