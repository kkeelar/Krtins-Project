def time_in_words():
    h = 5
    hour = ""
    m = 47
    minute = ""
    if h == 1:
        hour = ("one")
    if h == 2:
        hour = ("two")
    if h == 3:
        hour = ("three")
    if h == 4:
        hour = ("four")
    if h == 5:
        hour = ("five")
    if h == 6:
        hour = ("six")
    if h == 7:
        hour = ("seven")
    if h == 8:
        hour = ("eight")
    if h == 9:
        hour = ("nine")
    if h == 10:
        hour = ("ten")
    if h == 11:
        hour = ("eleven")
    if h == 12:
        hour = ("tweleve")

    if m == 1:
        minute = ("one")
    if m == 2:
        minute = ("two")
    if m == 3:
        minute = ("three")
    if m == 4:
        minute = ("four")
    if m == 5:
        minute = ("five")
    if m == 6:
        minute = ("six")
    if m == 7:
        minute = ("seven")
    if m == 8:
        minute = ("eight")
    if m == 9:
        minute = ("nine")
    if m == 10:
        minute = ("ten")
    if m == 11:
        minute = ("eleven")
    if m == 12:
        minute = ("tweleve")
    if m == 13:
        minute = ("thriteen")
    if m == 14:
        minute = ("fourteen")
    if m == 15:
        minute = ("fifteen")
    if m == 16:
        minute = ("sixteen")
    if m == 17:
        minute = ("seventeen")
    if m == 18:
        minute = ("eighteen")
    if m == 19:
        minute = ("nineteen")
    if m == 20:
        minute = ("twenty")
    if m == 21:
        minute = ("twenty one")
    if m == 22:
        minute = ("twenty two")
    if m == 23:
        minute = ("twenty three")
    if m == 24:
        minute = ("twenty four")
    if m == 25:
        minute = ("twenty five")
    if m == 26:
        minute = ("twenty six")
    if m == 27:
        minute = ("twenty seven")
    if m == 28:
        minute = ("twenty eight")
    if m == 29:
        minute = ("twenty nine")
    if m == 30:
        minute = ("thrity")
    if m == 31:
        minute = ("thrity one")
    if m == 32:
        minute = ("thrity two")
    if m == 33:
        minute = ("thrity three")
    if m == 34:
        minute = ("thrity four")
    if m == 35:
        minute = ("thrity five")
    if m == 36:
        minute = ("thrity six")
    if m == 37:
        minute = ("thrity seven")
    if m == 38:
        minute = ("thrity eight")
    if m == 39:
        minute = ("thrity nine")
    if m == 40:
        minute = ("forty")
    if m == 41:
        minute = ("forty one")
    if m == 42:
        minute = ("forty two")
    if m == 43:
        minute = ("forty three")
    if m == 44:
        minute = ("forty four")
    if m == 45:
        minute = ("forty five")
    if m == 46:
        minute = ("forty six")
    if m == 47:
        minute = ("forty seven")
    if m == 48:
        minute = ("forty eight")
    if m == 49:
        minute = ("forty nine")
    if m == 50:
        minute = ("fifty")
    if m == 51:
        minute = ("fifty one")
    if m == 52:
        minute = ("fifty two")
    if m == 53:
        minute = ("fifty three")
    if m == 54:
        minute = ("fifty four")
    if m == 55:
        minute = ("fifty five")
    if m == 56:
        minute = ("fifty six")
    if m == 57:
        minute = ("fifty seven")
    if m == 58:
        minute = ("fifty eight")
    if m == 59:
        minute = ("fifty nine")
    if m == 60:
        minute = ("sixity")
    

    
    if m == 0:
        print (hour, "o'clock")

    if m == 1:
        print (hour, minute,"minute past", hour)

    if m > 0 and m < 15:
        print (hour, minute, "minutes past five")

    if m == 15:
        print ("quarter past", hour)

    if m > 15 and m < 30:
        print (hour, minute, "minutes past five")

    if m == 30:
        print ("half past", hour)

    

    if m > 30 and m < 45:
        m = 60 - m
        if m == 31:
            minute = ("thrity one")
        if m == 32:
            minute = ("thrity two")
        if m == 33:
            minute = ("thrity three")
        if m == 34:
            minute = ("thrity four")
        if m == 35:
            minute = ("thrity five")
        if m == 36:
            minute = ("thrity six")
        if m == 37:
            minute = ("thrity seven")
        if m == 38:
            minute = ("thrity eight")
        if m == 39:
            minute = ("thrity nine")
        if m == 40:
            minute = ("forty")
        if m == 41:
            minute = ("forty one")
        if m == 42:
            minute = ("forty two")
        if m == 43:
            minute = ("forty three")
        if m == 44:
            minute = ("forty four")
        
            
        print (minute, "minutes to", hour)

    if m == 45:
        print ("quarter to", hour + 1)

    if m > 45 and m <= 59:
        m = 60 - m
        if m == 46:
            minute = ("forty six")
        if m == 47:
            minute = ("forty seven")
        if m == 48:
            minute = ("forty eight")
        if m == 49:
            minute = ("forty nine")
        if m == 50:
            minute = ("fifty")
        if m == 51:
            minute = ("fifty one")
        if m == 52:
            minute = ("fifty two")
        if m == 53:
            minute = ("fifty three")
        if m == 54:
            minute = ("fifty four")
        if m == 55:
            minute = ("fifty five")
        if m == 56:
            minute = ("fifty six")
        if m == 57:
            minute = ("fifty seven")
        if m == 58:
            minute = ("fifty eight")
        if m == 59:
            minute = ("fifty nine")

       
        
        print (minute, "minutes to", hour)
 



time_in_words()
