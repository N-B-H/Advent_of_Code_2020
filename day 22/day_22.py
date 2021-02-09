'''

Advent of Code 2020

--- Day 22: Crab Combat --- see https://adventofcode.com/2020/day/22

Status: PART I solved, PART II work in progress
Agenda: debug recursive_combat function

'''

input_string = open("example.txt", "r").read()
#input_string = open("input.txt", "r").read()

from collections import deque
from copy import deepcopy

raw_players = input_string.split("\n\n")
player = [None] * 2
for i in 0, 1:
    player[i] = deque([int(i) for i in raw_players[i].split(":\n")[1].split()])

#player_2 = deque([int(i) for i in raw_players[1].split(":\n")[1].split()])

deck = deepcopy(player)
print("Part I ", "Starting with the following decks:", sep="\n")
print("Player 1", list(player[0]))
print("Player 2", list(player[1]))

def combat(deck):

    while not min(len(deck[0]), len(deck[1])) == 0:

        #num_winner = max(player[1][0],player[0][0])
        if deck[0][0] > deck[1][0]: i_winner = 0
        else: i_winner = 1

        deck[i_winner].extend((deck[i_winner].popleft(), deck[not i_winner].popleft()))

        '''
        if player[0][0] < player[1][0]:
            winner_gets = [player[1].popleft(),player[0].popleft()]
            player[1].extend(winner_gets)
        else:
            winner_gets = [player[0].popleft(), player[1].popleft()]
            player[0].extend(winner_gets)
        '''

    return deck[i_winner], i_winner

winner, i_winner = combat(player)

print("\nResulting in:")
print("Player 1", list(player[0]))
print("Player 2", list(player[1]))


def get_score(winner):
    score = 0
    i = 1
    for num in list(winner)[-1::-1]:
        score += num * i
        i += 1

    return score

print("\nScore: ", get_score(winner))

### PART TWO ###

memo = set()

def recursive_combat(deck):
    global round
    round += 1
    #if deck in memo: return 0
    #else: memo.add(deck)

    #base case
    if min(len(deck[0]), len(deck[1])) == 0:
        if len(deck[0]) > len(deck[1]): return 0, deck[0]
        else: return 1, deck[1]

    if len(deck[0]) >= deck[0][0] and len(deck[1]) >= deck[1][0]:
        for i in (0,1):
            deck[i].popleft()

    else:
        if deck[0][0] > deck[1][0]: winner = 0
        else: winner = 1

        deck[winner].extend((deck[winner].popleft(), deck[not winner].popleft()))

    return recursive_combat(deck)

round = 0
print("\nPART II")
print(deck)
winner, deck = recursive_combat(deck)
print(winner)
print(deck)