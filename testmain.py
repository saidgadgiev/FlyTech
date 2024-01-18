import netmiko

import commands.comZteOLT

ip_address = input('Введите IP адресс -> ')
login = input('Введите логин -> ')
password = input('Введите пароль -> ')
device = {
        'device_type': 'zte_zxros_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }
bol = True
conect = None
print("1. Подключить коммутатор")
print("2. Команда")
print("3. Отключение")

while bol == True:
    comm = input('enter -> ')
    if comm == "1":
        conect = commands.comZteOLT.connectOLT_GPON(ip_address, login, password)
        print(conect)

    elif comm == "2":
        res = commands.comZteOLT.checkSubscriber(conect)
        print(res)
    elif comm == "3":
        # res = commands.comZteOLT.shotdownOLT()
        conect.disconnect()
        print('отключение')
    else: 
        print("false")
        bol = False
print(device)