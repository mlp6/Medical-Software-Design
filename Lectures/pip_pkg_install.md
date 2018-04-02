# Pip installing your own package

`setup.py` file

`from setup tools import setup`
Use `setup()` method

Can have source code available to developers -> can specify what you want installed in virtualenv

Can specify all sorts of things
```
setup (
  name='my_package_name',
  packages=['list of packages'],
  package_dir=[],
  version=1.0.0,
  license='Apache v1.0',
  author="Anika Mukherji",
  author_emai;="frst.last@duke.edu",
  long_description=open('README.md').read(),
  install_requires=["packages that must be installable"] # these are packages that must be able to be installed, gives flexibility
                                                         # that allows developer to freely develop code
)
```

### Option 1

Can run...
`python install setup.py`

Different from manually pointing PYTHONPATH
Actually installing package in virtual env

^ This workflow assumes you were able to get code onto your local computer

What if you don't want user to do that...?

### Option 2

Can run...
`pip install git+https://github...`
** this can be an ssh address as well
** or any path that says where your package is

Don't need central identity to store package -> can grab package from git
User doens't need to worry about source code -> _magic_

### Important Note

In package directories, need `__init__.py` file

Usually completely empty -> placeholder file giving python permission to autodiscover files in that directory


### Unit tests

Unit tests not included in general user package

But can be included if you want

Can even specify script that ensures all tests pass before package installs


## Reproducible code + analyses

`pip install git+https://github.com/mlp6/fem`
Pulls by default most recent version on master
If you need to go back a version... (like if you are writing a paper on results and you need to go back & recreate findings, but code has been further developed)
can specify tagged release version (like 1.0.0)
`pip install git+https://github.com/mlp6/fem@1.0.0`

*tagging is useful!

## Pros of using pip instead of git clone
With git clone = manually tell server the path + activating your virtual env (2 layers)
Pip install = most recent version of package in your virtual env -> leverage pip as package manager

Can add that address `git+https://github.com/...` to your requirements.txt file
