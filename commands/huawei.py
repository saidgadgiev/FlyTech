import netmiko

import doСonnection


# Коммутатор Huawei просмотр интерфейсов
def interfHuawei(ip_address, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('display interface brief')
        ssh.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Коммутатор Huawei просмотр маков
def listMacHuawei(ip_address, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'display mac-address'
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


# Просмотр ВЛАНОВ Huawei
def listVlanHuawei(ip_address, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        result = ssh1.send_command('display vlan')
        ssh1.disconnect()
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Просмотр информации о порте Huawei
def infoPortHuawei(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'display interface Ethernet 0/0/' + str(port)
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


# Поиск по макадрессу
def serchMacAddressHuawei(ip_address, macc, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'display mac-address ' + macc
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


# Маки на порту Huawei
def maccAboutPortHuawei(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = 'display mac-address dynamic Ethernet 0/0/' + str(port)
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

# Диагностика порта
def checkPortHuawei(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = [
            'system-view',
            'interface Ethernet 0/0/' + str(port),
            'virtual-cable-test',
            'y'
        ]
        print(command)
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


# Что прописано на порту
def disThisPortHuawei(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        print(1)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = [
            'system-view',
            'interface Ethernet 0/0/' + str(port),
            'display this'
        ]
        result = ssh1.send_config_set(command)
        ssh1.disconnect()
        print(result)
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Отключение порта Huawei
def shutdown_port(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = ['system-view',
                   'interface Ethernet 0/0/' + str(port),
                   'shutdown']

        result = ssh1.send_config_set(command)
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Включение порта Huawei
def undo_shutdown_port(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = ['system-view',
                   'interface Ethernet 0/0/' + str(port),
                   'undo shutdown']

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
