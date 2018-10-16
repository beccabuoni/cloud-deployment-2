sudo yum -y install nfs-utils
sudo mkdir /mnt/nfstest
sudo chmod -R 755 /mnt/nfstest
sudo chown nfsnobody:nfsnobody /mnt/nfstest
sudo exportfs -ra
