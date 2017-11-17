class Card(object):
    '''Represents a standard playing card.'''
    def __init__(self, suit: object = 0, rank: object = 2) -> object:
        self.suit = suit
        self.rank = rank
    suit_names = ['♠', '♥', '♣', '♦']
    rank_names = [None, 'A', '2','3','4','5','6','7','8','9','10','J','Q','K']
    def __str__(self):
        return "%s %s" % (Card.suit_names[self.suit], Card.rank_names[self.rank])
for x in range(0,4):
    for y in range(1,14):
        print(Card(x,y))