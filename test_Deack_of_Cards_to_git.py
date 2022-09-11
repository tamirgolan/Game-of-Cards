from unittest import TestCase, mock
from Deack_of_Cards import Deack_of_Cards
from Card import Card
from Player import Player
from unittest.mock import patch


class TestDeack_of_Cards(TestCase):

    def setUp(self):
        self.Deck1 = Deack_of_Cards()
        self.Deck1.list_suit=["♠", "♥", "♦", "♣"]
        self.Deck1.list_value=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def tearDown(self):
        return f"TearDown"

    # test if the list[i] contain what they are need to
    def test_init_suit_in(self):
        self.assertIn("♠",self.Deck1.list_suit)
        self.assertIn("♥", self.Deck1.list_suit)
        self.assertIn("♦", self.Deck1.list_suit)
        self.assertIn("♣", self.Deck1.list_suit)

    # test if the list[i] equal to what its need to be
    def test_init_suit_Eq(self):
        self.assertEqual(self.Deck1.list_suit[0],"♠")
        self.assertEqual(self.Deck1.list_suit[1],"♥")
        self.assertEqual(self.Deck1.list_suit[2],"♦")
        self.assertEqual(self.Deck1.list_suit[3],"♣")

    # test if the len of the list is right len(list_suit) cant be !=4
    def test_suit_len(self):
        self.assertNotEqual(len(self.Deck1.list_suit),5)
        self.assertNotEqual(len(self.Deck1.list_suit),3)


    def test_init_suit_in_invalid(self):
        self.assertNotIn(1,self.Deck1.list_suit)

    # test if there is no change in the list index
    def test_init_suit_eq_invalid_index(self):
        self.assertNotEqual(self.Deck1.list_suit[0],"♣")

    # test if the list[i] contain what they are need to
    def test_init_value_in(self):
        self.assertIn("2",self.Deck1.list_value)
        self.assertIn("3", self.Deck1.list_value)
        self.assertIn("4", self.Deck1.list_value)
        self.assertIn("5", self.Deck1.list_value)
        self.assertIn("6", self.Deck1.list_value)
        self.assertIn("7", self.Deck1.list_value)
        self.assertIn("8", self.Deck1.list_value)
        self.assertIn("9", self.Deck1.list_value)
        self.assertIn("10", self.Deck1.list_value)
        self.assertIn("Jack", self.Deck1.list_value)
        self.assertIn("Queen", self.Deck1.list_value)
        self.assertIn("King", self.Deck1.list_value)
        self.assertIn("Ace", self.Deck1.list_value)

    # # test if the list[i] equal to what its need to be
    def test_init_value_Eq(self):
        self.assertEqual(self.Deck1.list_value[0],"2")
        self.assertEqual(self.Deck1.list_value[1], "3")
        self.assertEqual(self.Deck1.list_value[2], "4")
        self.assertEqual(self.Deck1.list_value[3], "5")
        self.assertEqual(self.Deck1.list_value[4], "6")
        self.assertEqual(self.Deck1.list_value[5], "7")
        self.assertEqual(self.Deck1.list_value[6], "8")
        self.assertEqual(self.Deck1.list_value[7], "9")
        self.assertEqual(self.Deck1.list_value[8], "10")
        self.assertEqual(self.Deck1.list_value[9], "Jack")
        self.assertEqual(self.Deck1.list_value[10], "Queen")
        self.assertEqual(self.Deck1.list_value[11], "King")
        self.assertEqual(self.Deck1.list_value[12], "Ace")

    # test if there is invalid things in the list
    def test_init_value_in_invalid(self):
        self.assertNotIn("1", self.Deck1.list_value)
        self.assertNotIn("14", self.Deck1.list_value)


    # test if there is no change in the list index
    def test_init_value_eq_invalid_index(self):
        self.assertNotEqual(self.Deck1.list_value[0],"3")

    # test if the len of the list is right len(list_value) cant be !=13
    def test_list_value_len(self):
        self.assertNotEqual(len(self.Deck1.list_value), 12)
        self.assertNotEqual(len(self.Deck1.list_value), 14)


    # test if the len of the list is right len(pack) cant be !=52
    def test_peck_len(self):
        self.assertNotEqual(len(self.Deck1.pack),51)
        self.assertNotEqual(len(self.Deck1.pack),53)

    # test if there is no change in the list index
    def test_init_peck_eq_invalid_index(self):
        self.assertNotEqual(self.Deck1.pack[0], "3♠")

    # testing there is no cards duplicate
    def test_init_peck_double_cards(self):
        self.assertNotEqual(self.Deck1.pack[0],self.Deck1.pack[13])
        self.assertNotEqual(self.Deck1.pack[13], self.Deck1.pack[26])
        self.assertNotEqual(self.Deck1.pack[26], self.Deck1.pack[39])
        self.assertNotEqual(self.Deck1.pack[39], self.Deck1.pack[51])

    # testing there is no cards duplicate
    def test_init_peck_double_cards_2(self):
        for i in self.Deck1.pack:
            self.assertEqual(self.Deck1.pack.count(i),1)


    # testing if it is mix the pcak
    def test_mix_the_pack_before_game(self):
        self.First = self.Deck1.pack[0]
        self.Deck1.Mix_The_Pack()
        self.assertNotEqual(self.Deck1.pack[0], self.First)


    # testing if it is mixing the pack when pack len is not 52
    def test_mix_the_pack_while_playing(self):
        self.First = self.Deck1.pack[0]
        self.Deck1.pack.remove(self.Deck1.pack[-1])
        self.Deck1.Mix_The_Pack()
        self.assertEqual(self.Deck1.pack[0], self.First)

    # check if the card is removed from the pack
    def test_deal_one(self):
        self.First = self.Deck1.pack
        self.Deck1.deal_one()
        self.assertTrue(len(self.Deck1.pack) == 51)

    # check if the functaion take the card out of pack
    def test_deal_one_card_not_in(self):
        self.assertNotIn(self.Deck1.deal_one(),self.Deck1.pack)

    # check if deal one return the card
    def test_deal_one_return_card(self):
        D_card=Card("7","♠")
        with patch('Deack_of_Cards.Deack_of_Cards.deal_one') as mock_c:
            mock_c.return_value=D_card
            self.assertEqual(self.Deck1.deal_one(),D_card)



