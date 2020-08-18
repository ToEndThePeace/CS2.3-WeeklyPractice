#!/bin/python3

import math
import os
import random
import re
import sys


def tower(n, pos):
    rods = [[], [], [], []]
    ind = {}
    moves = 0

    def move_disc(r):
        nonlocal moves
        moves += 1
        x = rods[r].pop()
        while len(rods[0]) > 0 and rods[0][-1] < x:
            move_disc(0)
        for i in range(4):
            if i == r:
                continue
            else:
                if len(rods[i]) == 0 or rods[i][-1] > x:
                    rods[i].append(x)
                    ind[x] = i
                    break
        print(rods)

    for i in range(len(pos)):
        rods[pos[len(pos) - i - 1] - 1].append(len(pos) - i)
        ind[len(pos) - i] = pos[len(pos) - i - 1] - 1
    print(rods)
    # for i in range(len(rods[0]) - 1):
    #     if rods[0][i] != rods[0][i + 1] + 1:
    #         move_disc(0)
    for i in range(n):
        cur = len(pos) - i
        while ind[cur] != 0:
            move_disc(ind[cur])
    print(rods)
    print(moves)


if __name__ == '__main__':
    """
    Test Inputs         Outputs
    3, 1 4 1            3
    3, 1 3 3            5
    4, 2 4 4 4          8
    6, 1 4 2 4 2 2      14
    """
    N = int(input())

    a = list(map(int, input().rstrip().split()))

    tower(N, a)
