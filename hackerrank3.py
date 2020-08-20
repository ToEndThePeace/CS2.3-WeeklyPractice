#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.


def isBalanced(s):
    bracketmap = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []
    for i in s:
        if i not in bracketmap:
            stack.append(i)
        else:
            if len(stack) <= 0 or stack.pop() != bracketmap[i]:
                return "NO"
    if len(stack) > 0:
        return "NO"
    return "YES"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
