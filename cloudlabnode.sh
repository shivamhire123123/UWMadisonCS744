REQUIRED_PKG="openjdk-8-jdk"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
	echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
	sudo apt update
	sudo apt-get --yes install $REQUIRED_PKG
fi
if [ ! -d "/mnt/data" ]; then
	sudo mkfs.ext4 /dev/xvda4
	sudo mkdir -p /mnt/data
	sudo mount /dev/xvda4 /mnt/data
fi
