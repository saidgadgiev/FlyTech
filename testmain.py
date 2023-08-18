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
        "device_type": "zte_zxros_telnet",
        "host": "10.155.204.11",
        "username": "admin",
        "password": "P@ntera2i7",
        "secret": "P@ntera2i7",
        # "port": 23,
    }
    command = ['show mac']
    result = send_show_command(device, command)
    pprint(result, width=120)
