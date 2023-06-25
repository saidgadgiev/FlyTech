import sys

import disein
import doWorking
import netmiko

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.ui = disein.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.interfBTN.clicked.connect(self.comm_huawei_f)
        self.ip_address = self.ui.ipAddressEdit.text

        # self.ui.label_3.setText(self.btnTest())

    # Коммутатор Huawei
    def comm_huawei_f(self):
        ssh = doWorking.comm_huawei(self.ip_address)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('dis int br')
        self.ui.resultEdit.setText(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
