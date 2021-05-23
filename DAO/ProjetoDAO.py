import sqlite3
from Database.Database import Database

class ProjetoDAO:


    def salva_projeto(self, projeto):
        database = sqlite3.connect('C:\spiral-html\ProjectRankerDB.db')
        cursor = database.cursor()

        cursor.execute("""
                        INSERT INTO projeto VALUES (?,?,?,?,?,?,?,?,?,?,?)
                        """, (  projeto.nome,
                                projeto.descricao,
                                projeto.data_inicio,
                                projeto.data_termino,
                                projeto.qtd_pessoas_alocadas,
                                projeto.criterio_impacto,
                                projeto.criterio_valor,
                                projeto.criterio_custo,
                                projeto.criterio_esforco,
                                projeto.situacao,
                                projeto.nota)
                       )

        database.commit()
        database.close()

    @classmethod
    def busca_projeto(cls):
        db = sqlite3.connect('C:\spiral-html\ProjectRankerDB.db')

        cursor = db.cursor()

        cursor.execute("""SELECT oid, 
                                 nome, 
                                 data_inicio, 
                                 data_termino,
                                 IFNULL(nota, 0) nota
                          FROM   projeto""")
        query = cursor.fetchall()

        return query


        
