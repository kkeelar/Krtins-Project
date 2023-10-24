def seq():
    n = [1, 2, 4, 7, 9, 13]
    p = 5
    num_of_greater = []
    len_n = (len(n))
    

    for index in range(len_n - 1):
        x = (n[index] + n[index + 1])
        if x > p:
            num_of_greater.append(1)

    print (sum(num_of_greater))

seq()
