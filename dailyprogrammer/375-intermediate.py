# https://www.reddit.com/r/dailyprogrammer/comments/aq6gfy/20190213_challenge_375_intermediate_a_card/

from copy import deepcopy

# Flips card at specified index of hand if there's a card present
def flip_card(hand, index):
	hand_copy = deepcopy(hand)

	if hand_copy[index] != 'x':
		hand_copy[index] = str(1 - int(hand_copy[index]))

	return hand_copy

# Remove card at specified index and returns new hand. Reverses move if replace == True
def remove_card(hand, index):
	if hand[index] != '1':
		print('Invalid operation, specified entry is {}'.format(hand[index]))
		return

	hand_copy = deepcopy(hand)
	hand_copy[index] = 'x'

	# Perform flips to the left and right if necessary
	if index-1 >= 0:
		hand_copy = flip_card(hand_copy, index-1)
	if index+1 <= len(hand_copy)-1: 
		hand_copy = flip_card(hand_copy, index+1)

	return hand_copy	

# Check if the hand is successfully completed, stuck, or still in progress
def check_hand(hand):
	# If all entries are 'x', hand is successfully completed
	if set(hand) == {'x'}:
		return 1

	# If there are no 1s to remove, hand is deemed stuck
	if '1' not in set(hand):
		return -1

	# Otherwise, hand is deemed to be still in progress
	return 0

# From left to right, perform flips until no more can be performed
def play(hand):
	# Check if hand is completed
	hand_status = check_hand(hand)
	if hand_status == 1:
		return []
	elif hand_status == -1:
		return -1

	# Otherwise, make a move and iterate. Get a list of the indexes of hand which have value 1
	valid_moves = [i for i in range(len(hand)) if hand[i] == '1']

	for move in valid_moves:
		move_result = play(remove_card(hand, move))

		if move_result == -1:
			continue
		else:
			return [move] + move_result

	# If none of the valid moves result in success, return -1 to indicate an insolvable hand
	return -1

print('\nBeginning game!')

while True:
	input_str = input('\nEnter a starting hand, or enter "F" to finish\n')

	if input_str.upper() == 'F':
		print('\nThanks for playing!\n')
		break

	input_list = list(input_str)
	game_result = play(input_list)

	if game_result == []:
		print('Boring! Game was trivial. Already solved ...')
	elif game_result == -1:
		print('No solutions!')
	else:
		print('Solution found! Consider the sequence: {}'.format(game_result))