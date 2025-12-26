import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel 
from ui.tela_principal import Ui_MainWindow 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #---------------------------------------------------------
        # Preencher a tableView com dados do banco de dados SQLite
        #---------------------------------------------------------
        # 1. Conexão com o banco de dados
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/pj_docs.db")

        if not self.db.open():
            QMessageBox.critical(self, "Erro", "Não foi possível abrir o banco de dados.")
            return

        # 2. Configuração do Modelo SQL
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("documentos") # Tabela a ser exibida
        
        # 3. Definição da estratégia de edição
        # OnFieldChange: Salva no banco assim que você sai da célula editada
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        
        self.model.select() # Carrega os dados

        # 4. Conexão do modelo à tableView
        self.tableView.setModel(self.model)

        # 5. Ordem e seleção das colunas
        self.tableView.hideColumn(0)  # Oculta a coluna ID

        header = self.tableView.horizontalHeader()
        header.moveSection(4,0)  # Move a coluna 'procedimento' para a primeira posição
        header.moveSection(4,1)  # Move a coluna 'data_criacao' para a segunda posição
        header.setSectionResizeMode(2, QHeaderView.Stretch)  # Ajusta a coluna 'resumo' para preencher o espaço disponível 

        # ---------------------------------------------------------
        # Preencher o comboBox com procedimentos do banco de dados
        # ---------------------------------------------------------
        self.comboBoxProcedimentos.clear()
        query = self.db.exec("SELECT numero FROM procedimentos ORDER BY numero ASC")
        while query.next():
            numero = query.value(0)
            self.comboBoxProcedimentos.addItem(numero)

        #---------------------------------------------------------
        # Preencher o combobox do procedimento selecionado no cadastro
        #---------------------------------------------------------
        self.comboBoxProcedimentoSelecionado.clear()
        query = self.db.exec("SELECT numero FROM procedimentos ORDER BY numero ASC")
        self.comboBoxProcedimentoSelecionado.addItem("Todos")
        while query.next():
            numero = query.value(0)
            self.comboBoxProcedimentoSelecionado.addItem(numero)

        #Continuar a partir daqui

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())