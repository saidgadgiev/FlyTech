def comm_huawei(ip_address, login, password):
    # print(ip_address())
    huawei_router = {
        'device_type': 'huawei',
        'host': ip_address(),
        'username': login(),
        'password': password(),
        'secret': 'enablepass',
        # 'port': 20,
    }
    return huawei_router


def comm_dlink(ip_address):
    # print(ip_address())
    huawei_router = {
        'device_type': 'dlink_ds',
        'host': ip_address(),
        'username': 'loggin()',
        'password': 'password()',
        'secret': 'enablepass',
        # 'port': 20,
    }
    return huawei_router
