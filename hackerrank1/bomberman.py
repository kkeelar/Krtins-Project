def bomberman():
    grid = [[".", ".", ".",],
              [".", "0", ".",],
              [".", ".", ".",]]




    r = 3
    c = 3
    n = 3

  
    if n <= 1:
        for x in range (r):
            for y in range(c):
                print (grid[x][y], end = ' ')
            print(end = "\n")




    locations = []
    
    if n > 2:
        for x in range(r):
            for y in range(c):
                if grid[x][y] == "0":
                    element = [x,y]
                    locations.append(element)
                else:
                    
                    grid[x][y] = "0"





    if n == 3:
        for element in locations:
            grid[element[0]][element[1]] = "."
            if element[0] + 1 <= r-1:
                grid[element[0] + 1][element[1]] = "."
            
            if element[0] - 1 >= 0:
                grid[element[0] - 1][element[1]] = "."

            
            if element[1] + 1 <= c-1:
                grid[element[0]][element[1] + 1] = "."

            
            if element[1] - 1 >= 0:
                grid[element[0]][element[1] - 1] = "."
                

                        
        
                            
                if x+1 <= r-1:
                    grid[x + 1][y] = "."
                if x-1 >= 0:
                    grid[x - 1][y] = "."
                if y+1 <= c-1:
                    grid[x][y + 1] = "."
                if y-1 >= 0:
                     grid[x][y - 1] = "."
                            

        
        for x in range (r):
            for y in range(c):
                print (grid[x][y], end = ' ')
            print(end = "\n")
                    
            

   
bomberman()
