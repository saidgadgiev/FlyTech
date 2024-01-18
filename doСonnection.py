def connectOLT_GPON(ip_address, login, password):
    connect = {
        'device_type': 'zte_zxros_telnet',
        'host': ip_address,
        'username': login,
        'password': password,
    }
    return connect
