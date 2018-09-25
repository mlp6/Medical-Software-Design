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
cache:
      - pip
install:
      - pip install -r requirements.txt
script:
      - pytest -v --pep8
```

## Example Repository
https://github.com/mlp6/unit_test_example

# Unit Testing & Continuous Integration II
## Robust Unit Testing
Expanding on the basic idea of testing units of code from last class, we should take some time to consider common ways to write robust unit tests. Generally, tests should cover a wide variety of inputs your "unit" will receive including "bad" inputs (for example, if you were expecting an integer, what happens when someone passes your code a float?). Code written with tests that only test expected use cases will usually fail in unexpected ways in production.

### Bad Inputs

Here's a basic example: let's say you have a function that checks that two fruits are the same:
```py
def is_same_fruit(a, b):
  return a == b
```

What happens when a user types in `" apple"` and you are comparing it to `"apple"` in your code? You should have a test that ensures your `is_same_fruit` function works properly in this scenario. 

Generally you want to ensure that your code will actually behave the way you want it to, even when given odd inputs. You should think about what should happen when your code gets different input types than you were expecting, or inputs that have mistakes (e.g. if you expect a list of numbers, what should happen when you get `[1, 2, 3, "4", "hello"]` as an input? 

We will talk more about handling errors ("exceptions" in python) in the future, but for now you should know that unit testing helps ensure your code behaves well even under odd inputs. 

## Parametrized Testing
It is often helpful to run a test over many different input and exepcted output combinations. `pytest` provides a tool to streamline that process--a decorator called `parametrize`. We will talk more about [decorators](https://www.python-course.eu/python3_decorators.php) later in this class, but they allow your python functions to be augmented (or "decorated") with some additional functionality. The `parametrize` decorator lets us run a test function many times with different inputs and outputs.

We'll go over this more in class, but a simple example is below:

Here's a basic function we want to test:

```py
def add(a, b):
    return a + b
```

And here's a test that tests against many input and expected output combinations:
```py
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add_parametrize(a, b, expected):
    """
    test_add_parametrize is called with all of the input & expected output
    combinations specified in the decorator above.
    """
    assert add(a, b) == expected
```

We can break this down further:
```py
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
```
This part of the code is the "decorator." When the python intrepreter runs this, it knows to augment the function below in a certain way--in this case, it knows to essentially copy the test function below the decorator 3 times and call it 3 times with each set of inputs defined in the list.

Notice the decorator function takes two arguments. A string `"a,b,expected"` and a list of tuples `[(1, 2, 3), (2, 3, 5), ...]`. 

The string must match the named input parameters of your function, which you can see in the function definition (`def test_add_parametrize(a, b, expected):`).

The list of tuples is the list of input & expected output arguments to call the test function with. Each set of arguments is treated as a seperate test case by pytest when you run pytest.

You can see a live example of this working code and play around with it yourself [here](unit_testing/)

