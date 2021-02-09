'''

Advent of Code 2020

--- Day 6: Custom Customs --- see https://adventofcode.com/2020/day/6

Status: Solved
Agenda: Regular Expressions?

'''


import string

###
### INPUT
###
input_string = open("day_6_input.txt","r").read()
#example = open("example.txt", "r").read()


###
### FUNCTIONS
###

#   count number of different characters that appear in one group
def count_number_of_different_characters(group_string):
    occurred_chars = set()
    for i in group_string:
        if i in string.ascii_letters and i not in occurred_chars: occurred_chars.add(i)

    #print(occurred_chars)
    return len(occurred_chars)


#   count number of different characters that appear in EVERY line of one group
#   (=all persons of that group crossed this letter with "yes")
def count_number_of_all_yes_characters(group_string):

    lines = group_string.split()
    occurred_chars = {}
    all_yes_chars = 0

    for l in lines:             #browse lines
        for char in l:          #browse single letters in line
            if char in string.ascii_letters:
                if not char in occurred_chars: occurred_chars[char] = 1
                else: occurred_chars[char] += 1

    for char in occurred_chars.keys():
        if occurred_chars[char] == len(lines):
            all_yes_chars += 1

    return all_yes_chars

# COUNT-FUNCTION
# PART I: sum up counts of different character appearances per group
# PART II: sum up counts of characters that appear in every line per group
def count_character_appearances(groups):

    total_count_part_1 = 0
    total_count_part_2 = 0

    for each_group in groups:
        total_count_part_1 += count_number_of_different_characters(each_group)
        total_count_part_2 += count_number_of_all_yes_characters(each_group)

    return total_count_part_1,total_count_part_2

###
### MAIN PROGRAMM
###

# split input_string into list of groups
groups = input_string.split('\n\n')


# PRINT RESULTS
print("Part One:", count_character_appearances(groups)[0])
print("Part Two:", count_character_appearances(groups)[1])

