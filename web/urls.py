"""webのURLパターン定義"""
from django.urls import path
from .applications import decks, skills, views

app_name = "web"
urlpatterns = [
    path("", views.index, name="index"),
    path('register/deck', decks.register_deck, name='register_deck'),
    path('delete/deck', decks.delete_deck, name='delete_deck'),
    path('skills', views.select_skills, name='select_skills'),
    path('register/skill', skills.register_skill, name='register_skill'),
    path('delete/skill', skills.delete_skill, name='delete_skill'),
]
