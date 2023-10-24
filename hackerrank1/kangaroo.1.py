def kangaroo():
    x1 = [21]
    v1 = [6]
    x2 = [47]
    v2 = [3]
    for index in range (10000):
        x1 += v1
        x2 += v2
        if x2 == x1:
            print ("YES")
        else:
            continue

    print ("NO")

kangaroo()
