'''

Advent of Code 2020

--- Day 10: Adapter Array --- see https://adventofcode.com/2020/day/10

--- Part II ---

Status: Solved
Agenda: ?

'''

###
### INPUT
###

input_string = open("input.txt", "r").read()
#input_string = open("example2.txt", "r").read()

input_list = sorted([int(l) for l in input_string.split()])
input_list.insert(0,0)
input_list.append(max(input_list)+3)
input_set = set(input_list)

#print(input_list)

step_ranges = {1, 2, 3} # adjustable if needed for other tasks

#recursive count function with memo
memo = dict()

def rec_count(num, step_ranges, available_steps):
    if num in memo: return memo[num]
    if num == 0: return 1

    count = 0

    for i in step_ranges:
        if num-i >= 0 and (num-i) in available_steps: count += rec_count(num - i, step_ranges, available_steps)
    #print(num,count)
    memo[num] = count
    return count

print("\nDAY 10 - PART II")
print(rec_count(input_list[-1], step_ranges, input_list))

