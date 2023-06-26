import netmiko

import doWorking


# Коммутатор Huawei просмотр интерфейсов
def interfHuawei(ip_address):
    # print(ip_address())
    ssh = doWorking.comm_huawei(ip_address)
    ssh = netmiko.ConnectHandler(**ssh)
    result = ssh.send_command('dis int br')
    return result


# Коммутатор Huawei просмотр маков
def listMacHuawei(ip_address):
    ssh = doWorking.comm_huawei(ip_address)
    ssh = netmiko.ConnectHandler(**ssh)
    result = ssh.send_command('display mac-address')
    return result
