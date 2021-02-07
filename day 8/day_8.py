from copy import deepcopy
###
### INPUT
###


input_string = open("input.txt", "r").read()
#input_string = open("example2.txt", "r").read()

def find_loop(command_lines):
    executed_lines = set()
    acc = 0
    i = 0

    while not i in executed_lines:

        executed_lines.add(i)
        command, argument = command_lines[i].split()

        #print(i,acc)
        #print(command,argument)

        if command == "acc":
            acc += int(argument)
            i += 1

        elif command == "jmp":
            i += int(argument)

        else: i += 1

        if i >= len(command_lines): return False, acc

    return True, acc

def find_wrong_line(command_lines):

    altered_lines = deepcopy(command_lines)

    for i in range(len(command_lines)):
        command = command_lines[i].split()[0]

        if command == "nop": new_line = command_lines[i].replace("nop","jmp")
        elif command == "jmp": new_line = command_lines[i].replace("jmp","nop")
        else: continue

        altered_lines[i] = new_line

        #has_loop, acc = find_loop(command_lines)
        #print((command_lines[i]), has_loop, acc)

        #rerun with altered line
        has_loop, acc = find_loop(altered_lines)
        #print((altered_lines[i]), has_loop,acc)
        #print(command_lines)
        #print(altered_lines)
        altered_lines = deepcopy(command_lines)
        if not has_loop:
            return i, acc

    return 0,0

lines = input_string.split('\n')

has_loop, acc = find_loop(lines)

print("Has Loop =", has_loop)
print("acc=",acc)

wrong_line, acc = find_wrong_line(lines)

print(f"Line {wrong_line} has to be altered. Acc at the end is then: {acc}")
