import sqlite3


class Database:
    def conexao_db(self):
        database = sqlite3.connect('ProjectRankerDB.db')
#       cursor = database.cursor()
        return database