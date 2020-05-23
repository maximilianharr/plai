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

### Set-up virual environment
```bash
python3 -m venv ./venv
source venv/bin/activate
python3 -m pip install albumentations
python3 -m pip install graphviz
python3 -m pip install jupyter
python3 -m pip install keras
python3 -m pip install matplotlib
python3 -m pip install nltk
python3 -m pip install numpy
python3 -m pip install pandas
python3 -m pip install scikit-image
python3 -m pip install seaborn
python3 -m pip install sklearn
python3 -m pip install tensorflow
python3 -m pip install urllib3
```

Upgrade packages using:
```bash
python3 -m pip install --upgrade ${PKG_NAME}
```

#### Optional: If you want to use pandas_ml (see "Known Bugs")
Latest versions of pandas and scikit-learn prevent import of pandas_ml v.0.6.1. To fix this, install supported versions
```bash
python3 -m pip install pandas==0.24.0
python3 -m pip install scikit-learn==0.20.0
```

### Unit-Tests
Run all unittests using
```bash
python3 ${PATH_TO_WS}/common/tools/run_all_unittests.py
```

## Runtime
Install path to libaries
```bash
source ${PATH_TO_WS}/setup.bash
```

Source virual environment
```bash
source venv/bin/activate
```

## Misc

### Presentation about AI
https://docs.google.com/presentation/d/1TeR-_v_WoZFvz8AkOEy-XYhMKhS0AVy31fzfF2hcAQQ/edit?usp=sharing

### AI Hands-On Tutorials
- "Machine Learning von A-Z: Lerne Python & R für Data Science!" by Jannis Seemann  
  https://www.udemy.com/course/machine-learning-komplett/  
- "Deep Learning, Neuronale Netze & AI: Der Komplettkurs" by Jannis Seemann  
  https://www.udemy.com/course/deep-learning-und-ai/  
- "Complete Guide to TensorFlow for Deep Learning with Python" by Jose Portilla"  
  https://www.udemy.com/course/complete-guide-to-tensorflow-for-deep-learning-with-python/  

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
pip install jupyterthemess
jt -t chesterish
```

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
