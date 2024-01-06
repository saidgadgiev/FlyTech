import socket

import netmiko

ip_address = input('Введите IP адресс -> ')
login = input('Введите логин -> ')
password = input('Введите пароль -> ')
device = {
        'device_type': 'zte_zxros_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }
# device = switchboard_command.connectDlink(ip_address, login, password)
ssh = None
bol = True
print("1. Подключить коммутатор")
print("2. Просмотр интерфейсов")
print("3. отключение")
while bol == True:
    comm = input('enter -> ')
    if comm == "1":
        try:
            print('идет подключение')
            ssh = netmiko.ConnectHandler(**device)
            print("успех подключения")
        except socket.gaierror:
            print("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    elif comm == "2":
        res = ssh.send_command("show ports")
        print(res)
    elif comm == "3":
        ssh.disconnect()
        print(res)
    else:
        print("false")
        bol = False
print(device)


