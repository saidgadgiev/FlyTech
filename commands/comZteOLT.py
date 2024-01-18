import socket

import netmiko

import doСonnection


# Подключение к ОЛТ
def connectOLT_GPON(ip_address, login, password):
    try:
        telnet = doСonnection.connectOLT_GPON(ip_address, login, password)
        connect = netmiko.ConnectHandler(**telnet)
        # print('подключено')
        return connect, 'подключенно'
    except netmiko.exceptions.NetmikoAuthenticationException:
        # print('Ошибка Аудентификации')
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")
    except socket.gaierror:
        # print('Ненерное IP адресс')
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")


# Отключение от ОЛТ
def shutdownOLT():
    connectOLT_GPON().disconnect()
    return ('Соеденение с ОЛТ отключенно')


# Проверка абонента
def checkSubscriber(connect):
    res = connect.send_command('show gpon onu state gpon-olt_1/1/2')
    print(res)
