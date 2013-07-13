from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
from giftplanner.models import GiverHoliday, Occasion
from giftplanner import service
import logging

logger = logging.getLogger(__name__)

def home(request):

	USER_OUTLOOK_DAYS = 60

	try:
		user = request.user

	except:
		user = None

	opportunities_list = []
	opportunities = []

	# -------------------------------------------------------------------------
	# Generate list of upcoming holidays to add to the occasions list. The list
	# should be a list of dicts like this:
	# holidays = [{'name': 'Christmas', 'month': 12, 'day': 25, 'weekday': None, 'ordinal': None},
	# 			{'name': 'Memorial Day', 'month': 5, 'day': None, 'weekday': 0, 'ordinal': -1}]

	holidays = GiverHoliday.objects.filter(giver=user).values('holiday__name',
		                                                      'holiday__month',
		                                                      'holiday__day',
		                                                      'holiday__weekday',
		                                                      'holiday__ordinal')

	for holiday in holidays:
		holiday['name'] = holiday['holiday__name']
		holiday['month'] = holiday['holiday__month']
		holiday['day'] = holiday['holiday__day']
		holiday['weekday'] = holiday['holiday__weekday']
		holiday['ordinal'] = holiday['holiday__ordinal']

		holiday.pop('holiday__name')
		holiday.pop('holiday__month')
		holiday.pop('holiday__day')
		holiday.pop('holiday__weekday')
		holiday.pop('holiday__ordinal')

		upcoming_holiday = service.get_upcoming_holiday(holiday)
		opportunities_list.append(upcoming_holiday)

	# -------------------------------------------------------------------------
	# Generate list of user-specific occasions to add to the occasions list.
	# The list should be a list of dicts like this:
	# occasions = [{'giver': 'Bryce', 'recipient': 'Kathy', 'event': 'Birthday', 'event_date': date(1981, 8, 20)},
	# 			 {'giver': 'Bryce', 'recipient': 'Kathy', 'event': 'Anniversary', 'event_date': date(2005, 6, 17)}]

	occasions = Occasion.objects.filter(giver=user).values('giver', 'recipient', 'event', 'event_date', 'recipient__username')

	for occasion in occasions:
		occasion['recipient'] = occasion['recipient__username']
		occasion.pop('recipient__username')
		upcoming_occasion = service.get_upcoming_occasion(occasion)
		opportunities_list.append(upcoming_occasion)

	for opportunity in opportunities_list:
		if opportunity['opportunity_date'] <= date.today() + timedelta(days=USER_OUTLOOK_DAYS):
			opportunities.append(opportunity)

	opportunities = sorted(opportunities, key=lambda k: k['opportunity_date']) 

	# occasions = ['hi', 2]

	return render_to_response('index.html', locals(), context_instance=RequestContext(request))