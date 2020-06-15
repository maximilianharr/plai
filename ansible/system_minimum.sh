# Get the repository via GIT
sudo apt install -y git
mkdir ${HOME}/workspace
cd ~/workspace
git clone https://github.com/maximilianharr/plai.git plai

# Get and setup docker
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo service docker start
sudo usermod -aG docker $USER
newgrp docker

# Build and run container (jupyter-notebook)
cd ~/workspace/plai/docker
docker build -t planets/tatooine tatooine
docker run --user kenobi --publish 8891:8891 --volume ${HOME}/workspace:/home/kenobi/workspace -h tatooine -it planets/tatooine bash
firefox http://0.0.0.0:8891/login