rank_values = dict((rank, i) for i, rank in enumerate('23456789TJQKA'))


def evaluate(cards):

    # Extract ranks and suits from a list of cards (ie. "KC" stands for the King of Clubs)
    ranks, suits = [], []
    for i, card in enumerate(cards):
        ranks[i], suits[i] = card[0], card[1]
    ranks = sorted(ranks, key=lambda rank: rank_values[rank])

    flush = len(set(suits)) == 1
    straight = len(set(ranks)) == 5 and rank_values[ranks[-1]] - rank_values[ranks[-1]] == 4

    # Royal Flush
    if flush and straight and ranks[-1] == 'A':
        return 9

    # Straight Flush
    if flush and straight:
        return 8, ranks[-1]

    # Four of a Kind
    if len(set(suits)) == 2 and len(set(ranks)) == 2:
        return 7,

    # Full House

    # Flush
    if flush:
        return 5, ranks[-1]

    # Straight
    if straight:
        return 4, ranks[-1]

    # Three of a Kind

    # Two pairs

    # One pair

    # High card
    return 0, ranks[-1]
