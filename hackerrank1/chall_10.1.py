def seq():
    n = 3
    p = 4
    list_n = []
    num_of_greater = []
    for index in range (n + 1):
        list_n.append(index)
        
    for index in range(0, len(list_n)):
        for index_1 in range(1, len(list_n)):
                             print (list_n[index], list_n[index_1])
                             c = (list_n[index] * list_n[index_1])
                             if c <= p:
                                 num_of_greater.append(1)


            

    
            




    print (len(num_of_greater))

seq()
