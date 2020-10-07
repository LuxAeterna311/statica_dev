from PyQt5 import QtCore, QtGui, QtWidgets
from DescriptiveTable import Ui_Form
import Data
import sys


# Настройки главного окна программы, сгенерированные PyQt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 1, 521, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(540, 0, 101, 41))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 40, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Statica"))
        self.pushButton.setText(_translate("MainWindow", "Очистить таблицу"))
        self.toolButton.setText(_translate("MainWindow", "Инструменты"))
        self.pushButton_2.setText(_translate("MainWindow", "Описательная"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.action_2.setText(_translate("MainWindow", "Загрузить таблицу"))
        self.action_3.setText(_translate("MainWindow", "Сохранить таблицу"))
        self.action.setText(_translate("MainWindow", "Создать новую таблицу"))


# Пользовательские настройки
class App(QtWidgets.QMainWindow):
	def __init__(self):
	    super(App, self).__init__()
	    self.ui = Ui_MainWindow()
	    self.ui.setupUi(self)

	 	# Задаёт размер таблицы
	    self.ui.tableWidget.setColumnCount(Data.df.shape[1])
	    self.ui.tableWidget.setRowCount(Data.df.shape[0])
	 
	    # Очистка таблицы при клике на кнопку.
	    self.ui.pushButton.clicked.connect(self.clear)

	    # Заполнение значений
	    for row in range(len(Data.df)):
	    	col = 0

	    	for item in Data.df.iloc[row, :]:
	    		cellinfo = QtWidgets.QTableWidgetItem(str(item))
	    		self.ui.tableWidget.setItem(row, col, cellinfo)
	    		col += 1

	    self.ui.pushButton_2.clicked.connect(self.desc_stats)

	    self.ui.tableWidget.setHorizontalHeaderLabels(Data.df.columns)

	# Слот, очищающий таблицу
	def clear(self):
		self.ui.tableWidget.clear()
		self.ui.tableWidget.setColumnCount(10)
		self.ui.tableWidget.setRowCount(10)

	# Слот, создающий описательную таблицу
	def desc_stats(self):
		app = QtWidgets.QApplication(sys.argv)
		Form = QtWidgets.QWidget()
		ui = Ui_Form()
		ui.setupUi(Form)


		Form.ui.tableWidget.setColumnCount(Data.desc_df.shape[1])
		Form.ui.tableWidget.setRowCount(Data.desc_df.shape[0])

		for row in range(len(Data.desc_df)):
			col = 0

			for item in Data.desc_df.iloc[row, :]:
				cellinfo = QtWidgets.QTableWidgetItem(str(item))
				self.ui.tableWidget.setItem(row, col, cellinfo)
				col += 1

		Form.show()
		sys.exit(app.exec_())