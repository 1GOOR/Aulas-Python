import sqlite3 as sq

class DAOUsuario:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def conectar(self):
        """
        Esse metodo serve para criar uma conexão com o bando de dados
        :return: conn, cursor
        """
        self.conn = sq.connect("ControleEscola.db")
        self.cursor = self.conn.cursor()

        return self.conn, self.cursor
    def criarTabelaUsuario(self):

        conn,cursor = self.conectar()

        cursor.execute("""
        CREATE TABLE usuarios(
        
        id int primary key autoincrement;
        
        
        )
        """)

