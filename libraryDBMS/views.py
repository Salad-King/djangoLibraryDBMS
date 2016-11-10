import datetime;
from django.http import HttpResponse
def current_datetime(request):
	now = datetime.datetime.now()
	data = "<html><body>The program responded with %s</body></html>" % now
	return(HttpResponse(data))
	
def hoursAhed(request,value):
	value = int(value)
	deltaInTime = datetime.datetime.now() + datetime.timedelta(hours = value)
	data = "<html><body>In %s "
	if value == 1:
		data += "hour " 
	else:
		data += "hours " 
	data += "will be %s</body></html>"
	return(HttpResponse( data % (str(value),deltaInTime)))
	
