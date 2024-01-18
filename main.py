import sys
from PyQt5.QtWidgets import (QLineEdit, QInputDialog)
import commands.comZteOLT
import gui
from PyQt5 import QtWidgets

connect = None


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_address = self.ui.ipAddressEdit.text  # IP адрес из строки ввода
        self.login = self.ui.loginEdit.text  # Ввод логина
        self.password = self.ui.passwordEdit.text  # ввод пароля

        self.ui.conectOLT.clicked.connect(self.connectOLT_GPON)  # подключение к OLT

    # Диалоговое окно с получением значения число
    def inputDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getInt(self, 'Number port', 'Номер порта ->')
        if ok:
            le.setText(str(text))
            return text

    # Диалоговое окно с получением значения строка
    def inputStrDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getText(self, 'Enter Macc', 'Введите Мак ->')
        if ok:
            le.setText(str(text))
            return text

    # Подключение к ОЛТ
    def connectOLT_GPON(self):
        if 0 < len(self.ip_address()):
            gPON = commands.comZteOLT.connectOLT_GPON(self.ip_address(), self.login(), self.password())
            self.ui.resultEdit_GPON_ZTE.setText(gPON)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Отключение от ОЛТ
    def shutdownOLT(self):
        zteGpon = commands.comZteOLT.shutdownOLT()
        self.ui.resultEdit_GPON_ZTE.setText(zteGpon)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
