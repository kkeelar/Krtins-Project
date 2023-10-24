def compareTriplets():
    a = [1, 15, 98, 8]
    sum_1 = 0
    sum_2 = 0
    
    for x in (a):
        sum_1 = sum_1 + x

    print(sum_1)

    for x in range(len(a)):
        sum_2 = sum_2 + a[x]

    print(sum_2)

    y = 0
    sum_3 = 0
    while(y < len(a)):
        sum_3 = sum_3 + a[y]
        y = y + 1
    
    print(sum_3)  


compareTriplets()
def diagonalDifference(arr):

    dig_1_sum = 0     
    for x in (len(arr)):
            for y in (arr): 
                dig_1 = dig_1 + arr[x][y]


4, 0
3, 1
2, 2
1, 3
0, 4
                
