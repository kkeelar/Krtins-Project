def sock():
    ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
    pairs = []
    real_pairs = []
    final_pairs = []

    
    for element in range (1, max(ar) + 1):
        print ("this is the element", element)
        y = ar.count(element)
        pairs.append(y)
            
    print ("This is pairs", pairs)

    for element in (pairs):
        if element >= 2 and element % 2 == 0:
            real_pairs.append(element)
        if element > 2 and element % 2 != 0:
            element = element - 1
            real_pairs.append(element)

    print ("This is real_pairs", real_pairs)

    num_of_pairs = (sum(real_pairs) / 2)

    print (num_of_pairs)
    
sock()
