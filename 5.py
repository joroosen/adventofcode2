import time

start_time = time.time()
with open("5_input.txt") as f:
    mylist = f.read().splitlines()

def get_seat(bsp_id):
    rows = list(range(128))
    seats = list(range(8))
    for i in bsp_id:
        if i == "F":
            rows = rows[:int(len(rows)/2)]
        elif i == "B":
            rows = rows[int(len(rows)/2):]
        elif i == "R":
            seats = seats[int(len(seats)/2):]
        elif i == "L":
            seats = seats[:int(len(seats)/2)]

    return(rows[0], seats[0])

seats = []

for bpass in mylist:
    pass_temp = get_seat(bpass)
    seats.append(pass_temp[0] * 8 + pass_temp[1])

seats.sort()
myseat = 0

for i in range(1,len(seats)-1):
    if seats[i]+1 not in seats and seats[i+1]-1 not in seats:
        myseat = seats[i]+1

print(f'Day 5 Part 1: {max(seats)}')
print(f'Day 5 Part 2: {myseat}')
print(f"--- {time.time() - start_time} seconds ---")


translation = { 'F': '0', 'B': '1', 'L': '0', 'R': '1'}

# found at jjbeto ....nice
# https://github.com/jjbeto/adventofcode2020/blob/master/day05.ipynb

def seat_id_v2(ticket):
    return int(''.join([translation[letter] for letter in ticket]),2    )

print(seat_id_v2('FBFBBFFRLR'))
