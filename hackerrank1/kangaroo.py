def kangaroo():
    x1 = [21]
    v1 = [6]
    x2 = [47]
    v2 = [3]
    if x1 > x2 and v1 > v2:
        print ("NO")

    if x1 < x2 and v1 < v2:
        print ("NO")

    if x1 > x2 and v1 < v2:
        print ("YES")

    if x2 > x1 and v1 > v2:
        print ("YES")

kangaroo()
