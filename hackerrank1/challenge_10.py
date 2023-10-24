def seq():
    p = 3
    n = 4
    list_n = []
    num_of_greater = []
    for index in range (n + 1):
        list_n.append(index)
        
    for index in range(1, len(list_n)):
        print (list_n[index], list_n[index])
        a = (list_n[index] * list_n[index])
        if a <= p:
            num_of_greater.append(1)

    
            
        if index <= (len(list_n)):
            print (list_n[index], list_n[index + 1])
            b = (list_n[index] * list_n[index + 1])
            if b <= p:
                num_of_greater.append(1)

    index = (len(list_n) -1)
    while index > 0:
        if index -1 > 0:
            print (list_n[index], list_n[index - 1])
            c = list_n[index] * list_n[index - 1]
            if c <= p:
                num_of_greater.append(1)

        index = index -1




    print (len(num_of_greater))

seq()
