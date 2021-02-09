'''

Advent of Code 2020

--- Day 9: Encoding Error --- see https://adventofcode.com/2020/day/9

Status: Solved
Agenda: More elegant/efficient Solution?

'''

###
### INPUT
###

input_string = open("input.txt", "r").read()
#input_string = open("example2.txt", "r").read()

input_list = [int(l) for l in input_string.split()]
#print("INPUT:\n", input_list)
preamble_length = 25

###
### Functions
###

def is_valid(num, set_of_previous):
    for summand_a in set_of_previous:

        if num - summand_a in set_of_previous:
            #summand_b = num-summand_a
            return True
    return False

def get_first_wrong_number(list_of_numbers,preamble_length):
    previous_numbers = [num for num in list_of_numbers[:preamble_length]]
    #print(previous_numbers)
    #print(list_of_numbers[preamble_length:])

    for line in range(len(list_of_numbers))[preamble_length:]:
        num = list_of_numbers[line]
        #print(is_sum_of_two_in_preamble(num,previous_numbers))

        if not is_valid(num, set(previous_numbers)): return line, num
        else:
            #update previous_numbers
            previous_numbers.pop(0)
            previous_numbers.append(num)
    return None, None

def find_list_of_summands(num,possible_summands):
    #first_summand_index = 0
    #last_summand_index = 1

    for first_summand_index in range(len(possible_summands)):
        for last_summand_index in range(len(possible_summands))[first_summand_index+1:]:

            potential_list_of_summands = possible_summands[first_summand_index:last_summand_index+1]

            if sum(potential_list_of_summands) == num: return potential_list_of_summands
    return None


### PART 1

first_wrong_line, first_wrong_number = get_first_wrong_number(input_list,preamble_length)

print("\nPART 1:")
print("First wrong line: ", first_wrong_line)
print("Number: ", first_wrong_number)

### Part 2

list_of_summands = find_list_of_summands(first_wrong_number, input_list[:first_wrong_line])
smallest_summand, largest_summand = min(list_of_summands), max(list_of_summands)
result = smallest_summand + largest_summand

print("\nPART 2:")
print("The summands for the above number are: ", list_of_summands)
print(f"The smallest and largest of these summands are: {smallest_summand} and {largest_summand}")
print("They add up to: ", result)
