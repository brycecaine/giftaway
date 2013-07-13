from datetime import date
import logging

logger = logging.getLogger(__name__)

MONTH_DAY_COUNT = {1 : 31,
                   2 : 28, # not worrying about leap years for now
                   3 : 31,
                   4 : 30,
                   5 : 31,
                   6 : 30,
                   7 : 31,
                   8 : 31,
                   9 : 30,
                   10: 31,
                   11: 30,
                   12: 31}

def get_upcoming_holiday(holiday):
	current_year = date.today().year

	if holiday['name'] == 'Easter':
		holiday_date = calc_easter(current_year)
	
	elif holiday['day']:
		holiday_date = date(current_year, holiday['month'], holiday['day'])

	else: # handle a holiday that has a rule-based date
		month_weekdays = []
		for i in range(1, MONTH_DAY_COUNT[holiday['month']] + 1): # the starting-point 1 and the + 1 make this a 1-based loop
			loop_date = date(current_year, holiday['month'], i)
		
			if loop_date.weekday() == holiday['weekday']:
				month_weekdays.append(loop_date)

		holiday_date = month_weekdays[holiday['ordinal']]

	if holiday_date < date.today():
		holiday_date = date(current_year + 1, holiday_date.month, holiday_date.day)
	
	upcoming_holiday = {'name': holiday['name'], 'opportunity_date': holiday_date}

	return upcoming_holiday

# calc_easter from http://goo.gl/v63w1
def calc_easter(year):
    # "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    
    return date(year, month, day)

def get_upcoming_occasion(occasion):
	current_year = date.today().year

	occasion_date = date(current_year, occasion['date'].month, occasion['date'].day)

	if occasion_date < date.today():
		occasion_date = date(current_year + 1, occasion_date.month, occasion_date.day)
	
	upcoming_occasion = {'name': '{0}\'s {1}'.format(occasion['recipient'], occasion['event']), 'opportunity_date': occasion_date}

	return upcoming_occasion










