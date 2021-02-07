from merge_ranges import merge_ranges
from copy import deepcopy

input_string = open("input.txt","r").read()
#input_string = open("example2.txt","r").read()

#Part 1
def parse_all_ranges(input_string):
    text_blocks = [line for line in input_string.split("\n\n")[0].split()]
    parsed_ranges = []
    for i in range(len(text_blocks)):
        if "-" in text_blocks[i]:
            parsed_ranges.append(tuple([int(str_num) for str_num in text_blocks[i].split("-")]))

    return parsed_ranges, merge_ranges(parsed_ranges)

def parse_all_values(input_string):
    value_lines = [line for line in input_string.split("\n\n")[2].split("\n")[1:]]
    all_values = []
    for line in value_lines:
        for num in line.split(","):
            all_values.append(int(num))

    return all_values

def parse_tickets(input_string):
    ticket_strings = [line for line in input_string.split("\n\n")[2].split("\n")[1:]]

    parsed_tickets = []
    for line in ticket_strings:
        parsed_tickets.append([int(value) for value in line.split(',')])

    return parsed_tickets

def is_invalid(value_or_ticket, rules):
    if isinstance(value_or_ticket, int):
        value = value_or_ticket
        for rule in rules:
            if rule[0] <= value <= rule[1]: return False
        return True
    elif isinstance(value_or_ticket, list):
        ticket = value_or_ticket
        for value in ticket:
            if is_invalid(value,rules): return True
        return False

#Part 2

def get_valid_tickets(parsed_tickets, rules):
    valid_tickets = []
    for ticket in parsed_tickets:
        if not is_invalid(ticket, rules): valid_tickets.append(ticket)

    return valid_tickets

def get_invalids(all_values, rules):
    invalids = []
    for value in all_values:
        if is_invalid(value, rules): invalids.append(value)
    return invalids

def parse_rules(input_string):
    rule_strings = [line for line in input_string.split("\n\n")[0].split("\n")]

    parsed_rules = dict()

    for line in rule_strings:
        split_line = line.split(':')
        rule = split_line[0] #rule-name: str
        both_ranges_str = split_line[1]

        both_parsed_ranges = []
        for single_range_str in both_ranges_str.split(' or '):
            parsed_range_tuple = tuple([int(num_str) for num_str in single_range_str.split('-')])
            both_parsed_ranges.append(parsed_range_tuple)
        parsed_rules[rule] = both_parsed_ranges

    return parsed_rules

def get_column(n, tickets):
    column = []
    for i in range(len(tickets)):
        column.append(tickets[i][n])

    return column

def is_valid(num,rule):
    for r in rule:
        if r[0] <= num <= r[1]: return True
    return False


def column_can_be_field(column, rules, rule_key):

    rule = rules[rule_key]

    for n in column:
        if not is_valid(n,rule): return False

    return True

def allocate_fields(tickets, rules):
    fields = [None] * len(rules)

    column_can_be = []
    for i in rules:
        column_can_be.append(set())
        for key in rules.keys():
            column_can_be[-1].add(key)

    while None in fields:
        for n in range(len(tickets[0])):
            column = get_column(n,tickets)
            for key in rules.keys():
                if not column_can_be_field(column,rules,key):
                    if key in column_can_be[n]:
                        column_can_be[n].remove(key)

            if len(column_can_be[n]) == 1: # if only one field remains, add to results (fields[]) and remove it from all other potential allocations
                fields[n] = column_can_be[n].pop()
                for i in range(len(column_can_be)):
                    if i == n: continue

                    if fields[n] in column_can_be[i]:
                        column_can_be[i].remove(fields[n])


    return fields # i.e.: ["class","seat","row"]

def parse_my_ticket(input_string,fields):
    my_ticket_string = input_string.split("\n\n")[1].split("\n")[1]
    my_values = [int(value) for value in my_ticket_string.split(',')]

    return {fields[n]:my_values[n] for n in range(len(my_values))}


print("PART ONE\n")

parsed_rules, merged_rules = parse_all_ranges(input_string)
print("RULES: ", parsed_rules)
print("MERGED: ", merged_rules)

all_values = parse_all_values(input_string)
invalids = get_invalids(all_values, merged_rules)
print("ALL VALUES: ", all_values)
print("INVALID VALUES: ", invalids)
print("SUM: ", sum(invalids))

print("\nPART TWO\n")

parsed_tickets = parse_tickets(input_string)
valid_tickets = get_valid_tickets(parsed_tickets,merged_rules)
print("PARSED TICKETS: \n",parsed_tickets)
print("VALID TICKETS: \n", valid_tickets)

parsed_rules = parse_rules(input_string)
print("PARSED RULES: \n", parsed_rules)

fields = allocate_fields(valid_tickets,parsed_rules)
print("FIELDS: \n", fields)

my_ticket = parse_my_ticket(input_string,fields)

print("MY TICKET:\n", my_ticket)

dep_product = 1
for key in my_ticket.keys():
    if "departure" in key: dep_product *= my_ticket[key]

print("RESULT:\n", dep_product)
