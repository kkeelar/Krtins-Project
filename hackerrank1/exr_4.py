import array

def diagonalDifference():
    arr = [[0 for x in range(3)] for y in range(3)]
    arr[0][0] = 15
    arr[0][1] = 15
    arr[0][2] = 15
    arr[1][0] = 15
    arr[1][1] = 15
    arr[1][2] = 15
    arr[2][0] = 15
    arr[2][1] = 15
    arr[2][2] = 15
    dig_1_sum = 0
    
    for x in range(len(arr)):
        dig_1_sum = dig_1_sum + arr[x][x]
        
    print (dig_1_sum)    
    
    dig_2_sum = 0     
    m = len(arr)-1
    n = 0
    while m >= 0 and n < len(arr):
        dig_2_sum = dig_2_sum + arr[m][n]
        m = m - 1
        n = n + 1
        
    print (dig_2_sum)
    print (len(arr))
    
    diff = dig_1_sum - dig_2_sum
    if diff < 0:
        diff = diff * -1
    return diff

diagonalDifference()
