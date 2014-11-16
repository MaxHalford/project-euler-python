#is a year a leap year?
def leapYear(year):
    answer=True
    if year%100==0:
        if year%400!=0:
            answer=False
    else:
        if year%4!=0:
            answer=False
    return answer
#array with the number of days for each month           
days=[31,0,31,30,31,30,31,31,30,31,30,31]
#array with the days of the week
week=['mo','tu','we','th','fr','sa','su']
#when you move forward through the days of the week you go from Sunday to Monday
def moveAhead(array,current,move):
    move=move%len(array)
    current=(current+move)%7
    return current
#tmpDay will correspond to the index of the day of the week for the first day of a month
tmpDay=1
#nbSundays is the answer
nbSundays=0
#let's go through every year
for year in range(1901,2001):
    #if a year is a leap year it's first day is either 1 (normal) or 2 (leap year) more days ahead of the first day from the previous year
    if leapYear(year)==False:
        tmpDay=moveAhead(week,tmpDay,365%7)
    else:
        tmpDay=moveAhead(week,tmpDay,366%7)
    #let's check every month of the year
    for month in range(0,12):
        #check the first day of the first month to see if it's a Sunday
        if week[tmpDay]=='su':
            nbSundays+=1
        #then we set the number of days for February
        if leapYear(year)==False:
            days[1]=28
        else:
            days[1]=29
        tmpDay=moveAhead(week,tmpDay,days[month])
    if leapYear(year)==False:
        tmpDay=moveAhead(week,tmpDay,365%7)
    else:
        tmpDay=moveAhead(week,tmpDay,366%7)
print(nbSundays)