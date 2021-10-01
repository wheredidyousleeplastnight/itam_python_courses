a = []
n = int(input())
z1 = 0
z2 = 0
for i in range(n):
    stroki = input().split()
    a.append(stroki)

for g in range(len(a)):
    if 'True' in a[g]:
        z1 += 1
    else:
        z2 += 1

print(z1, z2)