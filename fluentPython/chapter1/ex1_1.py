import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]
        # print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def high_spades(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    d = FrenchDeck()
    # print(len(d))
    # print(d[0])
    # print(d[-1])
    # from random import choice
    # print(choice(d))
    for card in sorted(d, key=high_spades):
        print(card)