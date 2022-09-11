from Card import Card
from Deack_of_Cards import Deack_of_Cards
from Player import Player
from CardsGame import CardsGame
from random import *





#תוכנית ראשית :
#get a name for a player frome the user and return the ditels

#warl Game

name_1 = input("hello,pleas enter a name for a player:")
name_2 = input("hello,pleas enter a name for a player:")

game_1=CardsGame(name_1,name_2)



for i in range(10):
    card_1=game_1.Player1.get_card()
    card_2=game_1.Player2.get_card()
    print(f"{name_1} card for this round:[{card_1}] {name_2} card for this round: [{card_2}]")

    if card_1 > card_2:
        game_1.Player1.add_card(card_1)
        game_1.Player1.add_card(card_2)
        print(f"{name_1} you won the fight!!  not in the W A R")

    elif card_1 < card_2:
        game_1.Player2.add_card(card_1)
        game_1.Player2.add_card(card_2)
        print(f"{name_2} you won the fight!!  not in the W A R ")


# use the Winner to print the Winner
winner=game_1.Winner()
if winner == None:
    print("Game over , no winner its a Tie ")

else: print(f"well done {winner} , you won the W A R ! ")