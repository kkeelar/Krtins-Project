def b():
    arr = [1, 4, 4, 4, 5, 5, 5, 3]
    bird = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird[arr[i]] += 1
    print (bird.index(max(bird)))


    print (bird)


            

b()
        
        
