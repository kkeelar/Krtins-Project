def climbing():
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    ranked_places = []
    placements = []


    for index in range(len(ranked)-1):
        if ranked[index] == ranked[index + 1]:
            ranked_places.append(index + 1)
        ranked_places.append(index + 1)


    for element in (player):
        for index in range(len(ranked)):
            if element == ranked[index]:
                placements.append(ranked_places[index])

    for element in (player):
        if element > max(ranked):
                placements.append(1)
        if element < min(ranked):
                placements.append(len(ranked))
        for index in range(len(ranked)-1):
            if element < ranked[index] and element > ranked[index + 1] and index == 0:
                placements.append(index + 2)
            if element < ranked[index] and element > ranked[index + 1] and index > 0:
                placements.append(index + 1)
           
        
    print ("This is placements", placements)
    print ("This is ranked places", ranked_places)




climbing()





##    for element in player:
##        if element < min(ranked):
##            placements.append(len(ranked))
##    
