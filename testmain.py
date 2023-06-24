import sys

from disein import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MaWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MaWindow)
    MaWindow.show()
    sys.exit(app.exec_())
