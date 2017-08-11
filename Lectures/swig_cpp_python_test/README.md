# swig_cpp_python_test
simple test to generate Python module from C++ class

## Compiling
Ideally you should just be able to type ``make`` and the ``Makefile`` should
drive the bus.  You will need to update the ``ANACONDA3`` path for your local
install, and potentially paths for SWIG and C++ build tools.

## Python Usage
You can use the compiled code in python by one of the following two approaches:
```
import calc
calc.calc_add_two(1, 2)
```

```
from calc import calc_add_two as add_two
add_two(1, 2)
```
## Py.Test & GTest (Docker GitLab Runner)
This repository also demonstrates simple implementations of CI builds using:
1. ``py.test`` using an anaconda3 Docker image
2. Google Test (``gtest``) using a stock Fedora 24 Docker image
