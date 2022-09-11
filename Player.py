from random import *
from Deack_of_Cards import Deack_of_Cards

class Player:
    def __init__(self,name,number_of_cards:int=26):

        if 10 <= number_of_cards <=26:
            self.num_of_cards = number_of_cards
        else:
            self.num_of_cards=26

        self.name = name
        self.player_cards =[]

    def __str__(self):
       return f"player:{self.name},cards:{self.num_of_cards}{self.player_cards}"

    def __repr__(self):
        return f"player:{self.name},cards:{self.player_cards}{self.num_of_cards}"

    #mathod that choos a cards for the player
    def set_hand(self,deck:Deack_of_Cards):
        for i in range(self.num_of_cards):
            card=deck.deal_one()
            self.player_cards.append(card)


  #mathod that take a random card from the deck and return the card

    def get_card(self):
        random_card =choice(self.player_cards)
        self.player_cards.remove(random_card)
        return random_card

 #mathod that add any card to the deck

    def add_card(self,a_card):
        self.player_cards.append(a_card)