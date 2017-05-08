from django.shortcuts import render
from django.http import HttpResponse
from .models import words
# Create your views here.
def index(request):
    word_list=words.objects.order_by('-words_number')
    context = {'word_list':word_list}
    return render(request,'check_word/index.html',context)
def add(request):
    add_word = request.GET['word']
    if len(words.objects.filter(words_text=add_word)) > 0:
        result = words.objects.get(words_text=add_word)
        result.words_number=result.words_number+1
        result.save()
        return HttpResponse("existed!")
    else:
        result=words(words_text=add_word,words_number=1)
        result.save()
        return HttpResponse("created!")
