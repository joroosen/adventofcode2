import itertools
import time

start_time = time.time()
with open("2_input.txt") as f:
    mylist = f.read().splitlines()

valid_passwords = 0
for entry in mylist:
    policy_number = ((entry.split(": ", 1)[0]).split(" ", 1)[0]).split("-",1)
    policy_letter = (entry.split(": ", 1)[0]).split(" ", 1)[1]
    password = entry.split(": ", 1)[1]
    if int(policy_number[0]) <= password.count(policy_letter) <= int(policy_number[1]):
        valid_passwords += 1

print(f'Valid passwords: {valid_passwords}')

print(f"--- {time.time() - start_time} seconds ---")

#oplossing Beto:
# import re
#
# pattern = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
# lines = open('2_input.txt').read().splitlines()
#
#
# passwords_accepted = 0
# for line in lines:
#     matching = pattern.match(line)
#     if matching:
#         minimum, maximum, allowed_char, password = matching.groups()
#         if int(minimum) <= password.count(allowed_char) <= int(maximum):
#             passwords_accepted += 1
# print(f'Answer: {passwords_accepted}')