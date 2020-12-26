import re
import time

start_time = time.time()
with open("4_input.txt") as f:
    mylist = f.read().split('\n\n')

expected_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

def testheight(x):
    if x.endswith("cm"):
        if 150 <= int(x[:-2]) <= 193:
            return True
    elif x.endswith("in"):
        if 59 <= int(x[:-2]) <= 76:
            return True

validations = {
    "byr": lambda x: isinstance(int(x), int) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: isinstance(int(x), int) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: isinstance(int(x), int) and 2020 <= int(x) <= 2030,
    "hgt": lambda x: testheight(x),
    "hcl": lambda x: isinstance(x, str) and x[0] == "#" and x[1:].isalnum() and len(x[1:]) == 6,
    "ecl": lambda x: isinstance(x, str) and x == "amb" or x == "blu" or x == "brn" or x == "gry" or x == "grn" or x == "hzl" or x == "oth",
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True
}

valid_passports_part1 = 0
valid_passports_part2 = 0

# parse input into list of dict's (being passports)
for passport in mylist:
    passport = (dict(map(lambda x: x.split(':'), (passport.replace('\n',' ')).split(' '))))
    missing_fields = [ele for ele in expected_fields if ele not in passport]

    if len(missing_fields) == 0 or (len(missing_fields) == 1 and "cid" in missing_fields):
        valid_passports_part1 += 1
        if all(validations.get(k, lambda x: False)(v) for (k, v) in passport.items()):
                valid_passports_part2 += 1

print(f'Day 4 Part 1: {valid_passports_part1}')
print(f'Day 4 Part 2: {valid_passports_part2}')
print(f"--- {time.time() - start_time} seconds ---")