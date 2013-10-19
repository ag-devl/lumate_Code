from guestbook.models import Visitor
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

# Create your views here.	
def index(request):	
	f_name = request.POST.get('firstname') 
	l_name = request.POST.get('lastname')
	try:
	        if f_name:
			f_name = request.POST.get('firstname')
        		l_name = request.POST.get('lastname')
			p = Visitor(first_name = f_name,last_name = l_name,visited_on = datetime.datetime.today())
			p.save()
	except KeyError:
		f_name = 'default'
	return render_to_response ('guestbook/index.html',context_instance=RequestContext(request))	


def entry(request):
	visitor_array = Visitor.objects.all()
	return render_to_response ('guestbook/entry.html', {'visitor_list': visitor_array})
