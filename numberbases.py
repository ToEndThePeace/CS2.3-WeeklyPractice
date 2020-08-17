def dectohex():
    while True:
        x = input("input decimal number (exit to stop) >> ")
        if x == "exit":
            break
        print(hex(int(x)))


def dectooct():
    pass


if __name__ == "__main__":
    funcmap = [dectohex, dectooct]
    while True:
        print("Pick a base to convert your decimal numbers to!\n",
              "1: Hexadecimal (base 16)\n",
              "2: Octal (base 8)\n",
              "0: Exit")
        x = input(">> ")
        x = int(x)
        if x == 0:
            break
        elif x >= len(funcmap) or x < 1:
            print("Invalid response.")
        else:
            funcmap[x - 1]()
