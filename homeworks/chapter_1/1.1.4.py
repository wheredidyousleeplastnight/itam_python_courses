b = input().split()
n = 0
p = 0
g = 0
for c in range(len(b)):
    b[c] = int(b[c])
for i in range(len(b)):
    if b[i] < 0:
        n += 1
    if b[i] % 2== 0:
        p += 1
    if b[i] > 8:
        g += 1
print(n, g, p)
