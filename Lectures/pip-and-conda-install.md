## Python & pip setup

Download and install python from [here](https://www.python.org/downloads/) (We currently recommend python 3.6.x.). 

You need to make sure that `python` and `pip` are available as executable commands from your command line environment.  This will typically involve appending the path to your python executables to your `PATH` environmental variable.  One common way this is done in a bash shell enviroment is to add the following line to your `$HOME/.bashrc` file:
```
export PATH=/path/to/python/bin/:$PATH
```
:warning: Do not forget the `$PATH` at the end; this makes sure that all of your previous executable paths are still accessible!


Then make sure you have the most up to date pip:

For Mac/Linux:
```
pip install -U pip
```
For Windows:
```
python -m pip install -U pip
```
Then install the virtual environment creation tool called `virtualenv`.
```
pip install virtualenv
```

To create a new virtualenv in a project you're working on, first change directory (`cd`) to your project directory and run:
```sh
virtualenv myProject           # creates a virtual environment called "myProject" in your current directory
source myProject/bin/activate  # activates your virtual environment
```
This creates a virtual environemnt "sandbox" that will hold all the dependencies for your project at their specific versions.

Next, create a file called `requirements.txt` in this directory. This file will hold all the dependencies needed for your project. Fill it with the following: 
```
numpy
ipython
pytest
pytest-cov
pytest-pep8
```

Then run
```sh
pip install -r requirements.txt
```
to install those requirements in the currently activated virtual environment.

*Note: Windows machines can have difficulty installing packages like* `numpy` *that require access to C and Fortran compilers in your local system.  For that reason, you may want to use the Anaconda Setup below for Windows setups.*


## Anaconda Setup

[Install anaconda](https://docs.continuum.io/anaconda/install/). 

### Troubleshooting (skip to next section if no problems)
In your terminal type

```
which conda
```

If a path is returned to a `conda` program, you are all set to go. If you get some sort of a "not found" error, this means your terminal is unable to find the installed `conda` program, so you will have to tell it where to look. This is done by modifying the `PATH` environment variable. 

To fix this error on windows, find the install location of anaconda. There should be an `Anaconda3` folder in your user directory. Note the path down for this. Then create a `.bashrc` file in your home directory (`vim ~/.bashrc`) and put the following line in:
```
export PATH=/c/[YOUR PATH TO Anaconda3 folder here]/Scripts:$PATH
```
Then in the terminal type `source ~/.bashrc` and you should be good to go.

### Create virtual environment
In your project's git directory, create an `environment.yml` file that specifies the package dependencies of your project:

```
name: test-environment
dependencies:
  - python=3.6
  - numpy
  - ipython
  - pytest
  ... etc

```
Then:
```
conda env create -f environment.yml  # To create the virtual environment on your computer and install dependencies
source activate test-environment     # To activate the virtual environment for use
```
