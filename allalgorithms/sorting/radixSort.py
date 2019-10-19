def radixSort(A):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for  i in A:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        placement *= RADIX
    return A
