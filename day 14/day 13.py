### Bitwise Fun

input_string = open("example.txt","r").read()

string_lines = [line for line in input_string.split()]

mem = dict()
mask = str()

def make_bit_list(len,int_or_str):

    bit = bool()
    BitArray = [bit]*len

    if isinstance(int_or_str, int):
        pass

    return BitArray



for line in string_lines:
    if line[0:3]== "mask": mask = line.split("=")[1].strip()
    else:
        # split at "=", remove all non-digits for address, read address and value
        mem_command = line.split("=")
        address = int(mem_command[0].strip("mem[]"))
        int_value = int(mem_command[1].strip())
        bit_value = bin(int_value)
        bit_string = str(bit_value)[2:]
        new_value = mask
        for i in range(len(mask)):
            if mask[i] == "X":
                pass




