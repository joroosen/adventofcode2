import itertools
import time

start_time = time.time()
with open("01_input.txt") as f:
    mylist = f.read().splitlines()


for a, b, c in itertools.combinations(mylist, 3):
    if int(a) + int(b) + int(c) == 2020:
        print(int(a) * int(b) * int(c))
        break

print("--- %s seconds ---" % (time.time() - start_time))