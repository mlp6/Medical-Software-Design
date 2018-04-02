# Debugging using pdb or pudb

Python debugger! 
Can put breakpoints in code to see state of variables

Can see what packages are installed with 
`pip freeze`

* Useful:
If you want to create a `requirements.txt` file from a set of packages that you have just pip installed (without virtual environemnt), you can run  `pip freeze > requirements.txt`

Not good practice to keep debugger always active

Set breakpoint with...
`pudb.set_trace()`
Halts execution & allows you to inspect entire variable workspace

Click `!` -> puts you in interactive iPython environment that allows you to see variables & work with them (can manually test things out and see what happens)

When done, exit iPython -> back in debugger

Can read more about [pudb here](https://documen.tician.de/pudb/starting.html)

If pudb module is absent, can set a conditional to ignore any pudb calls
