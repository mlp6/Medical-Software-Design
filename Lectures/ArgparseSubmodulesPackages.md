# Argument Passing, Submodules, & Package Installation

## Make your code more flexible
* argparse
  + datatypes
  + default values
  + help

* Example: [argparse_demo.py](argparse_demo.py)

## Repositories within respositories

* ``git submodule``
  + clone a repository within a repository
  + ``git submodule init`` will create a ``.gitmodules`` files that stores the remote paths for each submodule
  + ``git submodule add URL`` adds each submodule (in a directory that is the repository name unless you specify otherwise)
  + pushed repositories do not copy the submodule contents, just the submodule URLs; the end-user must manually intialize (``git submodule init``) and update (``git submodule update``) all submodule content.
  + submodules are not perfect


* ``git subtree``
  + merge another repository branch into your repository
  + could just be a snapshot of a single commit state
  + content can be written into your repository and "come along for the ride"
  + easier to keep remote repositories frozen at previous (compatible) version unless explicitly brought up-to-date
  + more complicated initial syntax
  + More to read: http://blogs.atlassian.com/2013/05/alternatives-to-git-submodule-git-subtree/

## Installing external packages

* ``pip``
  + Python Package Index
  + can take a snapshot of all packages that you need with ``pip freeze > requirements.txt``
  + package environment can be created using ``pip install -r requirements.txt``
  + commonly used to create virtual environments for testing and rapid deployment
* ``conda`` (what Anaconda3 uses)

## Packaging your code to distribute
* ``__init__.py`` in all relevant directories, *except* test directories
* ``setup.py``

```
from distutils.core import setup
setup(name='bme590assignment02',
      version='RC1',
      packages=['bme590assignment02'],
      description = "amazing BME590 assignment",
      author = "amazing Duke Student",
      author_email = "netid@duke.edu",
      package_dir = {'bme590assignment02' : 'src'},
      #package_data = {},
      install_requires=['peakutils', 'bitstring'])
```

## Finding an arbitrary package
* Define ``PYTHONPATH`` (environmental variable).  This can be done
  "on-the-fly" or for your entire session.
* You can check what your PYTHONPATH has defined with the command: ``echo $PYTHONPATH``
* You can add paths to code in ``PyCharm -> Settings -> Project Interpreter``
* Manually add relative[|absolute] path

```
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+ '/../somedir/')
```
