import string
from copy import deepcopy

###
### INPUT
###

input_string = open("input.txt", "r").read()
#input_string = open("example2.txt", "r").read()

###
### FUNCTIONS
###

# Parse input to dictionary
# takes a string with all rules as input
# returns a dictionary with colors as keys and lists with all valid content-colors(str) as values

def input_to_rules(input_string):
    rules = dict()

    #separate lines
    lines = input_string.split('\n')

    #clear data from unnecessary words etc.
    for i in range(len(lines)):
        lines[i] = lines[i].replace("bags",'').replace("no other",'').replace("bag",'').strip(' .')

    #separate keys and values
    for i in range(len(lines)):
        split_line = lines[i].split('contain')
        key = split_line[0].strip()
        values = [value.strip(' ' + string.digits) for value in split_line[1].split(',')]
        rules[key] = values

    return rules

# get master dictionary
# colors as key, ALL Children, Grandchildren etc. joined in ONE List as value

def get_master_dict(rules):
    all_descendants_of = deepcopy(rules) # To be extended

    for outer_color in rules.keys(): # go through all colors

        if all_descendants_of[outer_color] == ['']: continue # this outer color doesn't contain anything

        cdi = 0  # current descendant index
        cur_descendants = all_descendants_of[outer_color] # list of  colors, contained in outer_color
        next_descendants = all_descendants_of[cur_descendants[cdi]]

        while True:

            # first generation children of outer_color are already in the list
            # merge current grandchildren into that list of children
            # eliminate duplicats

            descendants_to_add = [next_descendants[i] for i in range(len(next_descendants)) if next_descendants[i] not in all_descendants_of[outer_color] and not next_descendants[i]=='']
            all_descendants_of[outer_color].extend(descendants_to_add)

            #go to next descendant and break if it doesn't exist
            cdi += 1
            try: next_descendants = all_descendants_of[cur_descendants[cdi]]
            except: break

    return all_descendants_of

def get_outer_colors(my_color, master_dict): #(my_color, rules)

    possible_colors = []
    for color in master_dict.keys():
        if my_color in master_dict[color]: possible_colors.append(color)
    return possible_colors

###
### MAIN PROGRAMME
###

# parse rules to a dictionary
rules = input_to_rules(input_string)

# print rules
print("\nRULES:\n")
for key in rules.keys():
    print(key, "contains", rules[key])

# convert that dictionary of rules to a simplified master dictionary
# with colors as keys and ALL descendants in a list as value

master_dict = get_master_dict(rules)

# print master dictionary
print("\nMASTER DICTIONARY:\n")
for outer_color in master_dict.keys():
    print(outer_color, "ultimately contains:", master_dict[outer_color])

# extract all colors that eventually contain my color
my_color = "shiny gold"
possible_outer_colors = get_outer_colors(my_color, master_dict)

print(f"\nThese {len(possible_outer_colors)} colors can contain \"{my_color}\" eventually: \n", possible_outer_colors)
