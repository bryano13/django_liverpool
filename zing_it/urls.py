from django.urls import path
from zing_it import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team', views.team, name="team"),
    path('add_players', views.add_players),
    path('tweets', views.tweets, name="tweets"),
    path('shop', views.shop, name="shop")
]