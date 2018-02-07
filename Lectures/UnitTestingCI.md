# Unit Testing & Continuous Integration

## Unit Testing
* Test-Driven Development (TDD)
  + Write your tests before your code.
  + Verify function when generating new code.
  + Verify new functions / changes don't break previous functionality.
* Python unit testing frameworks:
  + `unittest`
  + `py.test` (what we will use)
  + `nose`
* `requirements.txt`
  + `pytest`
  + `pytest-pep8`
  + `pytest-cov`
* What are "good" units?
  + Functions/methods must be written with a very specific and narrow
    functional scope in mind.
  + If your function does "too much" and requires a very divergent set of
    tests, then that function should be broken up into individual functions,
    each with a more defined scope.
  + Your tests should include enough input configurations to cover all
    expected use cases.  Edge cases are important!  These tests will be
    expanded in the future to include graceful handling of exceptions, invalid
    inputs, etc.

## Continuous Integration (Travis CI)
* https://docs.travis-ci.com/user/getting-started
* Must enable Travis CI integration for your account *and* for specific
repositories!
* `.travis.yml` configuration file
```
language: python
python:
      - "3.6"
install:
      - pip install -r requirements.txt
script:
      - pytest -v --pep8
