# For details on how to build and run see README.md
# https://hub.docker.com/_/ros/
FROM ros:melodic

# Add user
RUN useradd -ms /bin/bash leia

CMD chmod +x /home/leia/workspace/plai/docker/alderaan/init.sh
ENTRYPOINT ["/home/leia/workspace/plai/docker/alderaan/init.sh"]