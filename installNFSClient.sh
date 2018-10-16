sudo yum -y install nfs-utils
sudo mkdir /mnt/nfstest
sudo mkdir /mnt/nfstest2
sudo mount -t nfs 192.168.1.1:/mnt/nfstest /mnt/nfstest
sudo mount -t nfs 192.168.1.3:/mnt/nfstest2 /mnt/nfstest2
