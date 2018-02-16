# -*- coding: utf-8 -*-
"""main function

This function tries the classes and methods.
"""

import sample.core
import mine


def main():

    # Use the provided class
    bulls_on_parade = sample.core.Song(["They rally around the family",
                                        "With a pocket full of shells"])

    bulls_on_parade.sing_me_a_song()

    print(bulls_on_parade.get_character_count())

    # Use a method that was not passed through
    bulls_on_parade.make_upper()
    bulls_on_parade.sing_me_a_song()

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


if __name__ == '__main__':
    main()
