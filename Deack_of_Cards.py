from Card import Card
from random import *

class Deack_of_Cards:


    def __init__(self):
        self.list_suit = ["♠", "♥", "♦", "♣"]
        self.list_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.pack = []

        for i in self.list_suit:
            for j in self.list_value:

                self.pack.append(Card(j,i))

    def __str__(self):
      return f"{self.pack}{self.list_suit}{self.list_value}"

    def __repr__(self):
        return f"{self.pack}{self.list_suit}{self.list_value}"

    # shuffle the pack
    def Mix_The_Pack(self):
        if len(self.pack)<52:
            print("!game is on! You can't shuffle in the middle of a game. ")
        elif len(self.pack) == 52:
            shuffle(self.pack)

    # pop after shuffle means random card is out

    def deal_one(self):
        R_c=choice(self.pack)
        self.pack.remove(R_c)
        return R_c


