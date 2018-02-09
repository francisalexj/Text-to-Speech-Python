from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .lib.gtts_token import Token

def index(request):
	conversion_text = request.POST.get('conversion_text', '')
	gts_token = Token()
	gen_token = gts_token.calculate_token(conversion_text)

	content = {
		'conversion_text': conversion_text,
		'gen_token' : gen_token
	}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(content, request))