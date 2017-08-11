# Python Class Class

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/davidbradway/pythoncomposition)

## Object oriented programming in Python, Outline (2016-09-22)

- Relate Python Classes to Modules
- How to define a Class
- Attributes
- Methods
- Objects
- Delegation
  - Inheritance
  - Composition

## Dictionaries, Modules, and Classes Compared

```python
# Dictionary

myDictionary = {'myKey': 'myValue1'}
print(myDictionary['myKey'])

# Module

# Built-in module
import os
print(os.getcwd())

# User-written module
### Begin myModule.py
def myFunction():
    return 'myReturnValue2'

myVariable = 'myValue2'
### End myModule.py

import myModule
print(myModule.myFunction())
print(myModule.myVariable)
```

Based on [Ex40][1] 

## Define a class

- Methods: actions to **do** on / to / with an object of this class
- Attribues: the properties / variables / data associated with an object of this class
- `__init__` 
  - Can take multiple arguments, or just the automatic one, traditionally called 'self'.
  - A ['magic' method][2] that initializes the class, which is called when a new object is Instantiated (created)
  - Sometimes called a 'dunder' for the double-underscores
  - Other 'dunders' are `__iter__`, `__call__`, `__new__`, `__del__`, and more.

```python
class myClass(object):
    """This is a myClass class.

    __init__ sets the myAttribute attribute.

    Attributes:
        myAttribute (str): string attribute

    """

    def __init__(self, myArgument = 'myDefault'):
        self.myAttribute = myArgument

    def myMethod(self):
        """ returns a literal string value
 
        :return: liteal string [str]
        """

        return 'myReturnValue3'
```

See the [Python Docs][3]

## Object
- An Object is an *Instance* (manifestation) of the given Class (template / blueprint)
- Objects can be passed to/from functions, etc. (everything in Python is an object!)
- Different Objects don't know the contents of each others' Attributes

```python
myObject = myClass()
print(myObject.myMethod())
print(myObject.myAttribute)

# To recap, different ways to access things of other things:

# dict-style key-value pairs
myDictionary['myKey']

# module-style functions and variables
myModule.myFunction()
myModule.myVariable

# class-style methods and attributes
myObject.myMethod()
myObject.myAttribute
```

## Delegation

- So you Don't Repeat Yourself (DRY), let each Class do what it knows best
- Use a general or abstract base Class with common Methods and Attributes
- Create more specific concrete Classes that use the base Class
  - Reuse the common Methods and Attributes via 'delegation'
  - Add or redefine Methods and Attributes that are unique
- Delegation can be accomplished via 'Inheritance' or 'Composition'

### Inheritance

- Specific object "is a" generic object. (Apple is a fruit)
- Child *inherits* **ALL** Methods and Attributes from all (1, 2 or more) parents and from *their* parents

```python
class Animal(object):
    """This is an Animal class.

    __init__ sets the kingdom attribute.

    Attributes:
        kingdom (str): a string indicating the kingdom of the animal.
    """

    def __init__(self):
        self.kingdom = 'Animalia'

class Lion(Animal):
    """This is a Lion class.

    __init__ sets the attributes

    Attributes:
        genus (str): a string indicating the genus
        species (str): a string indicating the species
        has_mane (bool): a boolean indicating if it has a mane
    """
    def __init__(self):
        super(Lion, self).__init__()
        self.genus = 'Panthera'
        self.species = 'Tigris'
        self.has_mane = True

    def says(self):
        """ prints what it says
        """

        print('Roar')

class Tiger(Animal):
    """This is a Tiger class.

    __init__ sets the attributes

    Attributes:
        genus (str): a string indicating the genus
        species (str): a string indicating the species
        has_stripes (bool): a boolean indicating if it has stripes
    """
    def __init__(self):
        super(Tiger, self).__init__()
        self.genus = 'Panthera'
        self.species = 'Leo'
        self.has_stripes = True

    def says(self):
        """ prints what it says
        """

        print('Grr')

# Multiple Inheritance!
class Liger(Lion, Tiger):
    """This is a Liger class.

    __init__ sets the attributes

    Attributes:
        species (str): a string indicating the species
    """
    def __init__(self):
        super(Liger, self).__init__()
        self.species = 'Leo x Tigris'

    def says(self):
        """ prints what it says
        """

        print('Grroar?')

hercules = Liger()

# Access attributes of Lion Class
print(hercules.has_mane)
print(hercules.genus)

# Access attribute of Animal Class (via Lion Class)
print(hercules.kingdom)

# Access attribute of Tiger Class
print(hercules.has_stripes)

# Access overloaded method of Liger Class
hercules.says()
```

