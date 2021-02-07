from copy import deepcopy

#input_string= open("example.txt").read()
input_string= open("input.txt").read()

lines = input_string.split()
grid = [list(line) for line in lines]


def has_no_neighbours(row,column,grid):
    n_range = 1

    left_border = max(0,column-n_range)
    right_border = min(len(grid[0]),column+n_range+1)

    top_border = max(0,row-n_range)
    bottom_border = min(len(grid),row+n_range+1)


    for y in range(len(grid))[top_border:bottom_border]:
        for x in range(len(grid[y]))[left_border:right_border]:

            if (y, x) == (row, column): continue

            if grid[y][x] == "#":
                return False

    return True

def count_neighbours(row, column, grid):
    count = 0
    n_range = 1

    top_index = max(0,row-n_range)
    bottom_index = min(len(grid),row+n_range)

    left_index = max(0, column - n_range)
    right_index = min(len(grid[0]), column + n_range)

    for y in range(len(grid))[top_index:bottom_index+1]:
        for x in range(len(grid[y]))[left_index:right_index+1]:

            if (y, x) == (row, column): continue

            if grid[y][x] == "#": count += 1

    return count

def apply_rules(grid):
    new_grid = deepcopy(grid)

    for row in range(len(grid)):
        for column in range(len(grid[row])):

            if grid[row][column] == ".":
                new_grid[row][column] = "."
                continue

            if has_no_neighbours(row,column,grid): new_grid[row][column] = "#"
            if count_neighbours(row,column,grid) >= 4: new_grid[row][column] = "L"

            #else: new_grid[row][column] = grid[row][column]


    return new_grid

def count_visible_neighbours(row,column,grid):
    count = 0

    #vertical and horizontal:

    up = [grid[y][column] for y in range(row-1,-1,-1)]
    down = [grid[y][column] for y in range(row + 1, len(grid))]
    left = [grid[row][x] for x in range(column - 1, -1,-1)]
    rigth = [grid[row][x] for x in range(column + 1,len(grid[0]))]

    up_right = []
    up_left = []
    down_right =[]
    down_left = []

    for y,x in zip(range(row-1,-1,-1),range(column - 1, -1,-1)):
        up_left.append(grid[y][x])

    for y,x in zip(range(row-1,-1,-1),range(column+1,len(grid[0]))):
        up_right.append(grid[y][x])

    for y, x in zip(range(row + 1, len(grid)), range(column + 1, len(grid[0]))):
        down_right.append(grid[y][x])

    for y, x in zip(range(row + 1, len(grid)), range(column - 1, -1,-1)):
        down_left.append(grid[y][x])

    for direction in [up,up_right,up_left,rigth,down_right,down,down_left,left]:
        #if "#" in direction: count += 1
        for i in range(len(direction)):
            if direction[i] == "L": break
            if direction[i] == "#":
                count += 1
                break

    return count

def apply_part_two_rules(grid):
    new_grid = deepcopy(grid)

    for row in range(len(grid)):
        for column in range(len(grid[0])):

            if grid[row][column] == ".":
                new_grid[row][column] = "."
                continue

            #if has_no_visible_neighbours(row,column,grid): new_grid[row][column] = "#"
            neighbour_count = count_visible_neighbours(row,column,grid)
            if neighbour_count == 0: new_grid[row][column] = "#"
            if neighbour_count >= 5: new_grid[row][column] = "L"

            #else: new_grid[row][column] = grid[row][column]


    return new_grid

def count_occupied_seats(grid):
    count = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):

            if grid[row][column] == "#": count += 1

    return count

def print_grid(grid):
    for row in grid:
        print(''.join(row))

### MAIN ###
old_grid = apply_rules(grid)
#print_grid(old_grid)

while True:

    #new_grid = apply_rules(old_grid)
    new_grid = apply_part_two_rules(old_grid)
    print()
    print_grid(new_grid)
    if new_grid == old_grid: break

    old_grid = deepcopy(new_grid)
print()
occupied_seats = count_occupied_seats(new_grid)


#print_grid(grid)
#print()
#print_grid(new_grid)
#print()
print(occupied_seats)
