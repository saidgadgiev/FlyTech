import netmiko
import switchboard_command

ip_address = input('Введите IP адресс -> ')
login = input('Введите логин -> ')
password = input('Введите пароль -> ')
device = switchboard_command.connectHuawei(ip_address, login, password)
ssh = None
bol = True
print("1. Подключить коммутатор")
print("2. Просмотр интерфейсов")
print("3. список маков")
while bol == True:
    comm = input('enter -> ')
    if comm == "1":
        pass
        # ssh = netmiko.ConnectHandler(**device)
    elif comm == "2":
        res = device.send_command("dis int br")
        print(res)
    elif comm == "3":
        res = device.send_command("display mac-address")
        print(res)
    else: 
        print("false")
        bol = False
print(device)