### Composition

- New Object "has an" Other Object that does some of its work
- New Object gets **ONLY** the methods that are explicitly mapped from the Other Object's class
- As an example, based on [Ex44][4], we will walk through `sample/core.py`, `mine.py`, and `mymain.py` in this repo.
- Before we dive in, consider `sample/core.py` a module that someone gives you:

```python
### Start sample/core.py
# -*- coding: utf-8 -*-
"""Song module

This module demonstrates a given class
"""


class Song(object):
    """This is a Song class.

    __init__ sets the lyrics attribute.

    Attributes:
        lyrics (list): a list of strings indicating lines of lyrics of the song.

    """

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """ print song lyrics
        """
        for line in self.lyrics:
            print(line)

    def get_character_count(self):
        """ count characters in lyrics
 
        :return: character count [int]
        """
        character_count = 0
        for line in self.lyrics:
            character_count = character_count + len(line)
        return character_count

    def make_upper(self):
        """ make lyrics all uppercase
        """
        for idx, line in enumerate(self.lyrics):
            self.lyrics[idx] = line.upper()
### End sample/core.py
```

- Try the methods given:

```python
import sample.core

# Use the provided class
bulls_on_parade = sample.core.Song(["They rally around the family",
                                    "With a pocket full of shells"])

bulls_on_parade.sing_me_a_song()

print(bulls_on_parade.get_character_count())

bulls_on_parade.make_upper()
bulls_on_parade.sing_me_a_song()
```

- We want to extend the features of that Class without touching the code given to us.
- We can use Inheritance or Composition to put new features in a derived Class.
- Why not Inheritance (this time)?
  - Let's say we want explicit control over which Methods are exposed in new Class and want to leave one out.
  - Also, Inheritance can get rather complicated in big projects, multiple layers of Classes, and/or multiple parents.
- So here is our new Class, saved in the `mine.py` module, which creates a Song Object as its Attribute, using Composition:

```python
### Start mine.py
import sample.core

class mySong(object):
    """This is a mySong class.

    __init__ sets the song attribute.

    Attributes:
        song (Song): a song of Class Song from the sample.core module

    """

    def __init__(self, lyrics):
        self.song = sample.core.Song(lyrics)

    # Redefine this method, adding exclamation points to each line!
    def sing_me_a_song(self):
        """ print song lyrics
        """
        for line in self.song.lyrics:
            print(line+"!")

    # Pass this method through unchanged
    def get_character_count(self):
        """ count characters in lyrics

        :return: character count [int]
        """
        return self.song.get_character_count()

### End mine.py
```

- Notice we didn't expose the `make_upper()` Method.
- Try using the methods of our composed Class (as done in the `mymain.py` script):

```python
import mine

# Use our custom class utilizing Composition
happy_bday = mine.mySong(["Happy birthday to you",
                          "I don't want to get sued",
                          "So I'll stop right there"])

# Use overloaded method
happy_bday.sing_me_a_song()

# Use method that was passed through
print(happy_bday.get_character_count())

# Try the method which was not passed through
try:
    happy_bday.make_upper()
# NOTE: new syntax!
except AttributeError as err:
    print("Didn't pass that method through in new class: {0}".format(err))
```

## Questions?

## More?

See a good Lynda.com tutorial on [Python 3 Essentials][5]

[1]: https://learnpythonthehardway.org/book/ex40.html 
[2]: http://www.rafekettler.com/magicmethods.html
[3]: https://docs.python.org/3.5/tutorial/classes.html
[4]: https://learnpythonthehardway.org/book/ex44.html
[5]: https://www.lynda.com/Python-tutorials/Understanding-classes-objects/62226/70985-4.html
