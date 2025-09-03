from framework.ssh_client import SSHClient

class StorageClient:
    def __init__(self,host,username,password):
        self.ssh = SSHClient(host,username,password)
    
    def create_partition(self,device="/dev/sda"):
        self.ssh.runcmd(f"sudo parted -s {device} mklabel msdos")
        cmd = f"sudo parted -s {device} mkpart primary ext4 1MiB 100%"
        return self.ssh.runcmd(cmd) 
    
    def format_partition(self,partition,fstype):
        return self.ssh.runcmd(f"mkfs.{fstype} -F {partition}")
    
    def mount_filesystem(self,mntdir,partition):
        #mntpath = "/mnt/testpath"
        self.ssh.runcmd(f"mkdir {mntdir}")
        return self.ssh.runcmd(f"mount {partition} {mntdir}")
    
    def run_fio(self,mount_point,runtime):
        cmd = (
            f"sudo fio --name=testing "
            f"--directory={mount_point} "
            f"--rw=readwrite "
            f"--bs=4k "
            f"--size=90M "
            f"--numjobs=1 "
            f"--time_based "
            f"--runtime={runtime} "
            f"--group_reporting "
            f"--output-format=json"
        )
        return self.ssh.runcmd(cmd)
    
    def close(self):
        self.ssh.close()