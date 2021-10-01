a = input()
b = list(a)
if len(b) > 6:
    c1 = b.pop(3-1)
    c2 = b.pop(5-1)
    print(c1, c2)
else:
    c3 = b[:: -1]
    c4 = c3[::2]
    print(c4)