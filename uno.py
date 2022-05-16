#!/usr/bin/python3

import random

# Making a card game I guess lmao
# Make it like Uno I guess, so have one card left out and then you have to match the suit or number

# Why not do this in JS?
# Because this is meant to be a terminal game; Macs come with python installed so they can run this
# But Macs don't have Node installed by default
# So if I send this package to Sean for instance, he can play the game without having to download node

# I could make it a web game, but I couldn't figure out how to do the mutations with vanilla JS while on this flight, so I thought a terminal game would be better


# handle draw on empty deck

# Print the rules at the top
print("Type 'd' to draw a card.")

# Modifications to cards:
# Values = 0 -> 9
# Suits = C, D, H, S

# Todo, make this smarter
# Going for string instead of tuples so its easier to display and easier to check ownership,
# just know that the first character is the value, and the second is the suit
deck = ["0c", "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c",
				"0d", "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d",
				"0h", "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h",
				"0s", "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s"]

random.shuffle(deck)

# Now we give cards to each player
# You are Player A, with the first hand
players = ["You", "Tomoki", "Jeannie", "Sean"]

hands = [[], [], [], []]

discardPile = []

# form the top of the discard pile
discardPile.append(deck.pop())

numCardsInHand = 7

# 7 cards for 4 people
for i in range(numCardsInHand * len(hands)):
	hands[i % len(hands)].append(deck.pop())



winner = ""

discardPileTop = discardPile[len(discardPile) - 1]

# Display the discard pile:
print(f'\n{discardPileTop}')

# draw a card
#   playerID = id number of the player drawing
def draw(playerID, deck, discardPile):

	if (len(deck)):
		cardDrawn = deck.pop()
		hands[playerID].append(cardDrawn)
	else:
		print("      Shuffling discard pile into deck")
		discardPileNew = discardPile.pop()

		# TODO: pass deck by reference or figure out how to mutate top level deck
		# Probably something like draw(self, etc), but I reckon the whole thing including draw has to be in a class
		deck = random.shuffle(discardPile)

		discardPile = discardPileNew

	if(playerID == 0):
		print(f"    Drew a {cardDrawn}\t({len(hands[playerID])})\n")
	else:
		print(f"    {players[playerID]} drew a card\t({len(hands[playerID])})")

def round():
	winner = ""

	discardPileTop = discardPile[len(discardPile) - 1]

	# Display your hand:
	handString = ""
	for card in sorted(hands[0], key=lambda x : x[1]):
		handString = handString + f'{card} '

	possibleCards = list(filter(lambda x : (x[0] == discardPileTop[0] or x[1] == discardPileTop[1]), hands[0]))

	# refactor into inline if soon
	if len(possibleCards):
		print(f'    Hand: {handString}\t\tDeck: {len(deck)} cards')
	else:
		print(f'    Hand: {handString} (must draw)\t\tDeck: {len(deck)} cards')

	# Now the cards have been distributed, go ahead and start playing the game by placing cards down in the center
	# You go first
	cardToPlay = "XX"
	drewCard = False
	while (not drewCard and cardToPlay[0] != discardPileTop[0] and cardToPlay[1] != discardPileTop[1]):
		cardToPlayTemp = input("      Play: ")

		if (cardToPlayTemp == "d"):
			# Player wants to draw
			draw(0, deck, discardPile)
			drewCard = True
			continue

		if (len(cardToPlayTemp) != 2):
			print("    That is not a card!")
			continue

		if (cardToPlayTemp not in hands[0]):
			print("    That card is not in your hand!")
			continue

		if (cardToPlayTemp[0] != discardPileTop[0] and cardToPlayTemp[1] != discardPileTop[1]):
			print("    That card has the wrong value/suit!")
			continue

		cardToPlay = cardToPlayTemp

	if (not drewCard):
		# add and remove from array
		hands[0].remove(cardToPlay)
		discardPile.append(cardToPlay)

		print(f'\n{cardToPlay}: You\t\t({len(hands[0])})')

		discardPileTop = discardPile[len(discardPile) - 1]

	# If after playing you have no cards left, you win!
	if (len(hands[0]) == 0):
		return players[0]


	# Now all of the AI's have to play!
	# Skip the first hand since that's you
	for handIdx, hand in enumerate(hands[1:]):
		# So it lines up with the array
		handIdx = handIdx + 1

		possibleCards = list(filter(lambda x : (x[0] == discardPileTop[0] or x[1] == discardPileTop[1]), hand))

		if (len(possibleCards)):
			# if there are possible cards, play one of them

			# Out of the cards that work, just choose a random one
			cardToPlay = random.choice(possibleCards)

			hands[handIdx].remove(cardToPlay)
			discardPile.append(cardToPlay)

			print(f'{cardToPlay}: {players[handIdx]}\t({len(hands[handIdx])})')
		else:
			# otherwise, just draw
			draw(handIdx, deck, discardPile)

		# If after playing the AI has no cards left, they win!
		if (len(hands[handIdx]) == 0):
			return players[handIdx]

	print("")


winner = ""

while(not winner):
	winner = round()

print(f"{winner} wins!")


# Fix TODO pls
# Add mechanics of Uno in
# Add your own wacky mechanics
