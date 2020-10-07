from PyQt5 import QtWidgets, QtGui
import Data
import sys

# Настройки главного окна программы, сгенерированные PyQt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(-5, 1, 651, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
# Пользовательские настройки
class Desc_table(QtWidgets.QFormLayout):
	def __init__(self):
	    # super(Desc_table, self).__init__()
	    self.ui = Ui_Form()
	    self.ui.setupUi(self)

	    self.ui.tableWidget.setColumnCount(Data.desc_df.shape[1])
	    self.ui.tableWidget.setRowCount(Data.desc_df.shape[0])

	    for row in range(len(Data.desc_df)):
	    	col = 0

	    	for item in Data.desc_df.iloc[row, :]:
	    		cellinfo = QtWidgets.QTableWidgetItem(str(item))
	    		self.ui.tableWidget.setItem(row, col, cellinfo)
	    		col += 1