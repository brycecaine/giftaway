from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
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
	# Generate list of upcoming holidays to add to the occasions list
	# Make this pull from a table
	holidays = [{'name': 'Christmas', 'month': 12, 'day': 25, 'weekday': None, 'ordinal': None},
				{'name': 'Memorial Day', 'month': 5, 'day': None, 'weekday': 0, 'ordinal': -1}]

	for holiday in holidays:
		upcoming_holiday = service.get_upcoming_holiday(holiday)
		opportunities_list.append(upcoming_holiday)

	# -------------------------------------------------------------------------
	# Generate list of user-specific occasions to add to the occasions list
	occasions = [{'giver': 'Bryce', 'recipient': 'Kathy', 'event': 'Birthday', 'date': date(1981, 8, 20)},
				 {'giver': 'Bryce', 'recipient': 'Kathy', 'event': 'Anniversary', 'date': date(2005, 6, 17)}]

	for occasion in occasions:
		upcoming_occasion = service.get_upcoming_occasion(occasion)
		opportunities_list.append(upcoming_occasion)

	logger.debug(opportunities_list)

	for opportunity in opportunities_list:
		logger.debug(opportunity['opportunity_date'])
		logger.debug(date.today() + timedelta(days=USER_OUTLOOK_DAYS))
		if opportunity['opportunity_date'] <= date.today() + timedelta(days=USER_OUTLOOK_DAYS):
			opportunities.append(opportunity)

	opportunities = sorted(opportunities, key=lambda k: k['opportunity_date']) 

	# occasions = ['hi', 2]

	return render_to_response('index.html', locals(), context_instance=RequestContext(request))