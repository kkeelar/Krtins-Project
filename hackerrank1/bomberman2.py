
def bomberman():
    n = 3
    r = 3
    c = 3

    grid = [[".", ".", "."],
              [".", "0", "."],
              [".", ".", "."]]




    if n <= 1:
        for x in range (r):
            for y in range(c):
                print (grid[x][y], end = ' ')
            print(end = "\n")
    
    locations = []
    
    if n == 2:
        for x in range(r):
            for y in range(c):
                if grid[x][y] != "0":
                   grid[x][y] = "0"
                    
        for x in range (r):
            for y in range(c):
                print (grid[x][y], end = ' ')
            print(end = "\n")

    if n == 3:
        for x in range(r):
            for y in range(c):
                if grid[x][y] == "0":
                    element = [x,y]
                    locations.append(element)
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
                


                            

        
        for x in range (r):
            for y in range(c):
                print (grid[x][y], end = ' ')
            print(end = "\n")
            
        print (grid)


bomberman()
    
    
