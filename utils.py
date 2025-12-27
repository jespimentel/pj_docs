import sqlite3
from datetime import datetime
from docx import Document


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


def gerar_resumo(caminho_arquivo):
    return f"Título gerado por IA a partir de {caminho_arquivo}", f"Resumo gerado por IA a partir de {caminho_arquivo}"

from docx import Document
from datetime import datetime

from docx import Document
from datetime import datetime

def exportar_relatorio(lista_dados):
    try:
        doc = Document()
        doc.add_heading('PJ Docs', 0)

        # 1. Agrupamento por procedimento
        agrupados = {}
        for item in lista_dados:
            proc = item['procedimento']
            if proc not in agrupados:
                agrupados[proc] = []
            agrupados[proc].append(item)

        # 2. Construção da hierarquia no documento
        for procedimento, documentos in agrupados.items():
            doc.add_heading(f"Procedimento: {procedimento}", level=1)
            doc.add_paragraph("")  
            
            for doc_info in documentos:
                # --- DATA DO CADASTRO ---
                p_data = doc.add_paragraph()
                p_data.add_run('Data: ').bold = True
                
                data_original = doc_info['data']
                try:
                    data_formatada = datetime.strptime(data_original, "%Y-%m-%d").strftime("%d/%m/%Y")
                except Exception:
                    data_formatada = data_original

                p_data.add_run(data_formatada)

                # --- TÍTULO DO DOCUMENTO ---
                p_titulo = doc.add_paragraph()
                p_titulo.add_run('Título: ').bold = True
                p_titulo.add_run(doc_info['titulo'])
                
                # --- RESUMO ---
                p_resumo = doc.add_paragraph()
                p_resumo.add_run('Resumo: ').bold = True
                p_resumo.add_run(doc_info['resumo'])
                
                # Espaço entre documentos do mesmo procedimento
                doc.add_paragraph("") 
                
            # Separador de procedimentos (fora do loop de documentos)
            doc.add_paragraph("________________________________________________")

        doc.save("relatorio_pj_docs.docx")
        return True
    except Exception as e:
        print(f"Erro ao gerar docx: {e}")
        return False

if __name__ == "__main__":
    criar_banco()