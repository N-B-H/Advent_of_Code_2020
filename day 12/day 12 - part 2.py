'''

Advent of Code 2020

--- Day 12: Rain Risk --- see https://adventofcode.com/2020/day/12

--- PART II ---

Status: Solved
Agenda: ?

'''

input_string = open("input.txt","r").read()
input_lines = [line for line in input_string.split()]

class instruction:
    def __init__(self,command,value):
        self.command = command
        self.value = value

    def print_instruction(self):
        print(self.command, self.value)

class vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class course:

    def __init__(self, position, direction):

        #self.x = position.x
        #self.y = position.y
        self.position = position

        self.vec_x = direction.x
        self.vec_y = direction.y
        #self.direction = direction

    def print_course(self):
        print("pos: ", self.position.x,self.position.y)
        print("vec: ", self.vec_x,self.vec_y)

    def move(self,iterations):

        for i in range(iterations):
            self.position.x += self.vec_x
            self.position.y += self.vec_y

        return self

    def update(self,instr):

        def rotate_waypoint(old_vector, turn_direction, degrees):
            new_vector = vec()

            if degrees == 180:
                new_vector.x = -old_vector.x
                new_vector.y = -old_vector.y

            elif turn_direction == "R" and degrees == 90 or turn_direction == "L" and degrees == 270:
                new_vector.x = old_vector.y
                new_vector.y = -old_vector.x

            elif turn_direction == "L" and degrees == 90 or turn_direction == "R" and degrees == 270:
                new_vector.x = -old_vector.y
                new_vector.y = old_vector.x

            return new_vector

        command_dict = {
            "N": lambda value: course(self.position, vec(self.vec_x, self.vec_y + value)),
            "S": lambda value: course(self.position, vec(self.vec_x, self.vec_y - value)),
            "E": lambda value: course(self.position, vec(self.vec_x + value, self.vec_y)),
            "W": lambda value: course(self.position, vec(self.vec_x - value, self.vec_y)),
            "L": lambda value: course(self.position, rotate_waypoint(vec(self.vec_x,self.vec_y), "L", value)),
            "R": lambda value: course(self.position, rotate_waypoint(vec(self.vec_x,self.vec_y), "R", value)),
            "F": lambda value: self.move(value)
        }

        new_course = command_dict[instr.command](instr.value)

        return new_course

def parse_line(line):
    command = line[0]
    value = int(line.strip("NSEWLRF"))

    return instruction(command,value)



instruction_list = [parse_line(line) for line in input_lines]

boat = course(vec(0,0),vec(10,1))

for instr in instruction_list:

    #instr.print_instruction()

    boat = boat.update(instr)

    #boat.print_course()

print()
print(f"|{boat.position.x}| + |{boat.position.y}| = {abs(boat.position.x)+abs(boat.position.y)}")