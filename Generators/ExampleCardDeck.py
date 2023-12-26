from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
Suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
Ranks = tuple(range(2,11)) + tuple('JQKA')

"""
suit_index = card_index // len(Ranks)
rank_index = card_index % len(Ranks)
"""

def card_gen():
    for i in range(len(Suits) * len(Ranks)):
        suit = Suits[i // len(Ranks)]
        rank = Ranks[i % len(Ranks)]
        card = Card(rank, suit)
        yield card

for card in card_gen():
    print(card)

print("--------")
def card_gen():
    for suit in Suits:
        for rank in Ranks:
            yield Card(rank, suit)

for card in card_gen():
    print(card)

class CardDeck:
    Suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    Ranks = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()

    def __reversed__(self):
        return CardDeck.reversed_card_gen()

    @staticmethod
    def card_gen():
        for suit in CardDeck.Suits:
            for rank in CardDeck.Ranks:
                yield Card(rank, suit)

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.Suits):
            for rank in reversed(CardDeck.Ranks):
                yield Card(rank, suit)

deck = CardDeck()
print(list(deck))
print(list(deck))
print(list(reversed(deck)))