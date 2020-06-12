# For details on how to build and run see README.md
# https://www.tensorflow.org/install/docker
FROM tensorflow/tensorflow:latest-gpu

# Install python modules
RUN python3 -m pip install albumentations
RUN python3 -m pip install graphviz
RUN python3 -m pip install jupyter
RUN python3 -m pip install keras
RUN python3 -m pip install matplotlib
RUN python3 -m pip install nltk
RUN python3 -m pip install numpy
RUN python3 -m pip install opencv-python
RUN python3 -m pip install pandas
RUN python3 -m pip install requests
RUN python3 -m pip install scikit-image
RUN python3 -m pip install seaborn
RUN python3 -m pip install sklearn
# already installed RUN python3 -m pip install tensorflow
RUN python3 -m pip install urllib3

# 
RUN apt update 
RUN apt install -y libsm6 libxext6
RUN apt install -y libfontconfig1 libxrender1

# Add user
RUN useradd -ms /bin/bash kenobi

CMD chmod +x /home/kenobi/workspace/plai/docker/tatooine/init.sh
ENTRYPOINT ["/home/kenobi/workspace/plai/docker/tatooine/init.sh"]