from paramiko import SSHClient
import paramiko



def __init__(self):
    self.ssh = SSHClient()

    # Instrução para ler chaves cadastros para evitar clicar em yes ou no
    self.ssh.load_system_host_keys()

    # Para caso a chave do servidor não for conhecida
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    self.ssh.connect(hostname='127.0.0.1', username='root', password='SENHA_DE_ROOT')

def exec_cmd(self,cmd):
    stdin,stdout,stderr = self.ssh.exec_command(cmd)
    if stderr.channel.recv_exit_status() != 0:
        print (stderr.read())
    else:
        print (stdout.read())

if __name__ == '__main__':
    ssh = SSH()
    ssh.exec_cmd("apt-get update")