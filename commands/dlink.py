import netmiko

import doСonnection


# Коммутатор D-Link просмотр интерфейсов
def interfDLink(ip_address, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('show ports')
        ssh.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Коммутатор DLink просмотр маков
def listMacDLink(ip_address, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'show fdb'
        result = ssh1.send_command(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Просмотр ВЛАНОВ Dlink
def listVlanDlink(ip_address, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        result = ssh1.send_command('show vlan')
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Просмотр информации о порте Dlink
def infoPortDlink(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'show ports ' + str(port) + ' details'
        result = ssh1.send_command(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Поиск по макадрессу Dlink
def serchMacAddressDlink(ip_address, macc, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'show fdb mac_address ' + macc
        # print(command)
        result = ssh1.send_command(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Маки на порту Dlink
def maccAboutPortDlink(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'show fdb port ' + str(port)
        result = ssh1.send_command(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Отключение порта Dlink
def shutdown_port_dlink(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = ['config ports ' + str(port) +
                   ' state disable']
        result = ssh1.send_config_set(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Включение порта Dlink
def undo_shutdown_port_dlink(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = ['config ports ' + str(port) +
                   ' state enable']

        result = ssh1.send_config_set(command)
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


