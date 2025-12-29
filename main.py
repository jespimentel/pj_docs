import sys
import os

from datetime import datetime

from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                             QHeaderView, QDialog, QFileDialog)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery 

from ui.tela_principal import Ui_MainWindow
from ui.tela_cadastro import Ui_Dialog

from utils import gerar_titulo_e_resumo, exportar_relatorio 

# Classe da Janela de Cadastro de Procedimento
class DialogCadastroProcedimento(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cadastrar Novo Procedimento")
        self.setModal(True) # Impede interação com a tela principal enquanto aberta

        self.pushButton.clicked.connect(self.accept) # Fecha e retorna QDialog.Accepted
        
    def get_dados(self):
        numero = self.lineEdit.text()
        descricao = self.lineEdit_2.text()
        return numero, descricao

# Classe da Janela Principal
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PJ Docs")

        # Configuração do Banco de Dados 
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/pj_docs.db")

        if not self.db.open():
            QMessageBox.critical(self, "Erro", "Não foi possível abrir o banco de dados.")
            return

        # Configuração do Modelo e TableView
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("documentos")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        
        # Ocultar ID e ajustar colunas
        self.tableView.hideColumn(0)
        header = self.tableView.horizontalHeader()
        header.moveSection(4,0)  # Move a coluna 'procedimento' para a primeira posição
        header.moveSection(4,1)  # Move a coluna 'data_criacao' para a segunda posição
        header.setSectionResizeMode(2, QHeaderView.Stretch)  # Ajusta a coluna 'resumo' para preencher o espaço disponível 
        
        # Conexão do Botão de Cadastro
        self.pushButtonCadastrar.clicked.connect(self.abrir_janela_cadastro)

        # Inicializa os ComboBoxes
        self.atualizar_comboboxes()

        # Conexão do Botão de Carregar Arquivo
        self.pushButtonCarregarArquivo.clicked.connect(self.selecionar_arquivo)

        # Conexão do Botão de Gerar Resumo
        self.pushButtonGerarResumo.clicked.connect(self.processar_resumo)

        # Conexão do Botão de Salvar Registro
        self.pushButtonSalvarRegistro.clicked.connect(self.salvar_registro)

        # Filtragem por Procedimento
        self.comboBoxProcedimentoSelecionado.currentTextChanged.connect(self.filtrar_por_procedimento)

        # Conexão do Botão de Exportar Relatório
        self.pushButtonExportarRelatorio.clicked.connect(self.preparar_relatorio)

    def abrir_janela_cadastro(self):
        # 2. Instancia e exibe a janela de diálogo
        dialog = DialogCadastroProcedimento(self)
        
        if dialog.exec() == QDialog.Accepted:
            numero, descricao = dialog.get_dados()
            
            if not numero or not descricao:
                QMessageBox.warning(self, "Aviso", "Todos os campos são obrigatórios.")
                return

            # 3. Inserção no banco de dados
            query = QSqlQuery(self.db)
            query.prepare("INSERT INTO procedimentos (numero, descricao) VALUES (?, ?)")
            query.addBindValue(numero)
            query.addBindValue(descricao)

            if query.exec():
                QMessageBox.information(self, "Sucesso", "Procedimento cadastrado!")
                
                # --- Atualizações das comboboxes ---
                self.atualizar_comboboxes() 
                
                # Define o item recém-criado como o selecionado no combo de cadastro
                self.comboBoxProcedimentos.setCurrentText(numero)
                
            else:
                QMessageBox.critical(self, "Erro", f"Erro ao inserir: {query.lastError().text()}")

    def atualizar_comboboxes(self):
        # Preenche os ComboBoxes com os procedimentos do banco de dados
        self.comboBoxProcedimentos.clear()
        self.comboBoxProcedimentoSelecionado.clear()
        self.comboBoxProcedimentoSelecionado.addItem("Todos")

        query = QSqlQuery("SELECT numero FROM procedimentos ORDER BY numero ASC", self.db)
        while query.next():
            num = query.value(0)
            self.comboBoxProcedimentos.addItem(num)
            self.comboBoxProcedimentoSelecionado.addItem(num)

    def selecionar_arquivo(self):
        # Obtém o caminho da pasta inicial do usuário (Home)
        pasta_inicial = os.path.expanduser("~")

        # Filtro atualizado para aceitar apenas PDF, DOCX e TXT
        filtro = "Documentos (*.pdf *.docx *.txt)"

        # Abre a caixa de diálogo para seleção de um arquivo único
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Arquivo",
            pasta_inicial,
            filtro
        )

        if caminho_arquivo:
            # Armazena o caminho completo em uma variável para uso posterior
            self.caminho_arquivo_selecionado = caminho_arquivo

            # Altera o texto do botão para indicar que o arquivo foi carregado
            self.pushButtonCarregarArquivo.setText("Arquivo Carregado!")
            fonte = self.pushButtonCarregarArquivo.font()
            fonte.setBold(True)
            self.pushButtonCarregarArquivo.setFont(fonte)
            
            return self.caminho_arquivo_selecionado
        
        return None
    
    def processar_resumo(self):
        caminho_arquivo = getattr(self, 'caminho_arquivo_selecionado', None)
        if not caminho_arquivo:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo selecionado.")
            return

        titulo, resumo = gerar_titulo_e_resumo(caminho_arquivo)

        self.lineEditAssunto.setText(titulo)
        self.textEditResumo.setPlainText(resumo)

    def salvar_registro(self):
        titulo = self.lineEditAssunto.text()
        resumo = self.textEditResumo.toPlainText()
        procedimento = self.comboBoxProcedimentos.currentText()
        data_criacao = datetime.now().strftime("%Y-%m-%d")

        if not titulo or not resumo:
            QMessageBox.warning(self, "Aviso", "Assunto e Resumo são obrigatórios.")
            return

        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO documentos (titulo, resumo, procedimento, data_criacao) 
            VALUES (?, ?, ?, ?)
        """)
        query.addBindValue(titulo)
        query.addBindValue(resumo)
        query.addBindValue(procedimento if procedimento != "" else None)
        query.addBindValue(data_criacao)
        if query.exec():
            QMessageBox.information(self, "Sucesso", "Registro salvo com sucesso!")
            self.model.select()  # Atualiza a exibição da tabela
            # Limpa os campos após salvar
            self.lineEditAssunto.clear()
            self.textEditResumo.clear()

            # Reseta o botão de carregar arquivo
            self.pushButtonCarregarArquivo.setText("Carregar Arquivo")
            fonte = self.pushButtonCarregarArquivo.font()
            fonte.setBold(False)
            self.pushButtonCarregarArquivo.setFont(fonte) 

            # Limpa a variável do caminho para evitar reprocessar o mesmo arquivo por engano
            if hasattr(self, 'caminho_arquivo_selecionado'):
                del self.caminho_arquivo_selecionado  

        else:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar: {query.lastError().text()}")

    def filtrar_por_procedimento(self, texto):
        if texto == "Todos":
            self.model.setFilter("")  # Remove o filtro
        else:
            self.model.setFilter(f"procedimento = '{texto}'")
        self.model.select()  # Atualiza a exibição da tabela

    def preparar_relatorio(self):
        dados_para_relatorio = []
        
        # Percorre apenas as linhas que estão visíveis após o filtro
        for row in range(self.model.rowCount()):
            linha = {
                "procedimento": self.model.record(row).value("procedimento"),
                "data": self.model.record(row).value("data_criacao"),
                "titulo": self.model.record(row).value("titulo"),
                "resumo": self.model.record(row).value("resumo")
            }
            dados_para_relatorio.append(linha)

        if not dados_para_relatorio:
            QMessageBox.warning(self, "Aviso", "Não há dados para exportar com o filtro atual.")
            return

        # Chama a sua função utilitária (importada de utils)
        sucesso = exportar_relatorio(dados_para_relatorio)
        
        if sucesso:
            QMessageBox.information(self, "Sucesso", "Relatório gerado com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())