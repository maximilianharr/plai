# Build using: 
#   docker build -t sensai/full .
# Run using (port 8891 for jupyter):
#   docker run --gpus all --user harrmax -p 8891:8891 -it sensai/full bash
# Run Jupyter in docker
#   jupyter-notebook --port 8891 --ip 0.0.0.0

# # https://www.tensorflow.org/install/docker
FROM tensorflow/tensorflow:latest-gpu

# Add user
RUN useradd -ms /bin/bash harrmax

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
