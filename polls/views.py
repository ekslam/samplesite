from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request, 'index.html', context)

def help(request):
    return HttpResponse('This is the help function!')
