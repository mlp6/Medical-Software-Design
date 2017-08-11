# -*- coding: utf-8 -*-
"""mySong module

This module demonstrates a new class that utilizes Composition.
This is an alternative to Inheritance that accomplishes delegation Explicitly,
rather than Implicitly.

References
# https://learnpythonthehardway.org/book/ex40.html
# https://learnpythonthehardway.org/book/ex44.html
# http://docs.python-guide.org/en/latest/writing/structure/
# http://blog.thedigitalcatonline.com/blog/2014/08/20/
python-3-oop-part-3-delegation-composition-and-inheritance/

@author: David Bradway
"""

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
