from copy import deepcopy

input_string = open("example.txt","r").read()


class tile_obj:
    def __init__(self, key, content,rotated = 0, flipped = None, position = None):
        self.key = key
        self.content=content
        self.rotated = rotated
        self.flipped = flipped
        self.position = position

class Vec:
    def __init__(self, y, x):
        self.x = x
        self.y = y

def parse_tiles(input_string):
    tiles = dict()

    raw_tiles = input_string.split("\n\n")
    for i in range(len(raw_tiles)):
        split_id_content = raw_tiles[i].split(":")
        tile_id = int(split_id_content[0].replace("Tile ",""))
        tile_content_str = split_id_content[1].strip("\n")

        tile_lines = tile_content_str.split()
        bit_lines = [None] * len(tile_lines)
        for k in range(len(tile_lines)):
            tile_lines[k] = tile_lines[k].replace("#","1").replace(".","0")
            bit_lines[k] =[bool(int(bit)) for bit in tile_lines[k]]
        tiles[tile_id] = tile_lines

    return tiles

def rotate_90_right(tile,*times):
    return list(zip(*reversed(tile)))

def flip_horizontal(tile):
    return reversed(tile)

def flip_vertical(tile):
    return [reversed(row) for row in tile]

def get_edges(tile):

    edges = []

    top = tile[0]
    top_reversed = top[0][::-1]

    right = [tile[i][-1] for i in range(len(tile))]
    right_reversed = right[::-1]

    bottom = tile[-1]
    bottom_reversed = bottom[::-1]

    left = [tile[i][0] for i in range(len(tile))]
    left_reversed = left[::-1]

    edges = [top, top_reversed, right, right_reversed, bottom, bottom_reversed, left, left_reversed]

    return edges

def get_neighbours(tiles):
    neighbours = {key: set() for key in tiles.keys()}

    for ID_1 in tiles.keys():
        ID_1_edges = get_edges(tiles[ID_1])

        for ID_2 in tiles.keys():
            if ID_1 == ID_2: continue
            if ID_2 in neighbours[ID_1]: continue

            ID_2_edges = get_edges(tiles[ID_2])

            for edge_1 in ID_1_edges:
                for edge_2 in ID_2_edges:
                    if edge_1 == edge_2 and not ID_2 in neighbours[ID_1]:

                        neighbours[ID_1].add(ID_2)

    return neighbours

def fewest_neighbours(neighbours):
    return sorted(neighbours.items(), key = lambda item: len(item[1]))


def is_valid_next_tile(cur_pos = Vec(0,0), next_pos = Vec(0,0), grid, neighbours):
    if not grid[cur_pos.y][cur_pos.x] in neighbours: return None
    if grid[next_pos.y][next_pos.x] in neighbours[grid[cur_pos.y][cur_pos.x]]: return True
    else: return False

    if len(neighbours) == 1: return neighbours.values()[0]

    new_neighbours = deepcopy(neighbours)

    x_max = 3
    y_max = 3
    #initial position:
    x, y = 0, 0
    next_x, next_y = 1, 0

    cur_key = None

    while grid[next_y][next_x] == None:
        #try if new tile
        for next_key in neighbours[cur_key]:
            pass
            is_valid_next_tile(grid)

    return True

def set_neighbour(neighbours, pos = Vec(0, 0), ID = 2971):

    if not (ID in neighbours): return False
    else:
        new_neighbours = deepcopy(neighbours)
        #reduce current ID from neighbours-keys, and -elements
        new_neighbours.pop(ID)
        for key in new_neighbours.keys():
            if ID in new_neighbours[key]: new_neighbours[key].remove(ID)



        #for next_ID in neighbours[ID]:
            #if set_neighbour(new_neighbours, pos=next_pos, ID=next_ID):

               # print(ID)

        return True

grid = [[None] * 3] * 3
pos = Vec(0, 0)
def purge_ID(ID,neighbours,neighbour_order):
    neighbours.pop(ID)
    for key in neighbours:
        neighbours[key].remove(ID)

    neighbour_order.remove(ID)

    return neighbours, neighbour_order

def arrange(neighbours,neighbour_order):

    #if not( x <= 3 and y <= 3): return grid

    #initial position
    x = y = 0
    try_grid = deepcopy(grid)
    #assume a tile to be the next:
    for ID in neighbour_order:
        try_grid[y][x] = ID
        neighbours, neighbour_order = purge_ID(ID, neighbours, neighbour_order)

        #assume a neighbour
        if neighbour_order[0] in neighbours[ID]:
            next_ID = neighbour_order[0]








    return grid


tile_dict = parse_tiles((input_string))

neighbours = get_neighbours(tile_dict)

for tile in neighbours:
    print(tile, neighbours[tile])
neighbour_order =[item[0] for item in fewest_neighbours(neighbours)]
print("Sorted Neighbours: ", neighbour_order)


#corner_tiles = get_corner_tiles(neighbours)
#print(corner_tiles)

tile_objects = dict()
for key in tile_dict.keys():
    tile_objects[key] = tile_obj(key, tile_dict[key])


grid = [[None] * 3] * 3
arrange(neighbours, neighbour_order)
