import string
from copy import deepcopy

###
### INPUT
###

#input_string = open("input.txt", "r").read()
input_string = open("example.txt", "r").read()

###
### OBJECTS
###

### Bag Object
class bag():
    def __init__(self,color,content_dict):
        self.color = color          # string
        self.content = content_dict # i.e. {"green":6,"yellow":3} // OR: set of bags??


###
### FUNCTIONS
###

# Parse input to a set of bag-objects, representing the rules

def input_to_set_of_bags(input_string):
    set_of_bags = set()

    #separate lines from input
    lines = input_string.split('\n')

    for i in range(len(lines)):
        if "no other" in lines[i]: # no other bags inside, nothing to parse, go to next bag
            first_two_words = lines[i].split(lines[i],2)[:1]
            outer_color = first_two_words[0]+first_two_words[1]
            content_dict = None
            set_of_bags.add(bag(outer_color,content_dict))
            continue

        # clear data from unnecessary words, dots, whitespace etc.
        lines[i] = lines[i].replace("bags",'').replace("no other",'').replace("bag",'').strip(' .')

        # split into outer color and its content (left & right from "contain")
            # "vibrant plum contain 5 faded blue, 6 dotted black"
            # ---> "vibrant plum", "5 faded blue, 6 dotted black"

        split_line = lines[i].split('contain')
        outer_color = split_line[0].strip()  # left from "contain"
        all_content_str = split_line[1].strip()  # right from "contain"

        # split into list of strings of contained colors
            # "5 faded blue, 6 dotted black"
            # ---> "5 faded blue", "6 dotted black"
        content_list_of_str = [entry.strip for entry in all_content_str.split(',')]

        # split those entry-strings in colors and their associated numbers into a dictionary
            # "5 faded blue", "6 dotted black" and the above extracted "vibrant plum"
            # --->"vibrant plum", {"faded blue": 5, "dotted black": 6}
        content_dict = {}
        for entry_str in content_list_of_str:
            entry_number = entry_str[0] # number is just the first charachter
            entry_color = entry_str.replace(string.digits,'').strip() # remove number and whitespace. only color left
            content_dict[entry_color] = entry_number #add to dictionary

        # add content dictionary of current outer_color to the set of bags
        set_of_bags.add(bag(outer_color,content_dict)

    return set_of_bags

# get master set of bags, with all descendants in bag.content dictionary

def get_master_set(set_of_bags):
    master_set = deepcopy(set_of_bags) # Its content to be extended to make all subsequent descendants visible

    #all_colors = {each_bag.color for each_bag in set_of_bags}

    for outer_bag in set_of_bags(): # go through all bags

        if outer_bag.content == None: continue # this outer color doesn't contain anything

        cdi = 0  # current descendant index
        cur_descendants = master_set[outer_bag] # list of  colors, contained in outer_bag
        next_descendants = master_set[cur_descendants[cdi]]

        while True:

            # first generation children of outer_bag are already in the list
            # merge current grandchildren into that list of children
            # eliminate duplicats

            descendants_to_add = [next_descendants[i] for i in range(len(next_descendants)) if next_descendants[i] not in master_set[outer_bag] and not next_descendants[i]=='']
            master_set[outer_bag].extend(descendants_to_add)

            #go to next descendant and break if it doesn't exist
            cdi += 1
            try: next_descendants = master_set[cur_descendants[cdi]]
            except: break

    return master_set

def get_outer_colors(my_color, master_dict): #(my_color, rules)

    possible_colors = []
    for color in master_dict.keys():
        if my_color in master_dict[color]: possible_colors.append(color)
    return possible_colors

###
### MAIN PROGRAMME
###

# parse rules to a dictionary
rules = input_to_set_of_bags(input_string)

# print rules
print("\nRULES:\n")
for key in rules.keys():
    print(key, "contains", rules[key])

# convert that dictionary of rules to a simplified master dictionary
# with colors as keys and ALL descendants in a list as value

master_dict = get_master_set(rules)

# print master dictionary
print("\nMASTER DICTIONARY:\n")
for outer_color in master_dict.keys():
    print(outer_color, "ultimately contains:", master_dict[outer_color])

# extract all colors that eventually contain my color
my_color = "shiny gold"
possible_outer_colors = get_outer_colors(my_color, master_dict)

print(f"\nThese {len(possible_outer_colors)} colors can contain \"{my_color}\" eventually: \n", possible_outer_colors)
