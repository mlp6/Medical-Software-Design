Text Manipulation
=================

1. Fork this repository, and create a commit that adds your net ID and the net IDs of your in-class parterns here:
  + Net ID:
  + Net ID:

2. Open ``example_text.txt`` compare the ``readline()`` and ``readlines()`` methods.  What is the difference?
  + Answer:

3. What methods are available in the object that is returned from these methods?  (Just take note, you don't need to record them all here.)

4. Take note of the newline characters (``\n``) at the end of each line.  How can you use ``rstrip()`` to get rid of them?
  + Example syntax:

5. Without any extra python modules, count the number of times the word "men" appears in this file.
  + Commit code with a method called ``count_men()``.

6. Create a new file called ``example_text_new.txt`` where each instance of the word "women" is replaced with "WOMEN".
  + Commit code with a new method called ``capitalize_women()``.

7. Write a method to test if a file contains the words "Blue Devil".  You could consider using ``in`` or ``.find()``
  + Commit code with a new method called ``contains_blue_devil()``.

8. Regular expressions open up a wealth of power in matching/searching/replacing text strings... but they have a decent learning curve.
  + https://docs.python.org/3/howto/regex.html
  + https://docs.python.org/3/library/re.html

9. Use ``re.compile()`` to create a regular expression object that finds all instances of the word "said" that do NOT end a sentence.
  + Commit code with new method called ``find_non_terminal_said()``.

10. Use regular expressions to find all words that contain multile vowels in a row, and capatilize that entire word when writing a new file called ``example_text_capped_vowel_words.txt``.
  + Commit code with new method called ``cap_multi_vowel_words()``.
