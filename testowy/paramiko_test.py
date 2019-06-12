import paramiko

hostname = "192.168.1.200"
username = "arnold"
password = "1234"
port = 22

#command = 'pwd; ls -l'


client = paramiko.SSHClient()

try:
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    #stdin, stdout, stderr = client.exec_command('pwd')
    #stdin, stdout, stderr = client.exec_command('ls')
    stdin, stdout, stderr = client.exec_command('cd Desktop; ls')
    print("Command:\n" + stdout.read().decode("utf-8"))
    print("err:\n" + stderr.read().decode("utf-8"))

    stdin, stdout, stderr = client.exec_command('ls')
    #print(stdin, stdout, stderr)
    print("Command:\n" + stdout.read().decode("utf-8"))
    print("err:\n" + stderr.read().decode("utf-8"))

finally:
    client.close()