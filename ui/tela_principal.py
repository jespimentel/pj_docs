# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 611))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 731, 171))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 691, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBoxProcedimentos = QComboBox(self.layoutWidget)
        self.comboBoxProcedimentos.setObjectName(u"comboBoxProcedimentos")

        self.horizontalLayout.addWidget(self.comboBoxProcedimentos)

        self.pushButtonCadastrar = QPushButton(self.layoutWidget)
        self.pushButtonCadastrar.setObjectName(u"pushButtonCadastrar")

        self.horizontalLayout.addWidget(self.pushButtonCadastrar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonCarregarArquivo = QPushButton(self.layoutWidget)
        self.pushButtonCarregarArquivo.setObjectName(u"pushButtonCarregarArquivo")

        self.horizontalLayout_2.addWidget(self.pushButtonCarregarArquivo)

        self.pushButtonGerarResumo = QPushButton(self.layoutWidget)
        self.pushButtonGerarResumo.setObjectName(u"pushButtonGerarResumo")

        self.horizontalLayout_2.addWidget(self.pushButtonGerarResumo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 171, 20))
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 190, 731, 291))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEditAssunto = QLineEdit(self.widget)
        self.lineEditAssunto.setObjectName(u"lineEditAssunto")

        self.verticalLayout_2.addWidget(self.lineEditAssunto)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textEditResumo = QTextEdit(self.widget)
        self.textEditResumo.setObjectName(u"textEditResumo")

        self.verticalLayout_2.addWidget(self.textEditResumo)

        self.pushButtonSalvarRegistro = QPushButton(self.tab)
        self.pushButtonSalvarRegistro.setObjectName(u"pushButtonSalvarRegistro")
        self.pushButtonSalvarRegistro.setGeometry(QRect(40, 490, 171, 23))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 540, 111, 20))
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(690, 0, 71, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.widget_3 = QWidget(self.tab_1)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(40, 30, 721, 101))
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 141, 16))
        self.layoutWidget1 = QWidget(self.widget_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 671, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBoxProcedimentoSelecionado = QComboBox(self.layoutWidget1)
        self.comboBoxProcedimentoSelecionado.setObjectName(u"comboBoxProcedimentoSelecionado")

        self.horizontalLayout_6.addWidget(self.comboBoxProcedimentoSelecionado)

        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.widget_4 = QWidget(self.tab_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(40, 140, 721, 421))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView = QTableView(self.widget_4)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_5.addWidget(self.tableView)

        self.pushButtonExportarRelatorio = QPushButton(self.widget_4)
        self.pushButtonExportarRelatorio.setObjectName(u"pushButtonExportarRelatorio")

        self.verticalLayout_5.addWidget(self.pushButtonExportarRelatorio)

        self.tabWidget.addTab(self.tab_1, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButtonCarregarArquivo.setText(QCoreApplication.translate("MainWindow", u"Carregar Arquivo", None))
        self.pushButtonGerarResumo.setText(QCoreApplication.translate("MainWindow", u"Gerar Resumo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Procedimento:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Assunto:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resumo", None))
        self.pushButtonSalvarRegistro.setText(QCoreApplication.translate("MainWindow", u"Salvar Registro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pimentel - 2025", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PJDocs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selecione o procedimento:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.pushButtonExportarRelatorio.setText(QCoreApplication.translate("MainWindow", u"Exportar Relat\u00f3rio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
    # retranslateUi

