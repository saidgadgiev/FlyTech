import socket

import netmiko
import doСonnection

# Просмотр не зареганных онушек

def showNoRegistOnuComm(ip_address, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show pon onu uncfg'
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Просмотр зареганных онушек
def listRegistrOnu(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show gpon onu state gpon-olt_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")

# Уровень сигнала
def signalStrenghtCommnd(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show pon power attenuation gpon-onu_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")

# Информация о зареганых онушек
def infoRegisteredOnuCommand(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show running-config interface gpon-olt_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")

# Что прописанно на ОНУ
def whatIsPrescribed(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show running-config interface gpon-onu_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")

# Просмотр Маков на ону
def showMac(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show mac gpon onu gpon-onu_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")
        
        
# Просмотр Информации об ону
def showInforOnu(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = ' show pon onu information gpon-onu_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")
        
def infoAboutPortONU(ip_address, port, login, password):
    try:
        telnet = doСonnection.comm_zte_telnet(ip_address, login, password)
        telnetConnect = netmiko.ConnectHandler(**telnet)
        command = 'show gpon remote-onu interface eth gpon-onu_1/' + port
        resultat = telnetConnect.send_command(command)
        telnetConnect.disconnect()
        return resultat
    except socket.gaierror:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")