'''

Advent of Code 2020

--- Day 10: Adapter Array --- see https://adventofcode.com/2020/day/10

--- Part I ---

Status: Solved
Agenda: ?

'''


### INPUT


input_string = open("input.txt", "r").read()
#input_string = open("example1.txt", "r").read()

input_list = sorted([int(l) for l in input_string.split()])

#Add first and last values according to the task
input_list.insert(0,0)
input_list.append(max(input_list)+3)


def count_differences(list_of_adapters):
    diff_of_1 = diff_of_3 = 0

    for i in range(len(list_of_adapters))[1:]:
        if list_of_adapters[i]-list_of_adapters[i-1] == 1: diff_of_1 += 1
        if list_of_adapters[i] - list_of_adapters[i - 1] == 3: diff_of_3 += 1

    return diff_of_1,diff_of_3


diff_of_1, diff_of_3 = count_differences(input_list)
result = diff_of_1 * diff_of_3

print("\nDAY 10 - PART 1")

#print(input_list)
#print(diff_of_1,diff_of_3)
print(result)

