import locale

from django.shortcuts import render
from django import template
#from django.http import HttpResponse

def home(request):										#для 127.0.0.0	
	#res = str('Привет, Мир!')							#строка в unicode	
	#res = res.encode(locale.getpreferredencoding())    	#перекодируем в удобный для системы (для windows - 1251)
	#return HttpResponse(res,content_type="text/plain") 	#при удалении параметра content_type выводится нечитаемая строка
														#если в параметр передать пустую строку - ничего не меняется
	return render(request, 'templates/index.html')
	
	
def hello(request):										#для 127.0.0.0/hello/
	return render(request, 'templates/static_handler.html')