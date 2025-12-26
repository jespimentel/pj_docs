import sqlite3

def criar_banco():
    nome_banco = "data\\pj_docs.db"
    
    sql_script = """
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;

    -- Table: documentos
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        titulo TEXT NOT NULL, 
        resumo TEXT, 
        data_criacao TEXT DEFAULT CURRENT_TIMESTAMP, 
        procedimento TEXT REFERENCES procedimentos (numero) ON DELETE SET NULL
    );

    -- Table: procedimentos
    CREATE TABLE IF NOT EXISTS procedimentos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        numero TEXT NOT NULL UNIQUE, 
        descricao TEXT
    );

    COMMIT TRANSACTION;
    PRAGMA foreign_keys = on;
    """

    try:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
        
        cursor.executescript(sql_script) # executescript para múltiplas instruções SQL
        conn.commit()
        
        print(f"Banco de dados '{nome_banco}' e tabelas criados com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
        
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_banco()