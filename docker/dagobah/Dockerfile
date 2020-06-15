# For details on how to build and run see README.md
# https://hub.docker.com/_/ros/
FROM ros:noetic

# Add user
RUN useradd -ms /bin/bash yoda

CMD chmod +x /home/yoda/workspace/plai/docker/dagobah/init.sh
ENTRYPOINT ["/home/yoda/workspace/plai/docker/dagobah/init.sh"]