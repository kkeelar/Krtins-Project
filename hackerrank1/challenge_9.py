def timecon():
    s = '07:40:03PM'
    mil_time = '00:00:00'
   
    if s[8:10] == 'PM' and s[0:2] == '12':
        print (s[0:8])
    if s[8:10] == 'AM' and s[0:2] == '12':
        print ('00' + s[2:8])
    
##    else:
##        x = ((s[0]) + (s[1]))
##        hour = (int(x))
##        if s[8:10] == "PM":
##            hour = (int(x) + 12)
##        str_hour = (str(hour))
##        milt_time = (str_hour + s[2:8])
##        milt_time_1 = int(milt_time[0:2])
##        if milt_time_1 < 10:
##            print ("0" + milt_time)
##
##        print (milt_time[0:2])
##    

     else:
       hour = s[0:2]
       if s[8:10] == 'AM' and int(hour) < 12:
           hour = s[0:2]
           print(hour + s[2:8])
           return hour + s[2:8]
       else:
           hour_pm = int(hour) + 12
           return str(hour_pm) + s[2:8]
        

    
timecon()
