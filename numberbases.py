def dectohex():
    while True:
        x = input("input decimal number (exit to stop) >> ")
        if x == "exit":
            break
        print(hex(int(x)))


def converter(func=hex):
    while True:
        x = input("Enter decimal value (exit to stop) >> ")
        if x == "exit":
            break
        else:
            print(func(int(x)) + "\n")


if __name__ == "__main__":
    convertermap = [hex, oct, bin]
    while True:
        print("Pick a base to convert your decimal numbers to!\n"
              "1: Hexadecimal (base 16)\n"
              "2: Octal (base 8)\n"
              "3: Binary (base 2)\n"
              "0: Exit")
        x = input(">> ")
        x = int(x)
        if x == 0:
            break
        elif x > len(convertermap) or x < 0:
            print("Invalid response.")
        else:
            converter(convertermap[x - 1])
