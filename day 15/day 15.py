from copy import deepcopy
from collections import deque
#import queue
import time
input_list = [16,11,15,0,1,7]

example = [
    [0,3,6],
    [1,3,2],
    [2,1,3],
    [1,2,3],
    [2,3,1],
    [3,2,1],
    [3,1,2]
]
#starting_numbers = example[0] #input_list
#starting_numbers = input_list

n = 2020


start_time = time.time()
#print(start_time)

def nth_call(n,starting_numbers):
    if n < len(starting_numbers): return starting_numbers[n]

    #turns = starting_numbers

    previous_call = starting_numbers[-1]
    #last_spoken = {starting_numbers[i]: [i] for i in range(len(starting_numbers))}

    # AS QUEUES

    last_spoken_q = dict()
    for i in range(len(starting_numbers)):
        last_spoken_q[starting_numbers[i]] = deque()
        last_spoken_q[starting_numbers[i]].append(i)

    i = len(starting_numbers)

    while i < n:
        if len(last_spoken_q[previous_call]) >= 2:
            call = last_spoken_q[previous_call][1]-last_spoken_q[previous_call][0]
        else: call = 0

        if not call in last_spoken_q: last_spoken_q[call] = deque()
        last_spoken_q[call].append(i)

        if len(last_spoken_q[call]) > 2: last_spoken_q[call].popleft()
        #print(i, call, last_spoken_q)

        previous_call = call
        i += 1

    '''
    AS LISTS
    
    #print(turns)
    while i < n:
        if len(last_spoken[previous_call]) < 2:
            call = 0
            #last_spoken[previous_call].append()
        else:
            call = last_spoken[previous_call][1]-last_spoken[previous_call][0]

        if call in last_spoken:
            if len(last_spoken[call]) >= 2: last_spoken[call].pop(0)
            last_spoken[call].append(i)
        else: last_spoken[call] = [i]
        previous_call = call
        i += 1
        #print(call)
        #print(last_spoken)
    '''
    return call

def print_first_20_of_examples(example):
    last_spoken = dict()
    starting_numbers = []
    for i in range(len(example)):
        starting_numbers = deepcopy(example[i])
        last_spoken = dict()
        for k in range(len(starting_numbers)):
            last_spoken[starting_numbers[k]] = [k]

        print("Starting Numbers: ", starting_numbers)
        #print(f"The {n}th number is: ", nth_call(n))


starting_numbers = deepcopy(input_list)

n = 30000000
print("Starting Numbers: ", starting_numbers)
print(f"The {n}th number is: ", nth_call(n,starting_numbers))
end_time = time.time()-start_time
print("Duration: ", end_time, "Seconds")