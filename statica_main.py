from PyQt5 import QtWidgets, QtGui
import MainWindow
import DescriptiveTable
import sys
import Data

def main():
	#print(Data.df)
	print(Data.desc_df)
	app = QtWidgets.QApplication([])
	app.setWindowIcon(QtGui.QIcon('logo.jpg'))

	application = MainWindow.App()
	application.show()

	desc_widget = QtWidgets.QWidget([])

	dest_table = DescriptiveTable.Desc_table()
	dest_table.show()

	sys.exit(desc_widget.exec())
	sys.exit(app.exec())
	

if __name__ == "__main__":
	main()
else:
	print("No")