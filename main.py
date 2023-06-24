import sys

import disein

import netmiko

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.ui = disein.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectBTN.clicked.connect(self.comm_huawei)
        # self.ui.label_3.setText(self.btnTest())

    # Коммутатор Huawei
    def comm_huawei(self):
        huawei_router = {
            'device_type': 'huawei',
            'host': '10.30.111.10',
            'username': 'admin',
            'password': 'fufvtvyjy',
            'secret': 'enablepass',
            # 'port': 20,
        }

        ssh = netmiko.ConnectHandler(**huawei_router)
        result = ssh.send_command('dis int br')
        self.ui.label_3.setText(result)
        print(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
