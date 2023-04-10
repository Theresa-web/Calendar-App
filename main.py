import calendar
import datetime
import geocoder
import os
import sys

def get_calendar(year=None, month=None):
    if not year:
        year = datetime.datetime.now().year
    if not month:
        month = datetime.datetime.now().month
    cal = calendar.monthcalendar(year, month)
    current_day = datetime.datetime.now().day

    month_name = calendar.month_name[month]
    print(month_name + '' + str(year))
    print(calendar.weekheader(2))
    print()
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '   '
            elif day == current_day and year == datetime.datetime.now().year and month == datetime.datetime.now().month:
                week_str += '\033[0;30;47m' + str(day) + '\033[0m' + ' '
            else:
                week_str += str(day) + ' '
        print(week_str)

def get_lat_long():
    g = geocoder.ip('me')
    return g.latlng

if len(sys.argv) == 1:
    get_calendar()
elif len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print('Usage: python calendar_app.py [month] [year]')
        print('If no arguments are provided, the current month’s calendar will be displayed.')
        print('If a month and a year are provided, the calendar for that month and year will be displayed.')
    else:
        try:
            year = datetime.datetime.now().year
            month = int(sys.argv[1])
            get_calendar(year, month)
        except ValueError:
            print('Invalid arguments. Type python calendar_app.py help for more information.')
elif len(sys.argv) == 3:
    try:
        year = int(sys.argv[2])
        month = int(sys.argv[1])
        get_calendar(year, month)
    except ValueError:
        print('Invalid arguments. Type python calendar_app.py help for more information.')
else:
    print('Invalid arguments. Type python calendar_app.py help for more information.')
