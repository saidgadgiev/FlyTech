def comm_zte_telnet(ip_address, login, password):
    dlink_router = {
        'device_type': 'zte_zxros_telnet',
        'host': ip_address(),
        'username': login(),
        'password': password(),
    }
    return dlink_router
