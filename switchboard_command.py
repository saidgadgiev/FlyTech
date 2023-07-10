import netmiko

import doСonnection


# Коммутатор Huawei просмотр интерфейсов
def interfHuawei(ip_address, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh = netmiko.ConnectHandler(**ssh)
    result = ssh.send_command('display interface brief')
    return result


# Коммутатор D-Link просмотр интерфейсов
def interfDLink(ip_address, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh = netmiko.ConnectHandler(**ssh)
    result = ssh.send_command('display interface brief')
    return result


# Коммутатор Huawei просмотр маков
def listMacHuawei(ip_address, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh1 = netmiko.ConnectHandler(**ssh)
    command = 'display mac-address'
    result = ssh1.send_command(command)
    return result


# Просмотр ВЛАНОВ Huawei
def listVlanHuawei(ip_address, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh1 = netmiko.ConnectHandler(**ssh)
    result = ssh1.send_command('display vlan')
    return result


# Просмотр информации о порте
def infoPortHuawei(ip_address, port, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh1 = netmiko.ConnectHandler(**ssh)
    command = 'display interface Ethernet 0/0/' + str(port)
    result = ssh1.send_command(command)
    return result


# Поиск по макадрессу
def serchMacAddressHuawei(ip_address, macc, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh1 = netmiko.ConnectHandler(**ssh)
    command = 'display mac-address ' + macc
    # print(command)
    result = ssh1.send_command(command)
    return result


# Маки на порту
def maccAboutPortHuawei(ip_address, port, login, password):
    ssh = doСonnection.comm_huawei(ip_address, login, password)
    ssh1 = netmiko.ConnectHandler(**ssh)
    command = 'display mac-address dynamic Ethernet 0/0/' + str(port)
    # print(command)
    result = ssh1.send_command(command)
    return result


# Диагностика порта
def checkPortHuawei(ip_address, port, login, password):
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


# Что прописанно на порту
def disThisPortHuawei(ip_address, port, login, password):
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
