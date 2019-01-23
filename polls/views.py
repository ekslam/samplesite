from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from .forms import QuestionModelForm
from datetime import datetime

# Create your views here.

def index(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request,'index.html',context)

def help(request):
    return HttpResponse('This is the help function!')

def detail(request, question_id):
    context = {}
    context['question'] = Question.objects.get(id=question_id)
    return render(request, 'detail.html', context)

def update(request, question_id):
    context = {}
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = QuestionModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponse('Question updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        #question = Question.objects.get(id=question_id)
        context['form'] = QuestionModelForm(instance=question)
        #context['q_id'] = question_id
    return render(request, 'update.html', context)


def create(request):
    context = {}
    context['form'] = QuestionModelForm(initial={'pub_date' : datetime.now()})
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls/')
        else:
            context['form'] = form
            render(request, 'create.html', context)
    else:
        return render(request, 'create.html', context)
