import sys

import disein
import switchboard_command

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.huawei = None
        self.ui = disein.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_address = self.ui.ipAddressEdit.text  # IP адресс из строки ввода
        self.ui.interfBTN.clicked.connect(self.switchbord_interf)  # кнопка просмотр портов
        self.ui.listMacBTN.clicked.connect(self.listMac)  # Кнопка список маков
        # self.ui.serchMacBTN.clicked.connect()  # кнопка поиск по маку
        # self.ui.label_3.setText(self.btnTest())

    # просмотр интерфейсов
    def switchbord_interf(self):
        self.huawei = switchboard_command.SwitchbordHuawei.interf(self, self.ip_address)
        # print(self.huawei)
        self.ui.resultEdit.setText(self.huawei)

    def listMac(self):
        self.huawei = switchboard_command.SwitchbordHuawei.listMac(self, self.ip_address)
        # print(self.huawei)
        self.ui.resultEdit.setText(self.huawei)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
