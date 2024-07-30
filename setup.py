"""
Install pychemauth.

author: nam
"""
from setuptools import find_packages, setup

# Get __version__ from __init__ file
exec(open("pychemauth/__init__.py").read())

setup(
    name="pychemauth",
    description="Python-based Chemometric Authentication",
    author="Nathan A. Mahynski",
    homepage="https://github.com/mahynski/pychemauth",
    python_requires=">=3.10.0",
    version=__version__,
    packages=find_packages(),
    license_files=("LICENSE",),
    test_suite="tests",
    tests_require=["pytest"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "baycomp==1.0.3",
        "bokeh",
        "bokeh_sampledata==2024.2",
        "BorutaShap @ git+https://github.com/Ekeany/Boruta-Shap.git@38af879",
        "imbalanced-learn==0.11.0",
        "IPython",
        "ipywidgets",
        "matplotlib==3.7.2",
        "nodejs==0.1.1",
        "numpy==1.24.3",
        "pandas==1.5.3",
        "pre-commit==3.3.3",
        "scikit-learn==1.3.0",
        "scipy==1.11.1",
        "seaborn==0.12.2",
        "shap==0.45.1",
        "tqdm==4.66.1",
        "umap-learn==0.5.3",
        "watermark==2.4.3",
        "pytest==7.4.0",
        "xgboost==2.0.0",
        "missingno==0.5.2",
        "wandb>=0.17.5",
        "pyts==0.13.0",
        "pillow>=10.0.0",
        "visualkeras>=0.1.3",
        "huggingface_hub==0.23.4",
        "tensorflow==2.14.0",  # This command should install keras==2.14.0 as well - based on Keras recommendation (https://keras.io/getting_started/#installing-keras-3) for creating a "universal GPU environment" based on Colab recommendations: https://colab.research.google.com/drive/13cpd3wCwEHpsmypY9o6XB6rXgBm5oSxu
    ],
)
