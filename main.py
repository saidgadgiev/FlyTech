import sys
from PyQt5.QtWidgets import (QLineEdit, QInputDialog)
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
        self.login = self.ui.loginEdit.text  # Ввод логина
        self.password = self.ui.passwordEdit.text  # ввод пароля

        # Коммутатор Huawei
        # self.ui.connectBTN.clicked.connect(self.connectSwichbord)  # Подключение к комм
        self.ui.interfBTN.clicked.connect(self.switchbord_interf)  # кнопка просмотр портов Huawei
        self.ui.interfBTN_2.clicked.connect(self.switchbord_interf_dlink) # кнопка просмотр портов DLink
        self.ui.listMacBTN.clicked.connect(self.listMac)  # Кнопка список маков
        self.ui.shundownPortBTN.clicked.connect(self.shutdownPort)  # Отключение порта
        self.ui.noShundownPortBTN.clicked.connect(self.noShutdownPort) # Включение порта
        self.ui.listVlanBTN.clicked.connect(self.listVlan)  # Просмотр вланов
        self.ui.infoPortBTN.clicked.connect(self.infoPort)  # информация о порте
        self.ui.serchMacBTN.clicked.connect(self.serchMacAddress)  # поиск по маку
        self.ui.macPortBTN.clicked.connect(self.macAboutPort)  # маки на порту
        
        # self.ui.checkPortBTN.clicked.connect(self.checkPort)  # Диагностика порта
        # self.ui.disThisBTN.clicked.connect(self.disThisPort)  # что прописанно на порту
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

    # просмотр интерфейсов Huawei
    def switchbord_interf(self):
        if 0 < len(self.ip_address()):
            huawei = switchboard_command.interfHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # просмотр интерфейсов D-link
    def switchbord_interf_dlink(self):
        if 0 < len(self.ip_address()):
            DLink = switchboard_command.interfDLink(self.ip_address, self.login, self.password)
            self.ui.resultEdit_2.setText(DLink)
        else:
            self.ui.resultEdit_2.setText("Введите IP устройства")


    # список маков Huawei
    def listMac(self):
        if 0 < len(self.ip_address()):
            huawei = switchboard_command.listMacHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Просмотр вланов Huawei
    def listVlan(self):
        if 0 < len(self.ip_address()):
            huawei = switchboard_command.listVlanHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Информация о порте Huawei
    def infoPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.infoPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Поиск по маку Huawei
    def serchMacAddress(self):
        if 0 < len(self.ip_address()):
            macAddress = self.inputStrDialog()
            huawei = switchboard_command.serchMacAddressHuawei(self.ip_address, macAddress, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Маки на порту Huawei
    def macAboutPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.maccAboutPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Диагномтика порта Huawei
    def checkPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.checkPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Чтот прописанно на порту Huawei
    def disThisPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.disThisPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(huawei)
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Отключение порта Huawei
    def shutdownPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.shutdown_port(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(f'Порт {port} отключен')
        else:
            self.ui.resultEdit.setText("Введите IP устройства")

    # Включение порта Huawei
    def noShutdownPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = switchboard_command.undo_shutdown_port(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit.setText(f'Порт {port} включен')
        else:
            self.ui.resultEdit.setText("Введите IP устройства")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
