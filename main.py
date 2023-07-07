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
        self.ui.serchMacBTN.clicked.connect(self.serchMacAddress)  # поиск по маку
        self.ui.macPortBTN.clicked.connect(self.macAboutPort)  # маки на порту
        # self.ui.checkPortBTN.clicked.connect(self.checkPort)  # Диагностика порта
        self.ui.disThisBTN.clicked.connect(self.disThisPort)  # что прописанно на порту
        # self.ui.label_3.setText(self.btnTest())

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

    # просмотр интерфейсов
    def switchbord_interf(self):
        huawei = switchboard_command.interfHuawei(self.ip_address)
        self.ui.resultEdit.setText(huawei)

    # список маков
    def listMac(self):
        huawei = switchboard_command.listMacHuawei(self.ip_address)
        self.ui.resultEdit.setText(huawei)

    # Просмотр вланов
    def listVlan(self):
        huawei = switchboard_command.listVlanHuawei(self.ip_address)
        self.ui.resultEdit.setText(huawei)

    # Информация о порте
    def infoPort(self):
        port = self.inputDialog()
        huawei = switchboard_command.infoPortHuawei(self.ip_address, port)
        self.ui.resultEdit.setText(huawei)

    # Поиск по маку
    def serchMacAddress(self):
        macAddress = self.inputStrDialog()
        huawei = switchboard_command.serchMacAddressHuawei(self.ip_address, macAddress)
        self.ui.resultEdit.setText(huawei)

    # Маки на порту
    def macAboutPort(self):
        port = self.inputDialog()
        huawei = switchboard_command.maccAboutPortHuawei(self.ip_address, port)
        self.ui.resultEdit.setText(huawei)

    # Диагномтика порта
    def checkPort(self):
        port = self.inputDialog()
        huawei = switchboard_command.checkPortHuawei(self.ip_address, port)
        self.ui.resultEdit.setText(huawei)

    # Чтот прописанно на порту
    def disThisPort(self):
        port = self.inputDialog()
        huawei = switchboard_command.disThisPortHuawei(self.ip_address, port)
        self.ui.resultEdit.setText(huawei)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
