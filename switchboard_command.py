import netmiko

import doWorking


# Коммутатор Huawei
class SwitchbordHuawei:
    # просмотр интерфейсов
    def interf(self, ip_address):
        # print(ip_address())
        ssh = doWorking.comm_huawei(ip_address)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('dis int br')
        return result

    # просмотр маков
    def listMac(self, ip_address):
        ssh = doWorking.comm_huawei(ip_address)
        ssh = netmiko.ConnectHandler(**ssh)
        result = ssh.send_command('display mac-address')
        return result


