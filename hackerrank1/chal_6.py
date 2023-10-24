def staircase():
    u_i = int(input("Hello, how big would you like your staircase: "))
    print (u_i * " ", "#")
    y = 2
    u_i_1 = u_i -1 
    while y < (u_i_1  + u_i):
        print (u_i_1 * " ", y * "#")
        y += 1
        u_i_1 -= 1

staircase()
