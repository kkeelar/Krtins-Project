import array
import sys


def max_min():
    arr = array.array("i", [1, 3, 5, 7, 9])
    total_min_sum = (sum(arr))
    max_1 = 0
    for x in range (len(arr)):
        if arr[x] >= max_1:
            max_1 = arr[x]
    print (total_min_sum - max_1)

    total_max_sum = (sum(arr))
    min_1 = 100
    for x in range (len(arr)):
        if arr[x] <= min_1:
            min_1 = arr[x]
    print (total_max_sum - min_1)
    

max_min()
        
