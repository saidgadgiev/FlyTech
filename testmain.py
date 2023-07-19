import netmiko
from pprint import pprint

def send_show_command(device, commands):
    res = {}
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                res[command] = output
            return res
    except (netmiko.NetmikoTimeoutException, netmiko.NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    device = {
        "device_type": "dlink_ds_telnet",
        "host": "10.155.207.13",
        "username": "admin",
        "password": "fufvtvyjy",
        "port": 23,
    }
    result = send_show_command(device, ["show fdb"])
    pprint(result, width=120)
