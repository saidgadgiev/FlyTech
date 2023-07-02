import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
import disein
import switchboard_command

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.ui = disein.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_address = self.ui.ipAddressEdit.text  # IP адресс из строки ввода
        # self.ui.connectBTN.clicked.connect(self.connectSwichbord)  # Подключение к комм
        self.ui.interfBTN.clicked.connect(self.switchbord_interf)  # кнопка просмотр портов
        self.ui.listMacBTN.clicked.connect(self.listMac)  # Кнопка список маков
        # self.ui.serchMacBTN.clicked.connect()  # кнопка поиск по маку
        self.ui.listVlanBTN.clicked.connect(self.listVlan)  # Просмотр вланов
        self.ui.infoPortBTN.clicked.connect(self.infoPort)  # информация о порте
        # self.ui.label_3.setText(self.btnTest())

    # Диалоговое окно с получением значения
    def inputDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getInt(self, 'Number port', 'Номер порта ->')
        if ok:
            le.setText(str(text))
            return text

    # просмотр интерфейсов
    def switchbord_interf(self):
        huawei = switchboard_command.interfHuawei(self.ip_address)
        # print(self.huawei)
        self.ui.resultEdit.setText(huawei)

    # список маков
    def listMac(self):
        huawei = switchboard_command.listMacHuawei(self.ip_address)
        # print(self.huawei)
        self.ui.resultEdit.setText(huawei)

    # Просмотр вланов
    def listVlan(self):
        huawei = switchboard_command.listVlanHuawei(self.ip_address)
        # print(self.huawei)
        self.ui.resultEdit.setText(huawei)

    # Информация о порте
    def infoPort(self):
        port = self.inputDialog()
        # print(port)
        huawei = switchboard_command.infoPortHuawei(self.ip_address, port)
        self.ui.resultEdit.setText(huawei)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
