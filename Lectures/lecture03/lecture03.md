Lecture 03: Python Fundamentals
===============================

Learning Objectives
-------------------
* Create a python virtual environment (conda, pip)
* Writing modular code (script vs. functions)
* Practice test-driven development (TDD) using py.test
* Utilize continuous integration in GitHub (Travis CI)

Class Demo
----------
https://github.com/mlp6/fem

Group Exercise
--------------
* Create a git repository for your group named `bme590lecture03`.
* Create a python virtual environment named `test` that contains the following packages:
  + numpy
  + ipython
  + pytest
  + pytest-cov
  + pytest-pep8
* Activate your virtual environment on your local computer.
* Have one group member create an issue to write a program that:
  + Adds 2 numbers
  + Returns the sum of those numbers is >= 0
  + Returns 0 if the sum of those number is < 0
* Have another group member--before writing the algorithm--write a unit test for the program (not on master!)
  + What tests should your unit tests contain?
* Run the test using `py.test -v`; it should fail.
* Write your summation algorithm and have it pass your tests.
* Once your algorithm passes its tests, create a Pull Request on GitHub to merge it into the master branch (closing your issue).
* Have everyone in the group pull down the latst master branch and run the unit test(s).

Next Lecture
------------
* Implement Travis CI on your repository.
* Write a similar number subtraction method, imposing Travis CI passage before merging a Pull Request into master.
* What happens if your functions receive non-number inputs?
