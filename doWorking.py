def comm_huawei(ip_address):
    # print(ip_address())
    huawei_router = {
        'device_type': 'huawei',
        'host': ip_address(),
        'username': 'admin',
        'password': 'fufvtvyjy',
        'secret': 'enablepass',
        # 'port': 20,
    }
    return huawei_router
