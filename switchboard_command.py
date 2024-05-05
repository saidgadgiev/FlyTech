import netmiko

import doСonnection

# Подключение к коммутатору Huawei
def connectHuawei(ip_address, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh = netmiko.ConnectHandler(**ssh)
        return ssh
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Коммутатор Huawei просмотр интерфейсов
def interfHuawei(ip_address, login, password):
    try:
        ssh = doСonnection.comm_huawei(ip_address, login, password)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('display interface brief')
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")

# Коммутатор D-Link просмотр интерфейсов
def interfDLink(ip_address, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('show ports')
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
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")


# Что прописанно на порту
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
               'interface Ethernet 0/0/'+ str(port),
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

# Отключение порта Dlink
def shutdown_port_dlink(ip_address, port, login, password):
    try:
        ssh = doСonnection.comm_dlink(ip_address, login, password)
        ssh1 = netmiko.ConnectHandler(**ssh)
        command = ['config ports '  + str(port) +
               ' state disable']
        result = ssh1.send_config_set(command)
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
        command = ['config ports '  + str(port) +
               ' state enable']

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
               'interface Ethernet 0/0/'+ str(port),
               'undo shutdown']

        result = ssh1.send_config_set(command)
        return result
    except netmiko.NetmikoTimeoutException:
        return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                "брандмауэр, блокирующий доступ.\n")
    except netmiko.NetmikoAuthenticationException:
        return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                "являются:\nНеверные имя пользователя и пароль")