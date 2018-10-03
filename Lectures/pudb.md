# Debugging (pdb/pudb)

* Can put breakpoints in code to see state of variables

* Not good practice to keep debugger always active

* Set breakpoint with `pudb.set_trace()`.  Example code: [example_pudb.py](example_pudb.py)

* Halts execution & allows you to inspect entire variable workspace

* Click `!` -> puts you in interactive `ipython` environment that allows you to
  see variables & work with them (can manually test things out and see what
  happens)

* When done, exit iPython -> back in debugger

* Can read more about `pudb` here: https://documen.tician.de/pudb/starting.html

* If `pudb` module is absent, can set a conditional to ignore any `pudb` calls.

* Compare `pudb` terminal usage with PyCharm debugger implementation
  (https://www.jetbrains.com/help/pycharm/debugging-code.html)
