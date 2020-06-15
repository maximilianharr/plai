# Alderaan
This docker container runs ROS 1

## Build
```bash
cd ~/workspace/docker
docker build -t planets/alderaan alderaan
```

## Run
```bash
docker run --user yoda --publish 11311:11311 --volume ${HOME}/workspace:/home/leia/workspace -h dagobah -it planets/dagobah bash
```