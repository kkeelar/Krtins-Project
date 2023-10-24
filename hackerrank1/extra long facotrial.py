def extra_long_factorial():
    n = 30
    n1 = 1
    for element in range(n):
        n1 *= n
        n = n - 1
        
    print (n1)


extra_long_factorial()
