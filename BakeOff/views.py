from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entry, TimeToVote

def homePage(request):
    timeToVote = TimeToVote.objects.all().first()
    if timeToVote == None:
        toVote = False
    else:
        toVote = timeToVote.timeToVote
    return render(request, "home_page.html", {"voting": toVote})

def enter(request):
    return HttpResponse("Enter Competition")
