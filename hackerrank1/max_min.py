import array
arr = array.array("i", [23, 1, -2, 100, 101, 0, 25])
max_1 = -100
##for x in (arr):
##    if x > max_1:
##        max_1 = x
max_index = -1
for x in range (len(arr)):
    if arr[x] >= max_1:
        max_1 = arr[x]
        max_index = x
        

print ("The maximun elemnet is ", max_1, " And its index is ", max_index)
min_1 = 100
min_index = 0
for x in range (len(arr)):
    if arr[x] <= min_1:
        min_1 = arr[x]
        min_index = x
        
print ("The mininum element is ", min_1, "And its index is ", min_index)
        
