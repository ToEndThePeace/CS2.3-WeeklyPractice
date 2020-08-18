# the index into the memory array is the location of the memory

# 1 - PRINT_BEEJ
# 2 - HALT
# 3 - SAVE_REG
# 4 - PRINT_REG print the register value

memory = [  # big array of bytes, 8 bits per byte
    1,  # PRINT_BEEJ

    3,  # SAVE_REG R$ 37, 3 is the "opcode" or "instruction"
    4,  # 4 and 37 are "operands" or "arguments"
    37,

    4,  # PRINT_REG R4
    4,

    2
]

"""
registers[4] = 37
"""


registers = [0] * 8

running = True

pc = 0  # current memory index

while running:
    ir = memory[pc]
    # print(ir)
    if ir == 1:
        print("BEEJ")
        pc += 1

    elif ir == 2:
        running = False
        pc += 1

    elif ir == 3:
        # get relevant arguments from memory
        indx = memory[pc + 1]
        val = memory[pc + 2]

        # update value and print it
        registers[indx] = val

        # increment past the arguments from this function call
        pc += 3

    elif ir == 4:
        indx = memory[pc + 1]
        print(registers[indx])
        pc += 2

    # num_args = ir >> 6  # this is a right-shift operator!
    # size_of_inst = num_args + 1
    # pc += size_of_inst
