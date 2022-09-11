from Card import Card
from Deack_of_Cards import Deack_of_Cards
from Player import Player
from random import *

class CardsGame:

    def __init__(self,name1:str,name2:str,Num_cards=26):
        if Num_cards<10 or Num_cards>26:
            Num_cards=26


        self.Deck = Deack_of_Cards()
        self.Cards = Num_cards
        self.Player1 = Player(name1,Num_cards)
        self.Player2 = Player(name2,Num_cards)
        self.list_players = [self.Player1,self.Player2]
        self.New_Game()

    def __str__(self):
        return f"{self.Deck}{self.Cards}{self.Player1}{self.Player2}{self.list_players}"

    def __repr__(self):
       return f"{self.Deck}{self.Cards}{self.Player1}{self.Player2}{self.list_players}"

    def New_Game(self):
        if len(self.Deck.pack)<52:
            raise TypeError("!game is on! You can't shuffle in the middle of a game.")
        self.Deck.Mix_The_Pack()

        for i in self.list_players:
            i.set_hand(self.Deck)

        self.Player1= self.list_players[0]
        self.Player2= self.list_players[1]


    def Winner(self):
        if len(self.Player1.player_cards) > len(self.Player2.player_cards):
            return self.Player1
        elif len(self.Player2.player_cards) > len(self.Player1.player_cards):
            return self.Player2
        else:
            return None