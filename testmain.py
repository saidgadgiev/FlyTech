import netmiko
ip_address = input('Введите IP адресс -> ')
login = input('Введите логин -> ')
password = input('Введите пароль -> ')
device = {
    'device_type': 'dlink_ds',
    'host': ip_address,
    'username': login,
    'password': password,
    'conn_timeout': 40
}
ssh = None
bol = True
print("1. Подключить коммутатор")
print("2. Просмотр интерфейсов")
print("3. список маков")
while bol == True:
    comm = input('enter')
    if comm == "1":
        ssh = netmiko.ConnectHandler(**device)
    elif comm == "2":
        print('two')
    elif comm == "3":
        print('three')
    else: 
        print("false")
        bol = False
print(device)