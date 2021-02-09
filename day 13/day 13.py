'''

Advent of Code 2020

--- Day 13: Shuttle Search --- see https://adventofcode.com/2020/day/13

Status: PART I Solved, PART II far too slow. Only works in theory or on a faster computer
Agenda: Efficiency for PART II, any neat mathematical solution???

'''

input_string = open("input.txt","r").read()

lines = [line for line in input_string.split()]

timestamp = int(lines[0])

busses = lines[1].split(",")

#PART ONE

available_busses = [int(bus) for bus in busses if not bus == "x"]


def is_multiple(multiple,of):
    if multiple % of == 0: return True
    else: return False

next_multiples = []

for bus in available_busses:
    time = timestamp
    while True:
        if time % bus == 0:
            next_multiples.append(time)
            break
        time += 1

wait = min(next_multiples)-timestamp
ID = available_busses[next_multiples.index(min(next_multiples))]

print("PART ONE\n")
print("Timestamp: ", timestamp)
print("All Busses: ", busses)
print("Available Busses: ", available_busses)
print("Next Multiples after timestamp:", next_multiples)

print()
print(f"Line {ID} is the closest. The waiting time is {wait} minutes")

print("ID x Waiting Time: ", ID*wait)

# PART TWO

def valid_offset(timestamp, multiples):

    for i in range(len(multiples)):
        if multiples[i] == "x": continue
        if not multiples[i] == timestamp + i: return False

    return True

first_bus = int(busses[0])

first_time_stamp = first_bus*int(busses[first_bus]) - first_bus
timestamp = first_time_stamp

print(first_bus)
print(first_time_stamp)

while True:

    all_multiples = []

    for bus in busses:
        time = timestamp
        if bus == "x":
            all_multiples.append("x")
            continue

        while True:

            if time % int(bus) == 0:
                all_multiples.append(time)
                break
            time += 1
    if valid_offset(timestamp, all_multiples): break

    timestamp += first_time_stamp #(timestamp+first_bus) * int(busses[first_bus]) - first_bus

    # display progress
    if timestamp % (int(busses[0])*50000) == 0: print(timestamp)

print("\nPART TWO\n")

print(timestamp)
print(all_multiples)