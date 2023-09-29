import netmiko
ip_address = input('Введите IP адресс -> ')
login = input('Введите логин -> ')
password = input('Введите пароль -> ')
device = {
        'device_type': 'dlink_ds_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }
# device = switchboard_command.connectDlink(ip_address, login, password)
ssh = None
bol = True
print("1. Подключить коммутатор")
print("2. Просмотр интерфейсов")
print("3. список маков")
while bol == True:
    comm = input('enter -> ')
    if comm == "1":
        ssh = netmiko.ConnectHandler(**device)
    elif comm == "2":
        res = ssh.send_command("show ports")
        print(res)
    elif comm == "3":
        res = ssh.send_command("show fdb")
        print(res)
    else: 
        print("false")
        bol = False
print(device)