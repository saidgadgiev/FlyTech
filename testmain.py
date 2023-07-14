import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname="10.50.57.1",
    username="admin",
    password="fufvtvyjy",
    look_for_keys=False,
    allow_agent=False
)
ssh = client.invoke_shell()
ssh.send("dis int br\n")

for res in range(50):
    print(ssh.recv(30000))
ssh.close()
