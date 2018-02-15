# Sphinx Documentation

Sphinx (http://sphinx-doc.org/) is a documentation generation engine for Python
that is extremely powerful and lots of configuration options.  Here's a quick
start to automatically generate API-like documentation using docstrings:

1. ``sphinx-quickstart docs``

This will create a distinct subdirectory (``docs/``) that contains all
documentation.
1. There are lots of options that you will be walked through... defaults are
   usually okay, but be sure to select 'y' for the ``autodoc`` option.
1. add path to ``docs/conf.py``:
```
sys.path.insert(0, os.path.abspath('..'))
```
There is a similar path commented out near the header that you can uncomment
and edit, along with the 2 import statements of the `os` and `sys` modules.
1. Run `sphinx-apidoc -o docs .` from the root level of your project (this
   will sweep through all of the `*.py` files in `.` and create
   corresponding `*.rst` files in `docs/`)
1. `docs/index.rst -> add modules that you'd like included in the documentation
  * Make sure that your docstring have a blank link before the rst `:param:` and
    `:returns:` lines.
  * Make sure to indent your file entries!!  Failure to indent will cause the
    rst-parser to "miss" your files.
  * You may want to add `_build/` to your `.gitignore` files:
1. Run Makefile to generate documentation (e.g., ``make html``).  This will
   create `docs/_build/html` with the default webpage being `index.html`.
