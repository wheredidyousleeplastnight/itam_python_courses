z1,z2,l = 0,0,0
n = int(input())
for i in range(n):
    stroki = input().split()
    if stroki.count('True') + stroki.count('False') >= 2:
        if stroki[3] == 'True':
            z1 += 1
        elif stroki[3]=='False':
            z2 += 1
        else:
            l += 1
    else:
        if stroki.count('True') == 1 and stroki.count('False') == 0:
            z1 += 1
        else:
            z2 += 1



print(z1, z2, l)





