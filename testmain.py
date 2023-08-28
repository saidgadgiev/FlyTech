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
        "device_type": "dlink_ds",
        "host": "10.155.207.13",
        "username": "admin",
        "password": "fufvtvyjy",
        'conn_timeout': 40
        # "secret": "fufvtvyjy",
        # "port": 23,
    }
    command = ['show fdb']
    result = send_show_command(device, command)
    # print(result)
