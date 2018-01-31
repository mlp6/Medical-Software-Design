# Python Fundamentals

## Setting Up Virtual Enironments
* Heavily recommended for local computer usage, 100% required for remote
  deployment.
* Python has a stadard library of functionality; additional functionality is
  imported into projects through additional packages.
  + PyPI is the most popular repository of Python packages.
  + `pip` is the tool to install packages from PyPI.
  + Different projects will require different packages.  Installing just the packages that you need for each Python project:
    - Prevents package version conflicts between different projects.
    - Establishes a minimized storage footprint of packages for each project
      (though commonly-used packages in many projects will be replicated).
  + `virtualenv` will be used to create virtual environments for each Python project.
  + :eyes: Make sure that you have `pip` and `virtualenv` installed on your laptop. :eyes:
* Steps towards creating and configuring a virtual environment:
  1. `virtualenv env` (creates a local python virtual environment in `env/`)
  1. `source env/bin/activate` (activate the working environment)
  1. `pip install $PACKAGENAME`
  1. Collect all of the packages that you need in a `requirements.txt` file
     [optionally include versions], and install all at once: `pip install -r
     requirements.txt`.  This is very useful for replicating virtual
     environments on new systems (e.g., CI testing setups).
  1. Work
  1. `deactivate`

## Python Starter Notes
* Python uses indentation--not semicolons and curly braces--to delineate
  different logical aspects of code.
```
if BOOLEAN_IS_TRUE:
    do_this()
else:
    do_that()
    and_this()

test_tuple = (1, 2, 3)
test_list = ['a', 'b', 'c']

for n, val in enumerate(test_tuple):
    print(val)
    print(n)
    print(test_tuple[n])

```

## Modular Coding
* Modularity will allow for discrete *units *of function to be explicitly *tested*.
  This is essential in medical software design.
* Modularity will allow the functional logic of software to be more readable.
* Modularity promotes the reuse of tested and validated code to compose new
  code.
* A non-object-oriented example of Python code:
```
def main():
    collect_all_csv_filenames()
    read_csv()
    write_data()


def collect_all_csv_filenames():
    from glob import glob
    pass


def read_csv():
    check_no_spaces()
    check_camel_case()
    pass


def write_data(type='json'):
    pass


def check_no_spaces():
    pass


def check_camel_case():
    pass
    

if __name__ == "__main__":
    main()
```
* All of the functions above, except for main, should be testable.
