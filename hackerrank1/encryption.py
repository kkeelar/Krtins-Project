import math

def encryption():
    s = "Mabappe is the Goat"
    s1 = s.replace(" ", "")
    len_s = (len(s1))
    sq_rt_s = math.sqrt(len_s)
    rows = (int(sq_rt_s))
    colums = (int(sq_rt_s) + 1)
    x = 0
    y = 0
    for i in range(rows):
        #print ("This is x", x)
        y += colums
        #print ("This is y", y)
        print (s1[x:y])
        x += colums


##    print (s1[0:8])
##    print (s1[8:16])
##    print (s1[16:24])
##    print (s1[24:32])        
##    print (s1[32:40])
##    print (s1[40:48])
##    print (s1[48:56])

encryption()
