import datetime

def wishme():
    a=""
    time = datetime.datetime.now().hour
    if(time >= 0 and time < 12):
        a="Good Morning Boss!"
    elif(time >= 12 and time < 17):
        a="Good Afternoon Boss!"
    else:
        a="Good Evening Boss!"
    return a


def tellDay():
    a=""
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        a=f"The day is {day_of_the_week}"
        print(a)
    return a

def tell_Tomorrow_Day():
    a=""
    day = datetime.datetime.today().weekday() + 2
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day >= 8:
        day=1
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        a=f"The day is {day_of_the_week}"
        print(a)
    return a

def tellTime():
    a=""
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    a=f"The time is {hour} Hours and {min} Minutes"
    print(a)
    return a
