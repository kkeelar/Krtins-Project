def calender():
    year = 1915
    if year >= 1917 and year % 4 == 0:
        print ("12.09.%d" % year)

    if year >= 1917 and year % 4 != 0:
        print ("13.09.%d" % year)

    if year <= 1917 and year % 400 == 0:
        print ("13.09.%d" % year)

    if year <=  1917 and year % 400 != 0:
        print ("12.09.%d" %  year)

calender()
