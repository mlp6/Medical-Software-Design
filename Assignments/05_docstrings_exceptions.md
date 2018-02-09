# Docstrings, Exceptions & Logging

Building on your unit testing assignment, do the following:
* Add exceptions to your functions that handle:
  + `ImportError`
  + `TypeError`
  + `ValueError`
  + A list of all available built-in exceptions are here:
    https://docs.python.org/3/library/exceptions.html
* Make sure that your unit tests cover that the correct exceptions are raised
  appropriately.  (https://docs.pytest.org/en/latest/assert.html)
* Add ReST style docstrings to all of your module functions.  Each team member
  should do this for their method on their feature branch, and this can be done
  on a branch that has already been merged.
  + Make sure that you docstring has a "one-liner".
  + Include input `:param :`
  + Include `:returns :`
  + Include `:raises :`
* Include `logging` in your module to capture:
  1. `info`
  1. `warning`
  1. `debug`
* Setup `sphinx` to generate documentation
  (https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/sphinx.md).
* Extra Credit: Setup your GitHub repository to trigger documentations builds
  on https://readthedocs.org/.
* **Remember to use a git feature branch development workflow to add all of the
  features above.**
* Create an annotated git tag `v2.0.0` when your assignment is complete.
