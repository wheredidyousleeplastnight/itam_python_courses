a = input()
k1, k2 = False, False
i1, i2 = 0, 0
for i in range(len(a)):
    if a[i].isupper() and k1 == False:
        i1 = i
        k1 = True

    if a[i].isdigit() and k2 == False and not(a[i+1].isdigit()):
        i2 = i+1
        k2 = True
print(a[i1::i2-i1])