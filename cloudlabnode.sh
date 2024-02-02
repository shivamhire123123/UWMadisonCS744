sudo apt update
sudo apt install openjdk-8-jdk
sudo mkfs.ext4 /dev/xvda4
sudo mkdir -p /mnt/data
sudo mount /dev/xvda4 /mnt/data
