# Docstrings

Docstrings are used to annotate functions to describe:
* One-liner summary of function
* More verbose description of function
* Input parameters
* What is returned

Relevant Python documentation: https://www.python.org/dev/peps/pep-0257/

There are three common docstring styles that can be used:
* [reStructuredText Docstring Format](https://www.python.org/dev/peps/pep-0287/)
* [Numpy Style Python Docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
* [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

`reStructuredText` docstrings are the "default" for most IDEs and code editors,
but it can be difficult to read (IMO).  Numpy and Google-style docstring tend
to be more readable in "raw" form, and can be easily compiled into full
documentation using the
[Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#)
[Sphinx](sphinx.md) extension.

**Example:** https://github.com/mlp6/fem
