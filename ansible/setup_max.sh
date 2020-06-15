# Update system
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade

# Install tools
sudo apt install build-essential
sudo apt install vim test
sudo apt install terminator
sudo apt install net-tools curl 

# Compiler
sudo apt install protobuf-compiler protobuf-c-compiler
sudo apt install clang

# Programming software

## Database

### PostgreSQL
### https://www.postgresql.org/download/linux/ubuntu/
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release --codename --short)-pgdg main" | sudo tee -a /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt install postgresql-12-postgis-3 postgresql-12-postgis-3-scripts
sudo pg_ctlcluster 12 main start

#### User input (change line in file)
sudo vim /etc/postgresql/12/main/pg_hba.conf
#### local   all             postgres                                peer
#### local   all             postgres                                md5
sudo pg_ctlcluster 12 main stop
sudo pg_ctlcluster 12 main start

### QGIS and pgadmin
sudo apt install qgis
sudo apt install pgadmin4
sudo apt install pgadmin4-apache2

# CI / CD
## Docker
## https://docs.docker.com/engine/install/ubuntu/
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-get install docker-compose

sudo usermod -aG docker $USER
newgrp docker

# IDEs
sudo snap install --classic code


# Python
sudo apt install python3-pip python3-venv
python3 -m pip install --upgrade pip

# Python virtual environment
cd ~/workspace
python3 -m venv venv
source venv/bin/activate
python3 -m pip install wheel
python3 -m pip install jupyter


# Cuda

# ~/.bashrc


# Ubuntu brightness
# https://askubuntu.com/questions/76081/brightness-not-working-after-installing-nvidia-driver
# https://askubuntu.com/questions/162317/screen-brightness-not-working
# https://wiki.archlinux.org/index.php/backlight
```bash
sudo -H vim /etc/default/grub
```
Change this line 
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```
to
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_osi=Linux acpi_backlight=video"
```
Then
```
sudo gedit /usr/share/X11/xorg.conf.d/10-nvidia-brightness.conf
```
paste
```
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BoardName      "GeForce RTX 2060"
    Option         "RegistryDwords" "EnableBrightnessControl=1"
EndSection
```