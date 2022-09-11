class Card:
    # class that create cards in the game

    def __init__(self,Value,Suit):
        if type(Value)!= str:
            raise TypeError("type value must ber str")
        if type(Suit)!= str:
            raise TypeError("type Suit must ber str")
        self.Value=Value
        self.Suit=Suit

    def __str__(self):
        return f"{self.Value}{self.Suit}"

    def __repr__(self):
        return f"{self.Value}{self.Suit}"

    def __gt__(self, other):
        # global In_V1, In_V2, In_S2, In_S1
        self.list_S = ["♠", "♥", "♦", "♣"]
        self.list_V = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


        # the index of the suit and value will decide how is bigger
        for i in range(len(self.list_S)):
            if self.Suit==self.list_S[i]:
                In_S1 = i


        for i in range(len(self.list_S)):
            if other.Suit==self.list_S[i]:
                In_S2 = i

        for i in range(len(self.list_V)):
            if self.Value==self.list_V[i]:
                In_V1 = i

        for i in range(len(self.list_V)):
            if other.Value==self.list_V[i]:
                In_V2 = i

        if In_V1 > In_V2:
            return True
        elif In_V1 == In_V2:
            if In_S1 > In_S2:
                return True
            else:
                return False
        else:
            return False