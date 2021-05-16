import sqlite3

class PeriodoDAO:
    def salva_periodo(self, periodo):
        database = sqlite3.connect('C:\spiral-html\ProjectRankerDB.db')
        cursor = database.cursor()

        cursor.execute("""INSERT INTO periodo VALUES (?,?,?,?)""",
                                      (periodo.nome,
                                      periodo.data_inicio,
                                      periodo.data_termino,
                                      periodo.orcamento)
                       )

        database.commit()
        database.close()