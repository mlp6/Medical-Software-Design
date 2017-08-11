Argument Passing, Submodules, Package Installation, & Sphinx
============================================================

Make your code more flexible
----------------------------
* argparse
  + datatypes
  + default values
  + help

* see history of this repository for intermediate forms of argparse usage

Repositories within respositories
---------------------------------

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

Installing external packages
----------------------------

* ``conda`` (what Anaconda3 uses)
* ``pip``
  + Python Package Index
  + can take a snapshot of all packages that you need with ``pip freeze > requirements.txt``
  + package environment can be created using ``pip install -r requirements.txt``
  + commonly used to create virtual environments for testing and rapid deployment

Packaging your code to distribute
---------------------------------
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

Finding an arbitrary package
----------------------------
* Define ``PYTHONPATH`` (environmental variable)
* You can check what your PYTHONPATH has defined with the command: ``echo $PYTHONPATH``
* You can add paths to code in ``PyCharm -> Settings -> Project Interpreter``
* Manually add relative[|absolute] path

```
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+ '/../somedir/')
```

Building Documentation with Sphinx
----------------------------------
Sphinx (http://sphinx-doc.org/) is a documentation generation engine for Python
that is extremely powerful and lots of configuration options.  Here's a quick
start to automatically generate API-like documentation using docstrings:

1. ``sphinx-quickstart``

I prefer to create a distinct subdirectory (``docs/``) that contains all documentation.

2. There are lots of options that you will be walked through... defaults are usually okay, but be sure to select 'y' for the ``autodoc`` option.

3. add path to ``docs/conf.py``:

```
sys.path.insert(0, os.path.abspath('..'))
```
There is a similar path commented out near the header that you can uncomment and edit, along with the 2 import statements of the ``os`` and ``sys`` modules.


4. Run ``sphinx-apidoc -o docs .`` from the root level of your project (this will sweep through all of the ``*.py`` files in ``.`` and create corresponding ``*.rst`` files in ``docs/``)

5. ``docs/index.rst`` -> add modules that you'd like included in the documentation
  * Make sure that your docstring have a blank link before the rst :param: and :returns: lines.
  * Make sure to indent your file entries!!  Failure to indent will cause the rst-parser to "miss" your files.
  * You may want to add ``_build/`` to your ``.gitignore`` files:

6. Run Makefile to generate documentation (e.g., ``make html``).  This will create ``docs/_build/html`` with the default webpage being ``index.html``.

