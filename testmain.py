import netmiko
from pprint import pprint


def send_show_command(devices, commands):
    res = {}
    try:
        ssh = netmiko.ConnectHandler(**device)
        res = ssh.send_config_set(commands)
        print (res)
    except netmiko.NetmikoTimeoutException:
        print("Не удалось установить TCP-соединение с устройством.\n"
              "Распространенными причинами этой проблемы являются:\n"
              "1. Неверное имя хоста или IP-адрес.\n"
              "2. Неправильный TCP-порт.\n"
              "3. Промежуточный брандмауэр, блокирующий доступ.\n")


if __name__ == "__main__":
    device = {
        "device_type": "huawei",
        "host": "10.50.57.11",
        "username": "admin",
        "password": "fufvtvyjy",
        # "secret": "P@ntera2i7",
        # "port": 23,
    }
    command = ['system-view', 
               'interface Ethernet 0/0/1',
               'undo shutdown']
    result = send_show_command(device, command)
    # print(result)
