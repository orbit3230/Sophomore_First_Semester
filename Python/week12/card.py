from random import shuffle

'''
English Comment to just practice writing English comments :)
202110155 김성현
'''
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
    # Constructor of Deck class
    def __init__(self) :
        self.mycardset = []  # card deck list
        for suite in self.suites :  # start from Hearts to Spades
            for value in self.values :  # start from A, 2, 3, ..., to K
                self.mycardset.append(f"{value} of {suite}")  # [A of Hearts, 2 of Hearts, ..., K of Spades]
                
    # shuffle the mycardset(deck) with random.shuffle module
    def shuffleDeck(self) :
        shuffle(self.mycardset)  
        return self  # return the deck itself(maybe shuffled..)
    
    # pop the last card of the deck itself
    def popCard(self) :
        return self.mycardset.pop()  # pop! pop!

# Define a class to create a player
# player will have a name and get cards in their hands
class Player(object) :
    def __init__(self, name) :
        self.nickname = name  # player's name
        self.__cards = []  # player's hand cards
    
    # We can directly access the cards of player with `Player.cards`
    @property
    def cards(self) :
        return self.__cards
    
    # player tostring method. format of "Player {name} has {cards}"
    def __str__(self) :
        info = f"Player {self.nickname} has \t {self.cards}"
        return info  # return tostring of player
        
    # We can append 'a' card to player's hand with assignment `Player.cards = card`
    @cards.setter
    def cards(self, card) :
        self.__cards.append(card)  # append card to player's hand
    
if __name__=='__main__' :
    deck = Deck()  # create a deck instance
    
    print(f"[Current Deck]\n{deck.mycardset}")  # print the current deck (before shuffle)
    print()  # \n
    shuffled_deck = deck.shuffleDeck()  # shuffle the deck and assign (I think assignment is not necessary.. deck has been shuffled)
    print(f"[Shuffled Deck]\n{shuffled_deck.mycardset}")  # print the shuffled deck (after shuffle)
    print()  # \n
    
    player1 = Player("Gil Dong")  # create a player1 instance
    player2 = Player("Chul Su")  # create a player2 instance
    
    for _ in range(4) :  # give players 4 cards one by one
        player1.cards = shuffled_deck.popCard()  # player1 append a card to his hand by @setter
        player2.cards = shuffled_deck.popCard()  # player2 append a card to his hand by @setter
    
    print(player1)  # print player1 in format of "Player {name} has {cards}"
    print(player2)  # print player2 in format of "Player {name} has {cards}"