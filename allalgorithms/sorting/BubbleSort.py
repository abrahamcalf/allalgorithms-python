a = [10, 40, 90, 20, 50, 30, 80, 60, 70]
for i in range(len(a)-1, 0, -1):
    swapped = 0
    for j in range(i):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swapped = 1
    if swapped == 0:
        break

print(a)
