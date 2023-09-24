def comm_huawei(ip_address, login, password):
    huawei_router = {
        'device_type': 'huawei', 
        'host': ip_address,
        'username': login,
        'password': password,
        'secret': 'enablepass',
        # 'port': 20,
    }
    return huawei_router


def comm_dlink(ip_address, login, password):
    dlink_router = {
        'device_type': 'dlink_ds',
        'host': ip_address,
        'username': login,
        'password': password,
        'conn_timeout': 40
        # 'secret': 'enablepass',
        # 'port': 23,
    }
    return dlink_router

def comm_dlink_telnet(ip_address, login, password):
    dlink_router = {
        'device_type': 'dlink_ds_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }

def comm_zte_telnet(ip_address, login, password):
    dlink_router = {
        'device_type': 'zte_zxros_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }