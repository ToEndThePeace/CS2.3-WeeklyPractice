from operator import itemgetter

y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(y)):
    print(y[len(y) - i - 1])

x = {
    14: "vs code",
    3: "window",
    9: "alloc",
    26: "views",
    4: "bottle",
    15: "inbox",
    79: "widescreen",
    16: "coffee",
    19: "tissue",
}

x = [item for item in x.items()]
x.sort(key=itemgetter(0), reverse=True)
for _, item in x:
    print(item)
