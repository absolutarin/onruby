
def is_leap(year):
    global leap
    if (year>999 and year<10000):
        if ( year%4==0 and (year%100!=0 or year%4==0)):
            leap = True
            print ("{0} is a leap year".format(year))
        else:
           leap = False
           print ("{0} aint a leap year".format(year))
    else:
        print ("Year must have 4 digits")
    return leap    
