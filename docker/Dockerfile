# For details on how to build and run see README.md
# https://www.tensorflow.org/install/docker
FROM tensorflow/tensorflow:latest-gpu

# 
RUN apt update 
RUN apt install -y libsm6 libxext6
RUN apt install -y libfontconfig1 libxrender1

# Install python libraries
COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r ./requirements.txt

# Add user
RUN useradd -ms /bin/bash ubuntu

CMD chmod +x /home/ubuntu/workspace/plai/docker/init.sh
ENTRYPOINT ["/home/ubuntu/workspace/plai/docker/init.sh"]