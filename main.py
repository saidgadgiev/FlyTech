import netmiko

huawei_router = {
    'device_type': 'huawei',
    'host': '10.30.111.10',
    'username': 'admin',
    'password': 'fufvtvyjy',
    'secret': 'enablepass',
    # 'port': 20,
}

ssh = netmiko.ConnectHandler(**huawei_router)
result = ssh.send_command('dis int br')
print(result)