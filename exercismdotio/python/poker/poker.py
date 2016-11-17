import logging, itertools, functools
#import pdb
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

THE_RANK = 0
THE_SUIT = 1

RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
HAND_CATEGORIES = ('high card', 'one pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush', 'five of a kind')

def poker(allHands):
	logging.debug(allHands)

	# sort the ranks
	allHands.sort(key=functools.cmp_to_key(compareHands)) # a bit of magic here, if you don't know about comparator functions
	logging.debug(allHands)

	# find winning rank, return all hands that match this rank
	allRanks = [getRank(hand) for hand in allHands]
	winningRank = allRanks[-1]
	return allHands[-len([rank for rank in allRanks if rank == winningRank]):] # ¯\_(ツ)_/¯




def compareHands(hand1, hand2):
	rank1 = getRank(hand1)
	rank2 = getRank(hand2)
	if HAND_CATEGORIES.index(rank1[0]) > HAND_CATEGORIES.index(rank2[0]):
		return 1
	elif HAND_CATEGORIES.index(rank1[0]) < HAND_CATEGORIES.index(rank2[0]):
		return -1
	else:
		if RANKS.index(rank1[1]) > RANKS.index(rank2[1]):
			return 1
		elif RANKS.index(rank1[1]) < RANKS.index(rank2[1]):
			return -1
		else:
			return 0


def getRank(hand): # `hand` is a list of strings. e.g. ['2S', '8H', '6S', '8D', 'JH']
	# check if hand is "five of a kind"
	if hand[0][THE_RANK] == hand[1][THE_RANK] == hand[2][THE_RANK] == hand[3][THE_RANK] == hand[4][THE_RANK]:
		return ('five of a kind', hand[0][THE_RANK])

	# check if hand is a "straight flush"
	if isStraight(hand) and isFlush(hand):
		return ('straight flush', getHighCard(hand))

	# check if hand is a "four of a kind"
	for i in range(5):
		# check if the first four cards are a "four of a kind"
		if hand[0][THE_RANK] == hand[1][THE_RANK] == hand[2][THE_RANK] == hand[3][THE_RANK]:
			return ('four of a kind', hand[0][THE_RANK])

		# move the first card to the end of the hand
		card = hand[0]
		del hand[0]
		hand.append(card)

	# check if hand is a 'full house'
	threeCards = getThreeOfAKind(hand)
	if threeCards is not None:
		fullHouseHand = hand[:]
		for card in threeCards:
			fullHouseHand.remove(card)
		if fullHouseHand[0][THE_RANK] == fullHouseHand[1][THE_RANK]:
			#pdb.set_trace()
			return ('full house', getHighCard(threeCards))

	# check if hand is a 'flush'
	if isFlush(hand):
		return ('flush', getHighCard(hand))

	# check if hand is a 'straight'
	if isStraight(hand):
		return ('straight', getHighCard(hand))

	# chec kif hand is a 'three of a kind'
	threeCards = getThreeOfAKind(hand)
	if threeCards is not None:
		return ('three of a kind', threeCards[0][THE_RANK])

	# check if hand is a 'two pair' or 'one pair'
	twoCards = getTwoOfAKind(hand)
	if twoCards is not None:
		remainingThreeCards = hand[:]
		for card in twoCards:
			remainingThreeCards.remove(card)

		otherTwoCards = getTwoOfAKind(remainingThreeCards)
		if otherTwoCards is not None:
			if RANKS.index(twoCards[0][THE_RANK]) > RANKS.index(otherTwoCards[0][THE_RANK]):
				return ('two pair', twoCards[0][THE_RANK])
			else:
				return ('two pair', otherTwoCards[0][THE_RANK])
		else:
			return ('one pair', twoCards[0][THE_RANK])

	# get high card of hand
	return ('high card', getHighCard(hand))






def getHighCard(hand):
	ranks = [RANKS.index(card[THE_RANK]) for card in hand]
	ranks.sort()
	return RANKS[ranks[-1]]

	
def isStraight(hand):
	#logging.debug('hand = ' + str(hand))
	ranks = [RANKS.index(card[THE_RANK]) for card in hand]
	ranks.sort()
	return (ranks[1] == ranks[0]+1) and (ranks[2] == ranks[0]+2) and (ranks[3] == ranks[0]+3) and (ranks[4] == ranks[0]+4)

def isFlush(hand):
	return hand[0][THE_SUIT] == hand[1][THE_SUIT] == hand[2][THE_SUIT] == hand[3][THE_SUIT] == hand[4][THE_SUIT]

def getThreeOfAKind(hand):
	ranks = [card[THE_RANK] for card in hand]
	for threeCards in itertools.combinations(ranks, 3):
		if threeCards[0] == threeCards[1] == threeCards[2]:
			return [card for card in hand if card[THE_RANK] == threeCards[0][THE_RANK]][0:3]
	return None

def getTwoOfAKind(hand):
	ranks = [card[THE_RANK] for card in hand]
	for twoCards in itertools.combinations(ranks, 2):
		if twoCards[0] == twoCards[1]:
			return [card for card in hand if card[THE_RANK] == twoCards[0][THE_RANK]][0:2]
	return None	