import socket
import sys
from PyQt5.QtWidgets import (QLineEdit, QInputDialog)
from PyQt5 import QtWidgets
import netmiko
import gui

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ip_address = self.ui.ipAddressEdit.text # IP адрес из строки ввода
        self.port_switchboard = self.ui.portEdit.text # порт коммутатора к кот подключен абонент
        self.interfaceClient = self.ui.interficeEdit.text # интерфейс абонента
        
        self.ui.start_check_GPON.clicked.connect(self.infoClientGpon) # Вывод информации
        
    def infoClientGpon(self):
        try:
            device = {
            'device_type': 'zte_zxros_telnet',
            'host': self.ip_address(),
            'username': '*****',
            'password': '********',
            }

            connection = netmiko.ConnectHandler(**device)
            command_info = connection.send_command(f'show pon onu information gpon-onu_1/{self.port_switchboard()}:{self.interfaceClient()}')
            command_signal_strength = connection.send_command(f'show pon power attenuation gpon-onu_1/{self.port_switchboard()}:{self.interfaceClient()}')
            command_show_port = connection.send_command(f'show gpon remote-onu interface eth gpon-onu_1/{self.port_switchboard()}:{self.interfaceClient()}')
            command_show_macc = connection.send_command(f'show mac gpon onu gpon-onu_1/{self.port_switchboard()}:{self.interfaceClient()}')
            command_show_config = connection.send_command(f'show running-config interface gpon-olt_1/{self.port_switchboard()}')
            
            result = '\nИНФОРМАЦИЯ ОБ ОНУШКЕ\n' + command_info +'\n\n УРОВЕНЬ СИГНАЛА \n\n' +  command_signal_strength + '\n\nПРОСМОТР МАКОВ НА ОНУ\n\n' + command_show_macc + '\n\nПРОСМОТР ЛИНКОВ НА ПОРТУ ОНУШКИ\n\n' + command_show_port
            connection.disconnect
            
            self.ui.resultEdit.setText(result) 
            self.ui.result2Edit.setText(command_show_config)
        except ValueError:
            self.ui.resultEdit.setText('ВВЕДИТЕ IP ADDRESS УСТРОЙСТВА') 
            self.ui.result2Edit.setText('ВВЕДИТЕ IP ADDRESS УСТРОЙСТВА')
        except socket.gaierror:
            self.ui.resultEdit.setText("Не удалось установить TCP-соединение с устройством. \n Проверьте правильно ли вы ввели IP address устройства ")
            self.ui.result2Edit.setText("Не удалось установить TCP-соединение с устройством. \n Проверьте правильно ли вы ввели IP address устройства ")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())