def sum():
    a = [0, 2, 7, 8]
    sum_1 = 0
    for x in (a):
        sum_1 = sum_1 + x

    print (sum_1)

    sum_1 = 0

    for x in range (len(a)):
        sum_1 = sum_1 + a[x]

    print(sum_1)

    sum_1 = 0

    y = 0
    while (y < len(a)):
        sum_1 = sum_1 + a[y]
        y = y + 1

    print (sum_1)


sum()
