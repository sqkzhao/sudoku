from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_game', views.new_game),
    path('board', views.board),
    # path('validate', views.validate),
]
