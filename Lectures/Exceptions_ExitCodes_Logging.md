# Try/Except[/Finally], Warnings, Exit Codes, Logging

Making our code more robust...

There are two primary types of python "errors":

1. Syntax Errors
2. Exceptions

## Syntax Errors

Syntax errors violate the coding syntax, meaning that python cannot interpret you code.  For example:

```
print "The sky is blue."
```

This yields the following syntax error output:

```
print "The sky is blue."
                       ^
SyntaxError: Missing parentheses in call to 'print'
```

The arrow points to where the syntax is invalid, and the error message [attempts to] convey what is wrong.

Relevant Python documentation: https://docs.python.org/3/tutorial/errors.html

## Exceptions

In contrast, Exceptions are raised when you have valid syntax, but an error occurs when your command attempts to run.  For example:

```
f = open('file.bin', 'rb')
```

While this command is syntactically correct, if the file ``file.bin`` does not exist, then this command will raise an exception:

```
FileNotFoundError: [Errno 2] No such file or directory: 'file.bin'
```

Other common exception errors are:
  * ``ZeroDivisionError``
  * ``NameError`` (trying to use a variable name that is not defined)
  * ``TypeError`` (mixing conflicting types of data in an operation, or passing a function variable input type that is not supported)
  * ``AssertionError``
  * ``ImportError``
  * ``IOError``
  * ``EOFError``

There is a comprehensive list of built-in exceptions here: https://docs.python.org/3/library/exceptions.html

## How do we raise exceptions?
To raise an exception in python to indicate an error, simply:                                                                                                                                                                          
```py                                                                                                                                                                                                                                  
raise ValueError("This message string gives more information and context about why this was raised.")                                                                                                                                  
```
You might want to raise an exception if inputs to a function are the wrong
type. For example:

```py                                                                                                                                                                                                                                  
# This function may raise a TypeError if called with certain args:                                                                                                                                                                     
def add(a, b):                                                                                                                                                                                                                         
    if type(a) is not int or type(b) is not int:                                                                                                                                                                                       
        raise TypeError("Inputs must be python ints")                                                                                                                                                                                  
    return a + b                                                                                                                                                                                                                       
```
If the inputs to this function are not ints, we will notified the caller of
this function (and the program as a whole) that an error condition has occured
(and in particular it's a `TypeError`) by raising this exception. If we do not
handle this exception then the program will crash. 

Generally, you should raise exceptions in your code to signal that some sort of error has occured in your function (like inputs being the wrong type) that you cannot proceed with execution of the code. Generally, you'll be raising exceptions from functions (say, `add`) and the goal of raising an exception is to notify the _caller_ of add (usually your `main` function) that something has gone wrong and `add` cannot proceed as intended. 

## What happens when an exception is raised?
When you raise an exception, code execution stops at that point and the exception propogates up to the caller of the function an exception was thrown in. The function does not return anything. The caller of your function can deal with the exception (for example, re-prompting the user for proper input) or it can allow the exception to propogate through the program until it crashes with an error message. 

## How do we deal with exceptions gracefully?
Syntax errors are caught and corrected with our unit tests and development testing, but exceptions can happen during device function.  We don't want our code to abruptly stop when an exception occurs, but instead, we want a planned procedure to deal with exceptions.

``try/except`` allows us to "try" to execute a segment of code, and if an exception is raised, then the "except" code is executed, and our "excepts" can be tailored to the specific exception error.

Example code:  [example_try_except.py](example_try_except.py)

## Pseudo-code example for running out of storage space

```py
def main():
    import errno
    while True:
        try:
            do_stuff()
        except IOError:
            if errno.ENOSPC:
                try:
                    push_data_to_web()
                except:
                    print("You're going to lose data, but prioritizing staying online.")
                clear_stuff_up()
            else:
                figure_out_what_else_might_be_wrong()

```

## Testing that your code throws an Exception
You will want to test that your code throws certain exceptions when given certain inputs or put in certain situations. This can be done as follows:
```py
def test_something():
    import pytest
    with pytest.raises(TypeError):
        func_that_raises_type_error(bad_input)
```

## Warnings
Items that require some user attention, but do not demand raising a full exception.  The ``warnings`` package provides this functionality.

## Errors that Demand Termination
``sys.exit()`` is the most common way to terminate program execution, and it is most useful to provide a returned exit status to indicate why termination occurred.

There is a dedicate module to system error symbols: https://docs.python.org/3/library/errno.html

Example code: [example_warning_exit.py](example_warning_exit.py)

## Logging
Device logs can be invaluable to confirm expected performance and to help debug when things go wrong.  Python has a ``logging`` module that provides rich functionality.  Logs can be kepy at varying "levels"; more verbose logs can provide more information, but at the expense of being much larger and more difficuly to parse.  Logs typically have more verbose debugging modes compared to less descriptive runtime modes.

Standard levels in the logging module include:
* DEBUG
* INFO
* WARNING (defalt level if not specified)
* ERROR
* CRITICAL

https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

Example code: [example_logging.py](example_logging.py)

Elegant way to use decorators to clean up the logging syntax: https://hackaday.com/2018/08/31/an-introduction-to-decorators-in-python/

# Excercise 
Write a program that sums up all of the numbers in a file on your machine. The text file _should_ contain one number per line in the file. Some lines of the file may not contain numbers (which would lead to a `ValueError`), you should be able to handle this and simply skip over those lines in your sum. Sometimes the file may not exist (`FileNotFoundError`), you should also handle this properly. The text files could look like the following:

```
1
20
blah
20
```
