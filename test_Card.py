from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.C_1=Card("Ace","♠")

    def tearDown(self):
        print("tearDown")


    # בדיקת ערכים תקינים
    def test_init_valid(self):
        self.assertEqual(self.C_1.Suit,"♠")
        self.assertEqual(self.C_1.Value,"Ace")

    # בדיקת ערכים לא תקינים
    def test_init_invalid_suit_invalid_type(self):
        with self.assertRaises(TypeError):
            C_2=Card("2",4)

    def test_init_invalid_value_invalid_type(self):
        with self.assertRaises(TypeError):
            C_2=Card(1,"Club")

    # בדיקת קלף גדול לפי ערך, על ידי True
    def test_gr_valid_bigger_value(self):
        c_1 = Card("Ace","♣")
        c_2 = Card("2","♣" )
        self.assertTrue(c_1 > c_2)

    # בדיקת קלף קטן לפי ערך,על ידי True
    def test_gr_valid_smaller_value(self):
        c_1 = Card("Ace", "♣")
        c_2 = Card("2", "♣")
        self.assertTrue(c_2<c_1)

    # בדיקת קלף גדול לפי סמל ,על ידי True
    def test_gr_valid_suit(self):
        c_1 = Card("2", "♥")
        c_2 = Card("2", "♠")
        self.assertTrue( c_1 > c_2)

    # בדיקת קלף קטן לפי סמל ,על ידי False

    def test_gr_valid_suit(self):
        c_1 = Card("2", "♥")
        c_2 = Card("2", "♠")
        self.assertFalse(c_1 < c_2)






