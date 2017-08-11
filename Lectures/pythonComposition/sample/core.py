# -*- coding: utf-8 -*-
"""Song module

This module demonstrates a given class
"""


class Song(object):
    """This is a Song class.

    __init__ sets the lyrics attribute.

    Attributes:
        lyrics (list): a list of strings indicating lines of lyrics
                       of the song.

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
