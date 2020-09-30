from setuptools import setup, find_packages

setup(
    name="egeaML",
    version="0.1.0",
    author="Andrea Giussani",
    author_email="andrea.f.giussani@gmail.com",
    description=("A python library used in support of the Book"
                 "'Applied Machine Learning with Python' (2019)"),
    url="https://github.com/andreagiussani/Applied_Machine_Learning_with_Python",
    license="BSD",
    packages=find_packages(),
    install_requires=['xgboost==1.2.0', 'pandas==1.1.2', 'scikit-learn==0.23.2',
                      'seaborn==0.11.0', 'catboost==0.24.1', 'gensim==3.8.3',
                      'nltk==3.5', 'matplotlib==3.3.2', 'wget==3.2',
                      'imbalanced-learn==0.7.0', 'tensorflow==2.3.1',
                      'keras==2.4.3', 'scipy==1.5.2',
                     ],
    include_package_data=True,
    classifiers=("Programming Language :: Python :: 3"),
)
