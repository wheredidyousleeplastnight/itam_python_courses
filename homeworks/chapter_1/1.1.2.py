a = input().split()
min = 0
max = 0
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
print(a[min], a[max])