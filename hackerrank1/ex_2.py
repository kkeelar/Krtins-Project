
def compareTriplets():
    a = [1, 15, 98, 8]
    b = [2, 4, 99, 8]

    a_p = 0
    b_p = 0
    for x in range (len(a)):
        if a[x] > b [x]:
            a_p = a_p + 1
            
        if b[x] > a[x]:
            b_p = b_p + 1
            
        if b[x] == a[x]:
            continue 
        
    print (a_p, b_p)

compareTriplets()
