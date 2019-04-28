#!/Users/lsy python
# coding:utf-8
# lsy
import paramiko
import time


def verification_ssh(host, username, password, port, root_pwd, cmd):
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=host, port=int(port), username=username, password=password)
    ssh = s.invoke_shell()
    print(ssh)
    ssh.send('su - \n')
    print(ssh.send('su - \n'))
    buff = ''
    if not buff.endswith('Password: '):
        resp = ssh.recv(9999)
        buff += str(resp)
        ssh.send(root_pwd)
        print(ssh.send(root_pwd))
        ssh.send('\n')
        buff = ''
    if not buff.endswith('# '):
        resp = ssh.recv(9999)
        buff += str(resp)
        buff = ''
    stdin, stdout, stderr = s.exec_command(cmd)
    result = stdout.read()
    print(result)
    stdin, stdout, stderr = s.exec_command('echo hello')
    print(stdout.read())
    s.close()
if __name__ == "__main__":
    verification_ssh('111.67.193.164', 'root', 'THElian996', '22', '1', 'ls')