def sam():
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6,]
    num_of_apples = []
    num_of_oranges = []
    for x in range (len(apples)):
         apple_loc = a + apples[x]
         if apple_loc >= s and apple_loc <= t:
             num_of_apples.append(1)
      
        
    for x in range (len(oranges)):
         orange_loc = b + oranges[x]
         if orange_loc >= s and orange_loc <= t:
            num_of_oranges.append(1)
                
    print (len(num_of_apples))
    print (len( num_of_oranges))

sam()
