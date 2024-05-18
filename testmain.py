import socket
import netmiko


device = {
        'device_type': 'zte_zxros_telnet',
        'host': '15.15.31.254',
        'username': 'admin',
        'password': 'fufvtvyjy',
    }
try:
    connection = netmiko.ConnectHandler(**device)
    result = connection.send_command('show running-config interface gpon-olt_1/1/1')
    connection.disconnect
    print(result)
except ValueError:
    print('Enter ip address')
except socket.gaierror:
    print("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
            "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
            "брандмауэр, блокирующий доступ.\n")
except TimeoutError:
    print('Не удаеться установить соеденение не верный АП аддресс ')
