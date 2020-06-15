# Tatooine
Using Tensorflow with GPU support in Docker
<img src="./doc/nvidia_container_toolkit.png" alt="Nvidia Toolkit" width="450"/>

## Setting up base docker images
### Install nvidia-container-toolkit
Docu: https://github.com/NVIDIA/nvidia-docker  
Add the package repositories  
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

### Install tensorflow docker
Docu: https://www.tensorflow.org/install/docker  

```bash
docker pull tensorflow/tensorflow
docker run --gpus all --rm nvidia/cuda nvidia-smi
docker run --gpus all -it tensorflow/tensorflow:latest-gpu bash
```

### Build specific docker
Make sure to be in the folder containing the Dockerfile  
```bash
docker build -t planets/tatooine tatooine
```

## Run Jupyer-Notebook in container (normal)
1) Run docker container (open port 8891 or any other open port for jupyter):
```bash
docker run --gpus all --user kenobi --publish 8891:8891 --volume ${HOME}/workspace:/home/kenobi/workspace -h tatooine -it planets/tatooine bash
```

2) Run jupyer-notebook in docker container:
```bash
jupyter-notebook --port 8891 --ip 0.0.0.0 --NotebookApp.token='maytheforce'
```

3) Open firefox on host and enter: http://0.0.0.0:8891

x) Open bash in exising docker
```
docker container list
docker exec -it ${CONTAINER_NAME} /bin/bash
```

### Run Jupyer-Notebook in docker (docker-compose)
1) Build and start docker
```bash
docker-compose up
```
Open jupyter-notebook in firefox
```bash
firefox http://0.0.0.0:8891/tree
```

## Known Bugs
### cuDNN Initialization Error (convolution algorithm)
Problem:  
```
Failed to get convolution algorithm. This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.
```
Solution:  
Add this to your python script:  
```python
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.InteractiveSession(config=config)
```
