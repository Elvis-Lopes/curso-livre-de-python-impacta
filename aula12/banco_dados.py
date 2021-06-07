import sqlite3

conn = sqlite3.connect("galeria.db")

cursor = conn.cursor()

def criar_tabela():
    sql = """
    CREATE TABLE albuns(titulo text, artista text, data_lacamento text, data_publicacao text, midia text)
    """

    cursor.execute(sql)
    conn.commit()