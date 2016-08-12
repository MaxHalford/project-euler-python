# is a year a leap year?
def leapYear(year):
    answer = True
    if year % 100 == 0:
        if year % 400 != 0:
            answer = False
    else:
        if year % 4 != 0:
            answer = False
    return answer
# when you move forward through the days of the week you go from Sunday to Monday
def moveAhead(current, move):
    move = move % 7
    current = (current + move) % 7
    return current
# array with the number of days for each month           
days=[31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# array with the days of the week
week=['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
# yearDay will correspond to the index of the day of the week for the first day of a year
yearDay = 2
# nbSundays is the answer
nbSundays = 0
# let's go through every year
for year in range(1901, 2001):
    if not(leapYear(year)):
        yearDay = moveAhead(yearDay, 365)
        # monthDay will correspond to the index of the day of the week for the first day of a month
        monthDay = yearDay
        # set the days for February
        days[1] = 28
    else:
        yearDay = moveAhead(yearDay, 366)
        monthDay = yearDay
        days[1] = 29
    # let's check every month of the year
    for month in range(0, 12):
        # check the first day of the first month to see if it's a Sunday
        if week[monthDay] == 'su':
            nbSundays += 1
        monthDay = moveAhead(monthDay, days[month])
print(nbSundays)
