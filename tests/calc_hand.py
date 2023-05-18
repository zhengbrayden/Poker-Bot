import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from commands.header import *
#want to test player.calc_hand() function
channel = Channel(0)
channel.create_lobby('l', 0)
player = channel.get_player(0)
deck = Deck()

# Test straight flush
player.hand = [Card('H', 5), Card('H', 6), Card('H', 7), Card('H', 8), Card('H', 9)]
player.calc_hand()
assert player.handscore == 9 * 10 ** 10 + 9, f"straight flush failed, got value {player.handscore}"

# Test four of a kind
player.hand = [Card('H', 5), Card('D', 5), Card('C', 5), Card('S', 5), Card('H', 9)]
player.calc_hand()
assert player.handscore == 8 * 10 ** 10 + 5 * 10 ** 8 + 9, f"four of a kind failed, got value {player.handscore}"

# Test full house
player.hand = [Card('H', 5), Card('D', 5), Card('C', 5), Card('H', 9), Card('D', 9)]
player.calc_hand()
assert player.handscore == 7 * 10 ** 10 + 5 * 10 ** 8 + 9 * 10 ** 6, f"full house failed, got value {player.handscore}"

# Test flush
player.hand = [Card('H', 5), Card('H', 6), Card('H', 9), Card('H', 10), Card('H', 14)]
player.calc_hand()
assert player.handscore == 6 * 10 ** 10 + 14 * 10 ** 8 + 10 * 10 ** 6 + 9 * 10 ** 4 + 6 * 10 ** 2 + 5 * 10 ** 0, f"flush failed, got value {player.handscore}"

# Test straight
player.hand = [Card('H', 5), Card('D', 6), Card('C', 7), Card('S', 8), Card('H', 9)]
player.calc_hand()
assert player.handscore == 5 * 10 ** 10 + 9 * 10 ** 8, f"straight failed, got value {player.handscore}"

# Test three of a kind
player.hand = [Card('H', 5), Card('D', 5), Card('C', 5), Card('S', 8), Card('H', 9)]
player.calc_hand()
assert player.handscore == 4 * 10 ** 10 + 5 * 10 ** 8 + 9 * 10 ** 2 + 8 * 10 ** 0, f"three of a kind failed, got value {player.handscore}"

# Test two pair
player.hand = [Card('H', 5), Card('D', 5), Card('C', 8), Card('S', 8), Card('H', 9)]
player.calc_hand()
assert player.handscore == 3 * 10 ** 10 + 8 * 10 ** 8 + 5 * 10 ** 6 + 9, f"two pair failed, got value {player.handscore}"

# Test one pair
player.hand = [Card('H', 5), Card('D', 5), Card('C', 8), Card('S', 9), Card('H', 10)]
player.calc_hand()
assert player.handscore == 2 * 10 ** 10 + 5 * 10 ** 8 + 10 * 10 ** 4 + 9 * 10 ** 2 + 8 * 10 ** 0, f"one pair failed, got value {player.handscore}"

# Test high card
player.hand = [Card('H', 2), Card('D', 5), Card('C', 8), Card('S', 9), Card('H', 14)]
player.calc_hand()
assert player.handscore == 1 * 10 ** 10 + 14 * 10 ** 8 + 9 * 10 ** 6 + 8 * 10 ** 4 + 5 * 10 ** 2 + 2 * 10 ** 0, f"high card failed, got value {player.handscore}"

print("All tests passed!")







