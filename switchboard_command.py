import netmiko

import doСonnection


# Коммутатор Huawei просмотр интерфейсов
def interfHuawei(ip_address):
    ssh = doСonnection.comm_huawei(ip_address)
    ssh1 = netmiko.ConnectHandler(**ssh)
    result = ssh1.send_command('display interface brief')
    return result


# Коммутатор Huawei просмотр маков
def listMacHuawei(ip_address):
    ssh = doСonnection.comm_huawei(ip_address)
    ssh1 = netmiko.ConnectHandler(**ssh)
    result = ssh1.send_command('display mac-address')
    return result


# Просмотр ВЛАНОВ Huawei
def listVlanHuawei(ip_address):
    ssh = doСonnection.comm_huawei(ip_address)
    ssh1 = netmiko.ConnectHandler(**ssh)
    result = ssh1.send_command('display vlan')
    return result
