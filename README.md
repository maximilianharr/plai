# PL:AI - Playground Library for Artificial Intelligence
Code-Snippets, tutorials and librarys for AI algorithm development

## Installation

### Cloud Computing
If you do not want to setup the environment on your computer, you can also execute your jupyter-notebooks on:
- Google Colab https://colab.research.google.com/drive/
- Kaggle https://www.kaggle.com/
- AWS https://aws.amazon.com/


### Clone repo
```bash
git clone https://github.com/maximilianharr/plai plai
```

### Build and Run Docker Container
```bash
cd docker 
docker-compose build
docker-compose up
```

#### Optional: If you want to use pandas_ml (see "Known Bugs")
Latest versions of pandas and scikit-learn prevent import of pandas_ml v.0.6.1. To fix this, install supported versions
```bash
python3 -m pip install pandas==0.24.0
python3 -m pip install scikit-learn==0.20.0
```

## Unit-Tests
Run all unittests using
```bash
python3 ${PATH_TO_WS}/common/tools/run_all_unittests.py
```

## Misc

### Presentation about AI
./common/tutorials/README.md
https://docs.google.com/presentation/d/1TeR-_v_WoZFvz8AkOEy-XYhMKhS0AVy31fzfF2hcAQQ/edit?usp=sharing

### AI Hands-On Tutorials
- "Machine Learning von A-Z: Lerne Python & R für Data Science!" by Jannis Seemann  
  https://www.udemy.com/course/machine-learning-komplett/  
- "Deep Learning, Neuronale Netze & AI: Der Komplettkurs" by Jannis Seemann  
  https://www.udemy.com/course/deep-learning-und-ai/  
- "Complete Guide to TensorFlow for Deep Learning with Python" by Jose Portilla"  
  https://www.udemy.com/course/complete-guide-to-tensorflow-for-deep-learning-with-python/  

### CNNs
https://pypi.org/project/darknetpy/
https://pypi.org/project/yolov3/

### Further information / links
https://neurohive.io/en/  
Implementations of common nets: https://github.com/keras-team/keras-applications  
Trained common nets: https://keras.io/api/applications/  

#### Popular datasets
Some popular datasets are listed at https://www.tensorflow.org/datasets/catalog/overview  
Coco (Common Objects in Context) http://cocodataset.org/#home 
Openimages https://storage.googleapis.com/openimages/web/index.html  

### Jupyter-Notebooks

#### Start jupyter-notebook
```bash
jupyter-notebook
```

#### Convert *.ipynb to *.py
```bash
jupyter nbconvert --to=python --output-dir=./ ${SCRIPT}.ipynb
```

#### Jupyer dark mode
```bash
pip install jupyterthemes
jt -t chesterish
```

## Frameworks
https://github.com/facebookresearch/detr

## Known Bugs
### pandas_ml import error
Problem:  
pandas_ml v.0.6.1 supports pandas v0.22.0 and scikit-learn 0.20.0 (1) and will throw "AttributeError" if newer version of pandas and scikit-learn provided.  
(1) https://pandas-ml.readthedocs.io/en/latest/  
Solution (not tested):  
```bash
python3 -m pip install pandas==0.24.0
python3 -m pip install scikit-learn==0.20.0
```

### Unfortunately this does not work yet:
```bash
sudo apt install rustc
pip install --upgrade pip setuptools wheel
python3 -m pip install bottleneck
python3 -m pip install darknetpy
python3 -m pip install yolov3
```