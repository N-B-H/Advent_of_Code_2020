###
### INPUT
###

#input_string = open("input.txt", "r").read()
input_string = open("example1.txt", "r").read()

input_list = sorted([int(l) for l in input_string.split()])
input_list.insert(0,0)
input_list.append(max(input_list)+3)

count = 1

### CLASSES
class TreeNode:
    def __init__(self,number):
        self.number = number
        self.children = []
        self.parent = None

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p=p.parent
            level += 1

        return level

    def get_prefix(self):
        ### unfinished!!

        level = self.get_level()

        split_points = [4,5,10]

        if self.parent and self.has_siblings():
            print(i.number for i in self.parent.children)
            #b = self.parent.children.sort(key = lambda x: x.number).index(self)
            b = len(self.parent.parent.children)-1
            print(b)
            a = level - b
            prefix = "   " * a + "|  " * b + "|-"
        else: prefix = level * "   " + "|-"

        return prefix

    def print_tree(self):
        level = self.get_level()
        spaces = level * "    "

        prefix = spaces + "|--"

        #prefix = self.get_prefix()
        #if self.parent and self.parent and self.parent.children and not self.parent.children == None and len(self.parent.children) > 1: prefix = "  " + prefix
        print(prefix, self.number)
        if self.children:

            for child in self.children:

                child.print_tree()

    def count_leaves(self):
        global count
        #print()
        #print(self.number,[self.children[i].number for i in range(len(self.children))])
        #print(count)

        if self.children:
            if len(self.children) > 1:
                count += len(self.children) - 1
            #print(count)

            for child in self.children:
                child.count_leaves()


        return count

    def has_siblings(self):
        if len(self.parent.children) > 1: return True
        else: return False

    def add_child(self,child):

        child.parent = self
        self.children.append(child)

    def add_children(self, *list_of_child_nodes):
        for child_node in list_of_child_nodes:
            self.add_child(child_node)

    def add_all_descendants(self,children_of):

        if children_of[self.number]:
            # add children...
            for child_num in children_of[self.number]:

                self.add_children(TreeNode(child_num))

            for i in range(len(self.children)):

                self.children[i].add_all_descendants(children_of)


def count_differences(list_of_adapters):
    diff_of_1 = diff_of_3 = 0

    for i in range(len(list_of_adapters))[1:]:
        if list_of_adapters[i]-list_of_adapters[i-1] == 1: diff_of_1 += 1
        if list_of_adapters[i] - list_of_adapters[i - 1] == 3: diff_of_3 += 1

    return diff_of_1,diff_of_3

def get_tree(list_of_numbers):

    children_of = {list_of_numbers[i]: set() for i in range(len(list_of_numbers))} #key = number, value = set_of_children

    #which number has which children?

    for num in list_of_numbers:
        for diff in (1,2,3):
            if num+diff in children_of:
                children_of[num].add(num+diff)

        if children_of[num] == set(): children_of[num] = None

    # generate tree of node objects
    root = TreeNode(list_of_numbers[0])
    root.add_all_descendants(children_of)

    return root


def count_possible_arrangements(tree):
    count = 0
    for cur_node in tree:
        if cur_node.children == None: count += 1

    return count

def count_possible_arrangements_b(list_of_numbers):
    tree = list() #of nodes. (index = id != line)

    for i in range(len(list_of_numbers)):
        cur_adapter = list_of_numbers[i]
        cur_children = set()
        for diff in (1,2,3):
            if cur_adapter+diff in list_of_numbers:
                cur_children.add(cur_adapter+diff)
        #new_node = (list_of_adapters[i], cur_children)
        tree[cur_adapter] = cur_children

    overall_arr_poss = 1
    overall_branch_count = 1
    for i in range(len(list_of_numbers))[1:-1]:
        cur_children = 0

        for diff in (1,2,3):
            if list_of_numbers[i]+diff in list_of_numbers: cur_children += 1

        overall_arr_poss += cur_children-1
        print("line, number and possibilities: ", i, list_of_numbers[i], cur_children)
        print(overall_arr_poss)
    return overall_arr_poss

### Part 1

print("PART 1")
diff_of_1, diff_of_3 = count_differences(input_list)
result = diff_of_1 * diff_of_3

print(input_list)
print(diff_of_1,diff_of_3)
print(result,"\n")


### Part 2
print("PART 2")

tree = get_tree(input_list)
tree.print_tree()
print(tree.count_leaves())
#print(get_tree(input_list).children[0].children[0].number)
#possible_arragengements = count_possible_arrangements(input_list)

#print(possible_arragengements, "possible arrangements")