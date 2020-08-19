#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.


def timeInWords(h, m):
    wordmap = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "half"
    }
    res = ""

    if m <= 30:
        if m == 0:
            res += f"{wordmap[h]} "
            res += "o' clock"
        else:
            res += wordmap[m]
            if m != 15 and m != 30:
                if m == 1:
                    res += " minute"
                else:
                    res += " minutes"
            res += f" past {wordmap[h]}"
    else:
        if h == 12:
            res += wordmap[1]
        else:
            res += wordmap[60 - m]

        if m != 45 and m != 30:
            if m == 1:
                res += " minute"
            else:
                res += " minutes"
        res += f" to {wordmap[h + 1]}"
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
