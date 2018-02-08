from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	content = {
		'foo': 'Alter bar'
	}
	return HttpResponse(template.render(content, request))