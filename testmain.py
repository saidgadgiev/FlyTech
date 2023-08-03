import netmiko
from pprint import pprint


def send_show_command(devices, commands):
    res = {}
    try:
        with netmiko.ConnectHandler(**devices) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                res[command] = output
            return res
    except netmiko.NetmikoTimeoutException:
        print("Не удалось установить TCP-соединение с устройством.\n"
              "Распространенными причинами этой проблемы являются:\n"
              "1. Неверное имя хоста или IP-адрес.\n"
              "2. Неправильный TCP-порт.\n"
              "3. Промежуточный брандмауэр, блокирующий доступ.\n")


if __name__ == "__main__":
    device = {
        "device_type": "huawei",
        "host": "10.50.57.1",
        "username": "admin",
        "password": "fufvtvyjy",
        # 'secret': 'enablepass',
        # "port": 20,
    }
    result = send_show_command(device, ['display mac-address'])
    pprint(result, width=120)
