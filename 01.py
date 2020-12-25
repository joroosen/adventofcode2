import itertools
import time

start_time = time.time()
with open("01_input.txt") as f:
    mylist = f.read().splitlines()


for a, b in itertools.combinations(mylist, 2):
    if int(a) + int(b) == 2020:
        print(int(a) * int(b))
        break

print("--- %s seconds ---" % (time.time() - start_time))