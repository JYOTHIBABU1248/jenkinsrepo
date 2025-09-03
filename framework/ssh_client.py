import paramiko

class SSHClient:
    def __init__(self,host,username,password):
        # self.host = host
        # self.username = username
        # self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host,username = username,password = password)
    
    # def runcmd(self,cmd):
    #     stdin, stdout, stderr = self.ssh.exec_command(cmd)
    #     out = stdout.read().decode().strip()
    #     err = stderr.read().decode().strip()
    #     return out if out else err
    def runcmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        exit_code = stdout.channel.recv_exit_status()

        if exit_code != 0:
            raise RuntimeError(f"Command failed [{cmd}]: {err or out}")

        return out or err

    
    def close(self):
        self.ssh.close()