# I take advantage of the fact that in Python (2, 3) > (1, 4), lists are comparable with priority
# given to the elements in a increasing fashion

rank_values = dict((rank, i) for i, rank in enumerate('23456789TJQKA'))


def has_pair(ranks, ignored_rank=None):
    max_rank = None
    for i, rank in enumerate(ranks[:-1]):
        if rank != ignored_rank and rank == ranks[i+1]:
            max_rank = rank
    return max_rank


def has_three_of_a_kind(ranks):
    for i in range(3):
        if ranks[i] == ranks[i+1] == ranks[i+2]:
            return ranks[i]
    return None

def has_four_of_a_kind(ranks):
    for i in range(2):
        if ranks[i] == ranks[i+1] == ranks[i+2] == ranks[i+3]:
            return ranks[i]
    return None


def get_high_card(ranks, ignored_ranks=()):
    return [rank for rank in ranks if rank not in ignored_ranks][-1]


def evaluate(cards):

    # Extract ranks and suits from a list of cards (ie. "KC" stands for the King of Clubs)
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    ranks = sorted(ranks, key=lambda rank: rank_values[rank])

    flush = len(set(suits)) == 1
    straight = len(set(ranks)) == 5 and rank_values[ranks[-1]] - rank_values[ranks[0]] == 4

    # Royal Flush
    if flush and straight and ranks[-1] == 'A':
        return 9

    # Straight Flush
    if flush and straight:
        return 8, rank_values[ranks[-1]]

    four_of_a_kind = has_four_of_a_kind(ranks)

    # Four of a Kind
    if four_of_a_kind:
        return 7, rank_values[four_of_a_kind]

    three_of_a_kind_rank = has_three_of_a_kind(ranks)
    pair_rank = has_pair(ranks, three_of_a_kind_rank)

    # Full House
    if three_of_a_kind_rank and pair_rank:
        return 6, rank_values[three_of_a_kind_rank], rank_values[pair_rank]

    # Flush
    if flush:
        return 5, rank_values[ranks[-1]]

    # Straight
    if straight:
        return 4, rank_values[ranks[-1]]

    # Three of a Kind
    if three_of_a_kind_rank:
        return 3, rank_values[three_of_a_kind_rank]

    # Two pairs
    if pair_rank:
        second_pair_rank = has_pair(ranks, ignored_rank=pair_rank)
        if second_pair_rank:
            pair_ranks = sorted((pair_rank, second_pair_rank), key=lambda rank: rank_values[rank])
            return 2, rank_values[pair_ranks[1]], rank_values[pair_ranks[0]], rank_values[get_high_card(ranks, ignored_ranks=pair_ranks)]

    # One pair
    if pair_rank:
        return 1, rank_values[pair_rank], rank_values[get_high_card(ranks, ignored_ranks=[pair_rank])]

    # High card
    return 0, rank_values[get_high_card(ranks)]


answer = 0

for line in open('p054_poker.txt').read().splitlines():
    cards = line.split(' ')
    hand_one = cards[:5]
    hand_two = cards[5:]
    if evaluate(hand_one) > evaluate(hand_two):
        answer += 1

print(answer)
