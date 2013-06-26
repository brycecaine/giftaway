from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):

	try:
		user = request.user

	except:
		user = None

	return render_to_response('index.html', locals(), context_instance=RequestContext(request))