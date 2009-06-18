from datetime import *
from django.shortcuts import render_to_response, get_object_or_404

from testcalendar.event.models import Event

events = [
		{ 'day':datetime(2009,6,30), 'title':"Concert at Huckelberries", 'class':"concert",    'url':'/foo/2' },
		{ 'day':datetime(2009,6,4),  'title':"BBQ at Mom\'s house",      'class':"restaurant", 'url':'/restaurants/9' }]

def foo(request) :
	d = {'events':events, 'date':datetime.now()}
	return render_to_response('foo.html', d)

def bar(request) :
	d = {'events':events, 'date':datetime.now()}
	return render_to_response('bar.html', d)

def index(request, year, month) :
	year, month = int(year), int(month)
	d = {'events':[], 'date':datetime(year, month,1,0,0,0)}
	return render_to_response('foo.html', d)

def event(request, object_id) :
	event = get_object_or_404(Event, pk=object_id)
	d = {'event':event}
	return render_to_response('event.html', d)
