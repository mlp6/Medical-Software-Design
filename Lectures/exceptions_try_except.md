# Exceptions & Try/Except in Python

## Raising Exceptions
In python, raising [exceptions](https://docs.python.org/3/tutorial/errors.html) allows code to indicate that an error has occured and that program execution should not proceed unless the error is _handled_. Raised exceptions that are not handled will cause the program to crash and yield the stack trace in the console that many of you have likely seen by now. There are many ["built-in" exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that can be raised in python including `ValueError`, `TypeError`, `ImportError`, and more.

To raise an exception in python to indicate an error, simply:
```py
raise ValueError("This message string gives more information and context about why this was raised.")
```

You might want to raise an exception if inputs to a function are the wrong type. For example:

```py
# This function may raise a TypeError if called with certain args:
def add(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("Inputs must be python ints")
    return a + b
```
If the inputs to this function are not ints, we will notified the caller of this function (and the program as a whole) that an error condition has occured (and in particular it's a `TypeError`) by raising this exception. If we do not handle this exception then the program will crash.

## Handling exceptions (try/except)
If we anticipate that a block of code will raise an exception that we want to handle in a particular way, we can use `try`/`except` blocks to catch the exception and specify how to proceed depending on which type of exception is thrown. For example:

```py
a = "string"
b = 1
try:
    add(a, b) # this code might raise an exception
except TypeError:
    # Handle the TypeError as appropiate
    print("You must enter integers") # tell the user?
except TimeoutError:
    # in this case, we should do more than just print a message:
    # maybe wait a little and retry the call?
    wait_and_retry(...)
```

Generally the __caller__ of a function that might raise an exception is responsible for handling that exception in a try/except block as shown above. 
