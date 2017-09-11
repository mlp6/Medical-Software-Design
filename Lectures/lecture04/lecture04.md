# Lecture 04: Python Fundamentals and Continuous Integration

## Objectives
- Review anaconda and vanilla python setup
- Review virtual environments and their purpose 
- Explanation and example of continuous integration configuration
- Types and exceptions in python (time permitting)
- Complete group excercise from last lecture with unit testing 

## Anaconda & python setup
Check [here](pip-and-conda-install.md) for a review on how to get anaconda and python setup with virtual environments.

## Virtual environments & their purpose
- Virtual environments are a __sandbox__ for your project. 
- When your project's virtual environment is active, your project has access to the all the dependencies you specified in your `environment.yml` or `requirements.txt` at a specific installed version.

When you deactivate this environment and switch to another project, that project's dependencies (at their particular versions) will be made "active" and available for use. You could have the same package used in two different projects at two different versions without a problem because of the encapsulations that environments bring. 

## Continuous Integration (CI)
- All code is automatically tested when pushed up to the remote.
- CI can block pull request merging into master
- CI can also automatically deploy code to production if all safety checks are met
- Travis CI/Circle CI

## In Class Demo
- General python syntax
- Exceptions and types (time permitting)

## Complete Group Activity
Finish up the group activity from [last lecture](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/lecture03/lecture03.md), begin work on a subtraction complement once completed.  
