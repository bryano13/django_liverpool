from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import json
from .models import Player

# Create your views here.

with open("players_list.json") as f:
    players = json.load(f)


def add_players(request):
    for player in players:
        obj = Player.objects.create(**player)
        obj.save()
    return HttpResponse("Players Added")


def home(request):
    return render(request, "zing_it/home.html")


def team(request):
    players_db = Player.objects.all()
    return render(request,'zing_it/team.html', {"players": players_db})


def shop(request):
    return render(request, "zing_it/shop.html")


def tweets(request):
    return render(request, "zing_it/tweets.html")
