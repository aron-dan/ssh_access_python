import paramiko

hostname = "192.168.1.150"
username = "coletivo"
password = "colR22@Acx04D33"
port = 6422


with paramiko.SSHClient() as client:
    # Instrução para ler chaves cadastros para evitar clicar em yes ou no
    client.load_system_host_keys()

    # Para caso a chave do servidor não for conhecida, priemira tentativa
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    client.connect(hostname, port, username, password, look_for_keys=False)
    print("ok")
    (stdin, stdout, stderr) = client.exec_command("ip address print")

    output = stdout.read()
    print(str(output, 'utf8'))

    client.close()



