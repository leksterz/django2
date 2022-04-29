from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from .models import Question, Availability

def index(request):
    latest_availability_list = Availability.objects.order_by('-date_of_session')[:5]
    context = {'latest_availability_list': latest_availability_list}
    return render(request, 'polls/index.html', context)


def detail(request, date):  
    latest_availability_list = Availability.objects.order_by('-date_of_session')[:5]
    context = {'latest_availability_list': latest_availability_list}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)