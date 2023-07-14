import re
import socket
import time
from pprint import pprint
import paramiko


def send_show_command(ip, user, passw, command):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=user,
        password=passw,
        look_for_keys=False,
        allow_agent=False
    )
    with cl.invoke_shell() as ssh:
        time.sleep(2)
        # ssh.send("dis int br")
        time.sleep(2)
        ssh.recv(60000)

        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(2)

            output = ""
            while True:
                try:
                    part = ssh.recv(60000).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
                if "More" in part:
                    ssh.send(" ")
            output = re.sub(" +--More--| +\x08+ +\08+", "\n", output)
            result[command] = output

        return result


if __name__ == "__main__":
    commands = ["display interface brief"]
    res = send_show_command("ip", "log", "pass", commands)
    pprint(res, width=120)

