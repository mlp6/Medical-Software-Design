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

## How do we deal with exceptions gracefully?
Syntax errors are caught and corrected with our unit tests and development testing, but exceptions can happen during device function.  We don't want our code to abruptly stop when an exception occurs, but instead, we want a planned procedure to deal with exceptions.

``try/except`` allows us to "try" to execute a segment of code, and if an exception is raised, then the "except" code is executed, and our "excepts" can be tailored to the specific exception error.

Example code:  [example_try_except.py](example_try_except.py)

## Pseudo-code example for running out of storage space

```
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
