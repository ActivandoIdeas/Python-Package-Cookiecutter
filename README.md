<div align="center">
  <img width="64" src="https://avatars1.githubusercontent.com/u/66532658?s=400&u=f2457dec96897c5dbc843372ec8b325589ab84d5&v=4" alt="cookiecutter-django-rest">
  <h3 align="center">Python Packager</h3>
  <p align="center">
    This is a <a href="https://github.com/cookiecutter/cookiecutter" target="__blank">cookiecutter</a> template for generate a package
  </p>
  <p align="center">
    <a href="https://github.com/ActivandoIdeas/Cookiecutter-Flask-Microservice-SQLAlchemy/blob/master/LICENSE">
      	<img src="https://img.shields.io/badge/License-BSD3-blue.svg"  alt="license badge"/>
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square"  alt="python badge">
    </a>
  </p>
</div>

# About this cookiecutter

## Features

- Simple and basic configuration for make a package and publish in pypi

# Prerequisites

* Python 3.6 or higger https://www.python.org/
* Pip https://pip.pypa.io/en/stable/installing/

Install cookiecutter

```shell
pip install --user cookiecutter
```

# Install

Use this command

```shell
cookiecutter https://github.com/ActivandoIdeas/Python-Package-Cookiecutter
```

### `setup.py`

* **Use setuptools**
  It's the standard packaging library for Python. `distribute` has merged back into `setuptools`, and `distutils` is less capable.
* **setup.py should not import anything from the package**
  When installing from source, the user may not have the packages dependencies installed, and importing the package is likely to raise an `ImportError`.
* **setup.py should be the canonical source of package dependencies**
  There is no reason to duplicate dependency specifiers (i.e. also using a `requirements.txt` file). See the testing section below for testing dependencies.

### Testing

* **Use [Tox](https://tox.readthedocs.io) to manage test environments**
  Tox provides isolation, runs tests across multiple Python versions, and ensures the package can be installed.
* **Uses [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.
* **Define testing dependencies in `tox.ini`**
  Avoid duplicating dependency definitions, and use `tox.ini` as the canonical description of how the unittests should be run.
* **`tests` directory should not be a package**
  The `tests` directory should not be a Python package unless you want to define some fixtures.
  But the best practices are to use [PyTest fixtures](https://docs.pytest.org/en/latest/fixture.html) which provides a better solution.
  Therefore, the `tests` directory has no `__init__.py` file.

### Build the solution
```sh
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --user --upgrade twine
python -m twine upload dist/*
```


# License

BSD 3-Clause "New" or "Revised" License
View in https://github.com/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab/blob/master/LICENSE

# Contributing

Contributors are always welcome!
Feel free to raise an issue or submit a PR.
Read the code of Conduct here: https://github.com/ActivandoIdeas/Codigo-de-Conducta-y-Guia-Rapida

This project is based on cuokiecutter: 
* Read this for project contribution: 
    * https://raphael.codes/blog/create-your-own-cookiecutter-template/
    * https://cookiecutter.readthedocs.io/en/1.7.2/tutorials.html