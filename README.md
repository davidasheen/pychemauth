Chemometric Authentication
==========================
This is a centralized repository of common (and emerging) tools to perform chemometric analysis implemented in python.  These methods are designed to be compatible with [scikit-learn's estimator API](https://scikit-learn.org/stable/developers/develop.html) so they can be deployed in pipelines used with GridSearchCV, etc.  

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
![Workflow](https://github.com/mahynski/chemometrics/actions/workflows/python-app.yml/badge.svg?branch=main)
<!--[![codecov](https://codecov.io/gh/mahynski/chemometrics/branch/main/graph/badge.svg?token=YSLBQ33C7F)](https://codecov.io/gh/mahynski/chemometrics)-->

## License Information
* See LICENSE for more information.
* Any mention of commercial products is for information only; it does not imply recommendation or endorsement by [NIST](https://www.nist.gov/).

# Installation

~~~ bash
$ git clone https://github.com/mahynski/chemometrics.git
$ pip install -r requirements.txt
~~~

Simply add this directory to your PYTHONPATH, or locally in each instance (i.e., sys.path.append()) and import the model as usual.

~~~ bash
$ echo 'export PYTHONPATH=$PYTHONPATH:/path/to/module/' >> ~/.bashrc
$ source ~/.bashrc
~~~

~~~ python
import chemometrics
~~~

You can run unittests to make sure your installation is working correctly.

~~~ bash
$ python -m unittest discover tests/
~~~

# Capabilities

## Preprocessors
### Scaling
* Corrected scaling (aking to sklearn's [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) but uses [unbiased/corrected standard deviation](https://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation) instead)
* Pareto Scaling (scales by square root of standard deviation)
* Robust Scaling (scales by IQR instead of standard deviation)
### Imputation
* Expectation Maximization with Iterative PCA (missing X values)
* Expectation Maximization with Iterative PLS (missing X values)
* Limit of Detection (randomly below LOD)

## Conventional Chemometrics
### Classifiers
* PCA (for data inspection)
* PLS-DA (soft and hard variants)
* SIMCA
* DD-SIMCA
### Regressors
* PCR
* PLS

## Topological Data Analysis
* [UMAP](https://umap-learn.readthedocs.io/en/latest/)
* [PacMAP](https://github.com/YingfanWang/PaCMAP)

## Outler Detection with AI/ML
* [pyOD](https://pyod.readthedocs.io/en/latest/)

## Explanations
* [SHAP](https://shap.readthedocs.io/en/latest/)

# Usage 

Refer to `examples/` for example usage and more explicit details.

## Example Pseudocode
~~~ python
>>> from chemometrics.classifier.plsda import PLSDA
>>> X_train, X_test, y_train, y_test = load_data(...)
>>> sp = PLSDA(n_components=30, style='soft')
>>> _ = sp.fit(X_train.values, y_train.values)
>>> pred = sp.predict(X_train.values)
>>> df, I, CSNS, CSPS, CEFF, TSNS, TSPS, TEFF = sp.figures_of_merit(pred, y_train.values)
~~~

# Deploying on Google Colab

You can use this repo in the cloud by using [Google Colab](https://colab.research.google.com).
Follow the instructions to set up an account if you do not already have one.

![](examples/colab_example.gif)

Below is the code that accompanies the gif above.

~~~python
# 1. Upload your data as a .csv file (enter this code and click "Choose Files")

from google.colab import files
uploaded = files.upload() # Currently there are some issues with this on Firefox

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
~~~

~~~python
# 2. Read your csv data into a Pandas DataFrame
import pandas as pd
df = pd.read_csv(list(uploaded.keys())[0])
~~~

~~~python
# Clone chemometrics repo
!git clone https://github.com/mahynski/chemometrics.git
!cd chemometrics; pip install -r requirements.txt
~~~~

~~~python
import chemometrics

# Perform analysis ...
~~~
