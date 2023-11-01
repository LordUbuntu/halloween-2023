# Jacobus Burger (2023)
# Happy Halloween
from time import sleep
from os import system, name
from itertools import count


frames = [
    "( つ ･ᴗ･)つ",
    "ς ( ･ᴗ･ ς )",
]
lyrics = "It did the mash\nIt did the ~~MONSTER MASH~~\nIt was a smash\nIt was a ~~GRAVEYARD SMASH~~"


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':
    for i in count(1):
        clear()
        print(frames[i % 2])
        print(lyrics)
        sleep(0.429)
