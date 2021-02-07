input_file = open("day_5_input.txt", "r").read()

input_list = input_file.split()

print(input_list)

example = "BBFFBBFRLL"

print(example)

def decrypt_code(code):

    def find_row(code):
        row_max = 127
        row_min = 0
        for i in range(len(code)-3):
            if code[i] == "F": row_max = (row_max+row_min)//2
            elif code[i] == "B": row_min = (row_max+row_min)//2 + 1
            #print(i,code[i],row_min, row_max)
        return row_min

    def find_column(code):
        column_max = 7
        column_min = 0
        for i in range(len(code))[-3:]:
            if code[i] == "L": column_max = (column_max+column_min)//2
            elif code[i] == "R": column_min = (column_max+column_min)//2 + 1
            #print(i,code[i],column_min, column_max)
        return column_min

    row = find_row(code)
    column = find_column(code)
    seat_ID = row * 8 + column

    return (row,column,seat_ID)

def find_highest_Seat_ID(decrypted_list):
    return max([decrypted_list[i][2]] for i in range(len(decrypted_list)))

def find_missing_seats(seat_list):

    missing_seats = []

    for row in range(128):
        for column in range(8):
            if not (row,column,row*8+column) in seat_list:
                missing_seats.append((row,column,row*8+column))
    return missing_seats

def find_gap_in_IDs(seat_list):

    for i in range(len(seat_list)): #list_by_ID = sorted(seat_list, key=lambda x: x[2])
        if seat_list[i][2] == i: continue
        else:
            print("BINGO! It\'s", seat_list[i])
            return seat_list[i]

 #   for i in range(len(list_by_ID)):
   #     if not list_by_ID[3][i] == None

#decrypt example
print(f"example \"{example}\":\n",decrypt_code(example))

#decrypt all data
decrypted_list = [decrypt_code(input_list[i]) for i in range(len(input_list))]
print("whole data:\n", decrypted_list)

highest_ID = find_highest_Seat_ID(decrypted_list)
print("highest ID: \n", highest_ID)

missing_seats = find_missing_seats(decrypted_list)
print("missing seats: \n",missing_seats)

my_seat = find_gap_in_IDs(missing_seats)
print("my seat is: \n", my_seat)