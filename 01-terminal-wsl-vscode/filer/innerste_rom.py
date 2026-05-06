import random
import time


MASKER = [
    r'''
       .-""""-.
      /  o  o  \
     |    __    |
      \  '--'  /
       '-.__.-'
      /|  ||  |\
     /_|__||__|_\
    ''',
    r'''
        .-====-.
       /  .  .  \
      |    /\    |
      |  /____\  |
       \  '--'  /
        '-.  .-'
          /__\
    ''',
]

KAPPER = [
    r'''
          /\
         /  \
        /____\
       /|    |\
      /_|____|_\
        /_||_\
       /__||__\
    ''',
    r'''
        .------.
       /  ____  \
      /  /    \  \
     /__/      \__\
       |  ()  |
       |______|
        /_||_\
    ''',
]


def vent():
    time.sleep(0.35)


def vis_intro():
    print(r'''
  ====================================
       DET INNERSTE ROMMET
  ====================================
    ''')
    vent()
    print(random.choice(MASKER))
    vent()
    print(random.choice(KAPPER))
    vent()


def vis_avvist():
    print(r'''
      _________
     |  FEIL   |
     | PASSORD |
     |_________|
         ||
         ||
    ''')
    print("Det var feil passord og du blir kastet ut.")


vis_intro()

forste_passord = input("Første passord: ")
andre_passord = input("Andre passord (trykk Enter for ikke noe passord): ")

if forste_passord == "fidelio" and andre_passord == "":
    print(random.choice(MASKER))
    print("Det som vises her inne egner seg ikke på en jobb-pc")
else:
    vis_avvist()
