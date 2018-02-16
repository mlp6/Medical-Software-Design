# Python Fundamentals

## Interactive Python Environments
* In addition to writing Python code in a file that can be executed, we have two common ways to interactively work with Python:
  + `ipython`
  + Jupyter notebooks (formerly called ipython notebooks)
* Jupyer notebooks are great for adding annotated text to describe / document
  snippets of executable Python code.  They are also great to render inline
  graphics, and they can be rendered live in GitHub to boot!
* We are going to use a Jupyer notebook for the first part of this assignment.

## Exploring Python Syntax
* Fork this repository: https://github.com/mlp6/Medical-Software-Design
* Create a branch on your local clone of the forker repository called:
  `$NETID/PythonFundamentals01` (the specific name is very important!)
* Create a local virtual environment with the packages in `requirements.txt`.
* Activate your virtual environment.
* Change into the `Assignments/` directory and run `jupyter notebook
  PythonFundamentals.ipynb`.  You will be prompted to launch a web browser that
  has an address that starts with `127.0.0.1` or `localhost`; your web browser
  might automatically be launched with this page too.
* Work through the interactive notebook exercise.
* Commit your completed notebook, and submit a Pull Request to `mlp6` and
  `suyashkumar` with the title `Python Fundamentals ($NETID)`.  Note - your Pull
  Request will be used to evaluate your notebook, but ultimately will be closed
  without merging it back in.
* If you find any errors in the notebook, please submit an Issue in the `mlp6`
  version of the repository.

## Mini-project
* We are going to start putting your `git` and `python` skills to use!
* The repository that you forked last lecture has hall all of the Pull Requests
  from each student merged into the master branch.
* Update the `master` branch of your forked repository to reflect the commits
  up until the `v1.0.0` annotated tag (which should be the latest version).
  Note that you can do this through GitHub **or** locally in your forked
  repository from the CLI.  Try doing it through the CLI by creating a second
  remote called `upstream` that use the URL of the `mlp6` version of the
  resitory, and then try to pull content from that remote into your master.
* Using as a starting point some of the pseudo-code presented in the modularity
  section of the Python Fundamentals lecture, write a Python program that (on a
  git feature branch!):
  + Concatenates all of the individual CSV files--execpt for `mlp6.csv`--into a
    single file called `everyone.csv`.
  + Checks that there are no spaces in the team name that a student specified.
  + Counts how many team names used CamelCase, and prints that could to
    `STDOUT` when the program finishes writing the file.
  + In addition to CSV, JSON is a very popular format. For each of the CSV
    files in the repository, have you code also generate a `$NETID.json`
    formatted file (i.e., for each `$NETID.csv` file, there should also be a
    `$NETID.json` file).
* Submit a Pull Request that has your modular code, along with `everyone.csv`
  and all of the `$NETID.json` files, and assign `suyashkumar` and `mlp6` as
  Reviewers.  As with above, the Pull Request will not be merged in, but will
  be used to evaluate your code, with feedback being given as a "Code Review".
