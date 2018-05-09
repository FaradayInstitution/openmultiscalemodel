# OxRSE Template Python Project
[![TravisCI](https://travis-ci.org/OxfordRSE/template-project-python.svg?branch=master)](https://travis-ci.org/OxfordRSE/template-project-python/)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/4409b63ew60cnmu3?svg=true)](https://ci.appveyor.com/project/martinjrobins/template-project-python)
[![codecov](https://codecov.io/gh/OxfordRSE/template-project-python/branch/master/graph/badge.svg)](https://codecov.io/gh/OxfordRSE/template-project-python)
[![Documentation Status](https://readthedocs.org/projects/oxrse-template-project-python/badge/?version=latest)](https://oxrse-template-project-python.readthedocs.io/en/latest/?badge=latest)

## Overview

This project provides a template for Python projects that want to adhere to good software practices.
It includes:

- A `setup.py` script for installation with `pip`.
- Style checking using `flake8` to check `PEP8` adherence.
- Documentation built from `dosctrings` using `Sphinx` and `reStructuredText`.
- Online documentation hosted on `readthedocs.org`.
- Unit tests built using the `unittest` module.
- Automated testing using `Travis` for Linux and OS/X, and `AppVeyor` for Windows
- Automated coverage testing using `coverage` and `codecov`.


## Installation

To install (for all users), use
```
pip install -e .
```
After running this, you can use `import oxrse` from anywhere on your system.

To install as a developer, use
```
$ pip install -e .[dev,docs]
```
Unlike a normal install, this doesn't _copy_ your project, but just makes a link to your source code.
As a result, you can still use `import oxrse` anywhere on your system, but the imported code will be the code in your development folder.

### How does it work?

Installation is handled via `setup.py`, which uses [setuptools](http://setuptools.readthedocs.io/).
This can then be used either directly (`python setup.py install`) or via `pip`.
Both methods install both the module and its dependencies.


## Style

OxRSE is written in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) and we follow the [PEP8 recommendations](https://www.python.org/dev/peps/pep-0008/) for coding style.

### Style checking

Adherence to PEP8 is checked using [flake8](http://flake8.pycqa.org/en/latest/).
To test your style locally, navigate to the OxRSE directory and type
```
$ flake8
```
Flake8 is configured using the file `.flake8`.

When there is no alternative (e.g. for imports in an `__init__.py`), individual lines of code can be excluded from style checking by adding `# noqa`.


## Documentation

Documentation is built from the [docstrings](https://www.python.org/dev/peps/pep-0257/) found in every module, class, and method. Docstrings are written in [reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html) (see also [wikipedia](https://en.wikipedia.org/wiki/ReStructuredText).

Documentation is built using [Sphinx](http://www.sphinx-doc.org/en/stable/). To do this locally, navigate to the OxRSE directory and type

```
cd doc
make clean
make html
```

Online documentation is built automatically and hosted by [readthedocs.org](https://oxrse-template-project-python.readthedocs.io/en/latest/).

To configure readthedocs, you must make an account on readthedocs.org and follow to instructions to create a project and link it to github.
Finally, make sure to tick "Install your project inside a virtualenv using setup.py install" on readthedocs "Advanced settings" tab.


## Testing

Unit tests are implemented using the [unittest](https://docs.python.org/3.3/library/unittest.html) package.

To run all unit tests, use
```
$ python -m unittest discover
```

To run a specific test, use e.g.
```
$ python -m unittest oxrse.tests.test_calculate
```

### Automated testing with Travis

We use [Travis](https://travis-ci.org) to test on Linux (Ubuntu) and OS/X.

To set this up, create an account on Travis (free for open source), and follow the instructions about setting up a project and linking it to github.

Once that's done, you can write a `.travis.yml` configuration script ([syntax](https://docs.travis-ci.com/)) that tells travis which Python versions to use, which commands to call for testing etc.
Feel free to copy-paste from our example code!

### Automated testing with AppVeyor

[AppVeyor](http://appveyor.com/) offers free testing on Windows systems.

As before, set up an account and follow the instructions.
An `appveyor.yml` configuration file ([syntax](https://packaging.python.org/guides/supporting-windows-using-appveyor/)) is used to tell AppVeyor which Python versions to test, what to install, and what test commands to run.

### Automated coverage checking with CodeCov

We use [codecov.io](https://docs.codecov.io/docs), which builds on [coverage](https://coverage.readthedocs.io/), to test if every line of code is hit during unit testing, and to generate nice reports.

Again, follow the instructions to set up and account and link it to github.

Some parts of your code (e.g. `NotImplementedError`s) can be excluded by writing a configuration file: `.coveragerc` ([syntax](https://coverage.readthedocs.io/en/latest/config.html)).


## Feedback and suggestions

If you have any feedback or suggestions about this project, please get in touch or open an issue.
