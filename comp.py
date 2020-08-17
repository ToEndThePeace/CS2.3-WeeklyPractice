# the index into the memory array is the location of the memory

# 1 - Print_BEEJ
# 2 - HALT

memory = [  # big array of bytes, 8 bits per byte
    1,
    1,
    1,
    2
]

running = True

pc = 0  # current memory index

while running:
    ir = memory[pc]

    if ir == 1:
        print("BEEJ")
        pc += 1
    else:
        running = False
        pc += 1
