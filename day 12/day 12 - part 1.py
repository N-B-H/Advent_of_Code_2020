#input_string = open("input.txt","r").read()
input_string = open("example.txt","r").read()
input_lines = [line for line in input_string.split()]

class instruction:
    def __init__(self,command,value):
        self.command = command
        self.value = value

    def print_instruction(self):
        print(self.command, self.value)


class course:
    def __init__(self,x=0,y=0,direction=0):
        self.x = x
        self.y = y
        self.direction = direction % 360

    def print_course(self):
        print(self.x,self.y,self.direction)

    def update(self,instr):
        def forward(direction):
            direction_to_string = {
                0: "E",
                90: "S",
                180: "W",
                270: "N"
            }
            return direction_to_string[direction]

        command_dict = {
            "N": lambda value: course(self.x,self.y + value, self.direction),
            "S": lambda value: course(self.x,self.y - value, self.direction),
            "E": lambda value: course(self.x + value, self.y, self.direction),
            "W": lambda value: course(self.x - value, self.y, self.direction),
            "L": lambda value: course(self.x, self.y, self.direction - value),
            "R": lambda value: course(self.x, self.y, self.direction + value),
            "F": lambda value: self.update(instruction(forward(self.direction),value))

        }


        new_course = command_dict[instr.command](instr.value)

        return new_course

def parse_line(line):
    command = line[0]
    value = int(line.strip("NSEWLRF"))

    return instruction(command,value)


current_course = course()

instruction_list = [parse_line(line) for line in input_lines]

new_course = course()

for instr in instruction_list:
    new_course = new_course.update(instr)
    instr.print_instruction()
    new_course.print_course()

print()
print(f"|{new_course.x}| + |{new_course.y}| = {abs(new_course.x)+abs(new_course.y)}")