import array

def determine():
    arr = array.array("i", [])
    u_i = int(input("Hello, how many numbers do want: "))
    arr = array.array("i", u_i * [1])
    for x in range (0, u_i):
        u_i1 = int(input("> "))
        arr[x] = u_i1
    Gzero = 0
    Lzero = 0
    zero = 0
    for x in (arr):
        if x > 0:
            Gzero += 1
        if x < 0:
            Lzero += 1
        if x == 0:
            zero += 1
    print (Gzero / len(arr))
    print (Lzero / len(arr))
    print (zero / len(arr))

determine()
