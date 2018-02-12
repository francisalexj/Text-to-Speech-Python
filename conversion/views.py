from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .lib.gtts import gTTS
from .models import ConversionModel

def index(request):
	conversion_text = request.POST.get('conversion_text', '')

	cvm = ConversionModel()

	language_list = gTTS.LANGUAGES.items()
	selected_lang = "en"

	audio_save_path = 'static/files/' + cvm.id_generator() + ".mp3"
	conversion_status = False

	if conversion_text!="":
		gts_conversion = gTTS(conversion_text)
		gts_conversion.save(audio_save_path)
		conversion_status = True

	content = {
		'conversion_text': conversion_text,
		'saved_path' : audio_save_path,
		'conversion_status' : conversion_status,
		'language_list' : language_list,
		'selected_lang' : selected_lang,
	}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(content, request))