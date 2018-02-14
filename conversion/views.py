from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .lib.gtts import gTTS
from .models import ConversionModel

def index(request):
	conversion_text = ''
	conversion_lang = 'en'

	language_list = gTTS.LANGUAGES.items()

	content = {
		'conversion_text': conversion_text,
		'language_list' : language_list,
		'selected_lang' : conversion_lang,
	}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(content, request))

def translate(request):
	if request.method != "POST":
		return redirect('/')

	conversion_text = request.POST.get('conversion_text', '')
	conversion_lang = request.POST.get('conversion_lang', 'en')

	cvm = ConversionModel()

	language_list_master = gTTS.LANGUAGES
	language_list = language_list_master.items()
	selected_lang = (language_list_master[conversion_lang] if conversion_lang in language_list_master else "")

	audio_save_path = 'static/files/' + cvm.id_generator() + ".mp3"
	conversion_status = False

	if conversion_text!="":
		gts_conversion = gTTS(text=conversion_text, lang=conversion_lang)
		gts_conversion.save(audio_save_path)
		conversion_status = True

	content = {
		'conversion_text': conversion_text,
		'saved_path' : audio_save_path,
		'conversion_status' : conversion_status,
		'language_list' : language_list,
		'selected_lang' : selected_lang,
	}
	template = loader.get_template('translate.html')
	return HttpResponse(template.render(content, request))