Regular Expressions (Python)
============================

* ``import re``
  + ``re.match``
  + ``re.search``
  + ``re.findall``
  + ``re.sub``

* Match text string *character* patterns.  We will use "raw" strings that are delineated as r''.

* Exact pattern matches: ``r'abc'``

* Only certain characters ``r'a[bde]c'`` or a range of characters
  ``r'a[b-e]c'``;  you can exclude characters using the ``^``: ``r'a[^bde]c'``.

* Any digit can be represented with ``\d`` and any alphanumeric with ``\w``.
  You can also designante any non-digit as ``\D`` or non-alphanumeric as
  ``\W``.

* Any character can be represented with ``.``

* Characters can be repeated using ``{#}`` or ``{min,max}``.  Can also use
  ``*`` for "0 or more repetitions" or ``+`` for "1 or more repetitions.

* Whitespace: ``\s``  Any non-whitespace: ``\S``

* Starts/Ends with: ``^``/``$``

* [Nested] Group Capture: ``([()])``

* Logic: ``|``

* Great Resources:
  + https://regex101.com/
  + https://regexone.com/
