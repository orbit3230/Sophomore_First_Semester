from random import shuffle

# Define a class to create
# all type of cards
class Cards :
    #global suites, values
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self) :
        pass
    
# Define a class to categorize each card
class Deck(Cards) :
    def __init__(self) :
        self.mycardset = []
        for suite in self.suites :
            for value in self.values :
                self.mycardset.append(f"{value} of {suite}")
                
    def shuffleDeck(self) :
        shuffle(self.mycardset)
        return self
    
    def popCard(self) :
        return self.mycardset.pop()

class Player(object) :
    def __init__(self, name) :
        self.nickname = name
        self.__cards = []
        
    @property
    def cards(self) :
        return self.__cards
    
    def __str__(self) :
        info = f"Player {self.nickname} has \t {self.cards}"
        return info
        
    @cards.setter
    def cards(self, card) :
        self.__cards.append(card)
    
if __name__=='__main__' :
    deck = Deck()
    
    print(f"[Current Deck]\n{deck.mycardset}")
    print()
    shuffled_deck = deck.shuffleDeck()
    print(f"[Shuffled Deck]\n{shuffled_deck.mycardset}")
    print()
    
    player1 = Player("Gil Dong")
    player2 = Player("Chul Su")
    
    for _ in range(4) :
        player1.cards = shuffled_deck.popCard()
        player2.cards = shuffled_deck.popCard()
    
    print(player1)
    print(player2)